```
# pip install modelscope
from modelscope import snapshot_download

model_path = 'LLM-Research/Meta-Llama-3.1-8B-Instruct'
cache_path = '/mnt/data/llch/Llama3.1-8B-Ins'
model_path = 'openbmb/minicpm-v-2_6'
cache_path = '/mnt/data/llch/cpm2.6'
snapshot_download(model_path, cache_dir=cache_path)
```

