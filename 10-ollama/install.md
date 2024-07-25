### ollama install

```shell
curl -fsSL https://ollama.com/install.sh | sh
```

### ollama ctl

```shell
systemctl status ollama
systemctl stop ollama
systemctl start ollama
sudo lsof -i :11434
```

### 模型下载

```python
# Model Download
# pip install modelscope
from modelscope import snapshot_download

model_path = 'LLM-Research/Meta-Llama-3.1-8B-Instruct'
cache_path = '/mnt/data/llch/Llama3.1-8B-Ins'
snapshot_download(model_path, cache_dir=cache_path)
```

### 合并gguf

- gguf==>gguf

https://modelscope.cn/models/qwen/Qwen2-57B-A14B-Instruct-GGUF

https://github.com/ggerganov/llama.cpp/discussions/6404

https://github.com/ggerganov/llama.cpp/pull/6135

https://github.com/ollama/ollama/blob/main/docs/import.md

```shell
假设有:
qwen2-57b-a14b-instruct-q8_0-00001-of-00002.gguf
qwen2-57b-a14b-instruct-q8_0-00002-of-00002.gguf

git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
make
#  找到最后一个00002.gguf即可
./llama-gguf-split --merge qwen2-57b-a14b-instruct-q8_0-00001-of-00002.gguf qwen2-57b-a14b-instruct-q8_0.gguf

# Modelfile参考
FROM /mnt/data/qwen1_5-14b-chat-q8_0.gguf
  
TEMPLATE """{{ if .System }}<|im_start|>system
{{ .System }}<|im_end|>{{ end }}<|im_start|>user
{{ .Prompt }}<|im_end|>
<|im_start|>assistant
"""

PARAMETER stop "<|im_start|>"
PARAMETER stop "<|im_end|>"
```

- safetensors==>gguf

```text
python convert_hf_to_gguf.py --help
python convert_hf_to_gguf.py  <path_to_safetensor_file> --outfile <path_to_gguf_file> --outtype {f32,f16,bf16,q8_0,auto}
python convert_hf_to_gguf.py /mnt/data/llch/Llama3.1-8B-Ins/LLM-Research/Meta-Llama-3___1-8B-Instruct --outfile /mnt/data/llch/Llama3.1-8B-Ins/Llama3.1-8B-Ins.gguf --outtype f16
```

```text
vi Modelfile

FROM /mnt/data/llch/Llama3.1-8B-Ins/Llama3.1-8B-Ins.gguf
TEMPLATE """
{{ if .Messages }}
{{- if or .System .Tools }}<|start_header_id|>system<|end_header_id|>
{{- if .System }}

{{ .System }}
{{- end }}
{{- if .Tools }}

You are a helpful assistant with tool calling capabilities. When you receive a tool call response, use the output to format an answer to the orginal use question.
{{- end }}<|eot_id|>
{{- end }}
{{- range $i, $_ := .Messages }}
{{- $last := eq (len (slice $.Messages $i)) 1 }}
{{- if eq .Role "user" }}<|start_header_id|>user<|end_header_id|>
{{- if and $.Tools $last }}

Given the following functions, please respond with a JSON for a function call with its proper arguments that best answers the given prompt.

Respond in the format {"name": function name, "parameters": dictionary of argument name and its value}. Do not use variables.

{{ $.Tools }}
{{- end }}

{{ .Content }}<|eot_id|>{{ if $last }}<|start_header_id|>assistant<|end_header_id|>

{{ end }}
{{- else if eq .Role "assistant" }}<|start_header_id|>assistant<|end_header_id|>
{{- if .ToolCalls }}

{{- range .ToolCalls }}{"name": "{{ .Function.Name }}", "parameters": {{ .Function.Arguments }}}{{ end }}
{{- else }}

{{ .Content }}{{ if not $last }}<|eot_id|>{{ end }}
{{- end }}
{{- else if eq .Role "tool" }}<|start_header_id|>ipython<|end_header_id|>

{{ .Content }}<|eot_id|>{{ if $last }}<|start_header_id|>assistant<|end_header_id|>

{{ end }}
{{- end }}
{{- end }}
{{- else }}
{{- if .System }}<|start_header_id|>system<|end_header_id|>

{{ .System }}<|eot_id|>{{ end }}{{ if .Prompt }}<|start_header_id|>user<|end_header_id|>

{{ .Prompt }}<|eot_id|>{{ end }}<|start_header_id|>assistant<|end_header_id|>

{{ end }}{{ .Response }}{{ if .Response }}<|eot_id|>{{ end }}
"""
SYSTEM """You are a helpful assistant. 你是一个乐于助人的助手。"""
PARAMETER stop <|start_header_id|>
PARAMETER stop <|end_header_id|>
PARAMETER stop <|eot_id|>

ollama create Llama3.1-8B-Ins -f Modelfile
ollama run Llama3.1-8B-Ins
```

### env

```
vi /etc/systemd/system/ollama.service
Environment="OLLAMA_MODELS=/mnt/data/ollama/models"
Environment="OLLAMA_HOST=0.0.0.0"
```

```text
~# cat /etc/systemd/system/ollama.service
[Unit]
Description=Ollama Service
After=network-online.target

[Service]
ExecStart=/usr/bin/ollama serve
User=ollama
Group=ollama
Restart=always
RestartSec=3
Environment="OLLAMA_HOST=0.0.0.0:11434"

[Install]
WantedBy=default.target
```