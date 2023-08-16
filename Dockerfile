FROM rocm/pytorch
MAINTAINER Viraj Shah <viraj.v.shah03@gmail.com>

RUN apt-get update -y

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install fastai
RUN python3 -m pip install jupyter

EXPOSE 1337

CMD ["jupyter", "notebook", "--allow-root", "--port=1337", "--ip=0.0.0.0"]
