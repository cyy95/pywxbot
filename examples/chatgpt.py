import pywxbot as wxbot
import openai

openai.api_key = 'YOUR_API_KEY'

app = wxbot.WxBot()


@app.watch('微信群名称')
def auto_reply(msg):
    if not msg.txt.startswith('bot'):
        return
    try:

        resp = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "你是一个大语言模型."},
                {"role": "user", "content": msg.txt[3:]},
            ]
        )
        print(resp.choices[0].message.content)
        return f'@{msg.nick_name} {resp.choices[0].message.content}'
    except Exception as e:
        print(e)
        return f'@{msg.nick_name} 问得太快了，请重试'


app.run()
