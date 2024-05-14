FROM python:3.10.12-alpine3.18
COPY . /root
ENV TZ=Asia/Shanghai
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories &&  apk add curl git tzdata && pip3 install -U --pre aiogram

WORKDIR /aigramBot
ENTRYPOINT ["sh", "/root/run.sh"]