![img.png](..%2Fusing_files%2Fcomfyui%2Fimg.png)

### install

```shell
cd /mnt/data/llch/
git clone https://github.com/aceliuchanghong/ComfyUI.git
cd /mnt/data/llch/ComfyUI
```

### env

```shell
conda create -n ComfyUI python=3.10
conda create -p /mnt/data/llch/env/ComfyUI python=3.10
source activate /mnt/data/llch/env/ComfyUI
pip install -r requirements.txt
du -sh
watch -n 1 nvidia-smi
```

### model

```shell
wget https://huggingface.co/runwayml/stable-diffusion-v1-5/blob/main/v1-5-pruned-emaonly.ckpt
```

### run

```shell
python main.py --listen 0.0.0.0
nohup python main.py --listen 0.0.0.0>vcomfyui.log &
```
