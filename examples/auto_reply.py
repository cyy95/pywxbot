import src.pywxbot as wxbot

app = wxbot.WxBot()


@app.watch('文件传输助手')
def auto_reply(msg):
    return f'recv : {msg.txt}'


app.run()
