# fastai_rocm

## NOTE:
**This docker image is functional, I have however, found a better way**
- Install pytorch for rocm via pip from <a href="https://pytorch.org/get-started/locally/">here</a>
- Install fastai normally using the command `pip install fastai`
- Thats it, it works, tensorflow has the exact same process

### The output on my machine
![image](https://github.com/viraj-s15/fastai_rocm_docker/assets/79002760/1443d727-5cf2-401a-874d-f97df2573471)

![image](https://github.com/viraj-s15/fastai_rocm_docker/assets/79002760/42742dd7-3b7a-416e-95cb-120c0053c522)

I am able to use the discrete gpu with torch just as I would with cuda. 
If one still wants to confirm whether, the gpu is active or not, you can run
`python main.py` and look at the time difference. 

--------------------------------------------------------------------------------------------------------------------------------

This project generates a docker image that enables rapid development with the [fast.ai v1](https://github.com/fastai/fastai) library with Modern AMD graphics cards through the [Rocm stack](https://github.com/RadeonOpenCompute/ROCm).

This docker image contains:

* Jupyter Notebook
* Pytorch
* Fast.ai
* Rocm Utilities
* Python 3.6

Usage
```bash
sudo docker run -it -v $HOME:/data -p 1337:1337 --privileged --rm --device=/dev/kfd --device=/dev/dri --group-add video briangorman/fastai_rocm
```

Your home directory will be exposed in /data. The docker container will output a link to access the jupyter notebook


## Requirements
[Modern Linux kernel](https://rocm.github.io/ROCmInstall.html#rocm-support-in-upstream-linux-kernels)

[Hardware](https://rocm.github.io/ROCmInstall.html#hardware-support)
