name="main.py"
while true
do

    source /root/update.sh
    pip install -i https://mirrors.aliyun.com/pypi/simple/ -r requirements.txt
    python3 ${name}
done