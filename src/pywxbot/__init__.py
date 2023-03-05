import time

import psutil
import pyautogui
import pyperclip
from pywinauto import Application, mouse


class Message:
    def __init__(self, nick_name, txt, is_myself=False):
        self.nick_name = nick_name
        self.txt = txt
        self.is_self = is_myself

    def __str__(self):
        return f'{self.nick_name}:{self.txt},is_self:{ self.is_self}'

    def __eq__(self, other):
        return self.nick_name == other.nick_name and self.txt == other.txt and self.is_self == other.is_self


class WxBot:
    def __init__(self):
        pids = psutil.process_iter()
        pid = None
        self.items_func = {}
        # 遍历全部进程ID
        for p in pids:
            if p.name() == 'WeChat.exe':
                pid = p.pid
                break
        if pid is None:
            raise Exception('WeChat is not running')
        self.app = Application(backend="uia").connect(process=pid)
        self.win = self.app[u'微信']
        self.win.set_focus()

    def watch(self, name):
        def decorator(func):
            self.items_func[name] = {'callback': func, 'last_msg_list': None}

        return decorator

    def get_all_msg(self):
        chat_box = self.win.child_window(title="消息", control_type="List")
        all_ctrls = chat_box.wrapper_object().descendants()

        msg_list = []

        for ctrl in all_ctrls:
            txt = ctrl.window_text()
            childs = ctrl.children()
            if len(childs) < 1:
                continue
            childs = ctrl.children()[0].children()
            if len(childs) < 1:
                continue
            author = childs[0].window_text()
            last_name = childs[-1].window_text()
            if last_name != '' and txt != '':
                msg_list.append(Message(last_name, txt, is_myself=True))
                continue

            if author == '' or txt == '':
                continue

            msg_list.append(Message(author, txt))

        return msg_list

    def run(self):
        if len(self.items_func) == 0:
            return

        while True:

            for (group_name, group) in self.items_func.items():

                search = self.win.child_window(title=group_name, control_type="ListItem")
                cords = search.rectangle()
                mouse.click(button='left', coords=((cords.left + cords.right) // 2, (cords.top + cords.bottom) // 2))

                last_msg_list = group.get('last_msg_list')
                cb = group.get('callback')
                all_msgs = self.get_all_msg()
                if last_msg_list is None:
                    group['last_msg_list'] = all_msgs
                    continue

                if last_msg_list[-1] == all_msgs[-1]:
                    # print('没有新消息')
                    continue

                for index in range(len(all_msgs)):
                    if all_msgs[-index - 1] == last_msg_list[- 1]:
                        break

                group['last_msg_list'] = all_msgs
                newest = all_msgs[-index:]
                for msg in newest:
                    ret = cb(msg)
                    if ret is None:
                        continue
                    send_msg(ret)

            time.sleep(1)


def send_msg(txt: str):
    pyperclip.copy(txt.replace('|', '\n'))
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('enter')
