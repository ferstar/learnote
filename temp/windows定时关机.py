# coding=utf8
import os
import threading
import time

import pyHook  # 在http://www.lfd.uci.edu/~gohlke/pythonlibs/#pyhook这里下载, 用pip安装
import pythoncom  # 在https://sourceforge.net/projects/pywin32/files/pywin32/Build%20220/这里下载安装

last_time = time.time()
flag = False

def shut_down():
    while 1:
        time.sleep(1)
        new_time = time.time()
        # print("new time: {}".format(new_time))
        if new_time - last_time > 1800:  # 30分钟无按键响应就关机
            os.system("shutdown /s /t 1")  # 1秒后关机


def OnMouseEvent(event):
    global last_time
    last_time = time.time()
    # print("old time: {}".format(last_time))
    return True


def OnKeyboardEvent(event):
    global last_time, flag
    if not flag and str(event.Key) == 'Space':  # 按下空格键启动子线程计时
        t = threading.Thread(target=shut_down)
        t.setDaemon(True)  # 设定主线程结束时自动杀掉子线程
        t.start()
        flag = True
    last_time = time.time()
    # print("old time: {}".format(last_time))
    if str(event.Key) == 'Escape':  # 按下ESC退出程序
        exit()
    # print(event.Key)
    return True


def main():
    # create the hook mananger
    hm = pyHook.HookManager()
    # register two callbacks
    hm.MouseAllButtonsDown = OnMouseEvent
    hm.KeyDown = OnKeyboardEvent
    # hook into the mouse and keyboard events
    hm.HookMouse()
    hm.HookKeyboard()
    pythoncom.PumpMessages()


if __name__ == "__main__":
    main()
