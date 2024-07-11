```shell
curl -fsSL https://ollama.com/install.sh | sh
```

```shell
systemctl status ollama
systemctl stop ollama
systemctl start ollama
sudo lsof -i :11434
```

合并gguf
(https://modelscope.cn/models/qwen/Qwen2-57B-A14B-Instruct-GGUF)
(https://github.com/ggerganov/llama.cpp/discussions/6404)

```shell
假设有:
qwen2-57b-a14b-instruct-q8_0-00001-of-00002.gguf
qwen2-57b-a14b-instruct-q8_0-00002-of-00002.gguf

git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
make
合并:
./llama-gguf-split --merge qwen2-57b-a14b-instruct-q8_0-00001-of-00002.gguf qwen2-57b-a14b-instruct-q8_0.gguf
```
