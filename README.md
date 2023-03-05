# pywxbot

pywxbot 是一个微信机器人框架,通过模拟鼠标键盘操作微信Window客户端实现自动回复等功能。

## 特性

- [x] 消息监听
- [ ] 消息发送
- [ ] 好友搜索
- [ ] 好友自动通过
- ......

## Quick Start

### 安装

可以通过本命令安装pywxbot：

`pip install  pywxbot -i https://pypi.douban.com/simple/`

### 使用实例

1.启动Windows微信客户端

2.登录微信

3.把聊天对象搜索到聊天列表中，确保聊天对象在左侧聊天列表中处于可见状态

4.运行下面的代码

```python
import pywxbot

app = pywxbot.WxBot()

# 监听消息
@app.watch('文件传输助手')
def auto_reply(msg):
    return f'recv : {msg.txt}'

app.run()
```
