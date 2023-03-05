# pywxbot

pywxbot 是一个微信机器人框架


## Quick Start

### 安装

可以通过本命令安装pywxbot：

`pip install  pywxbot -i https://pypi.douban.com/simple/`

### 使用实例
```python
import pywxbot

app = pywxbot.WxBot()

# 监听消息
@app.watch('文件传输助手')
def on_message(msg):
    return f'recv : {msg.txt}'

app.run()
```
