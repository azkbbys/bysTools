from time import sleep
import tkinter.messagebox
from functions.easyprompt import *
import functions.info
from os import system
import tkinter

import functions.update
def exitnow():
    sleep(1)
    info('程序运行结束')
    exit()
print('欢迎使用bysTools!\n本程序为@阿兹卡班毕业生 制作，保留所有权利，部分外部软件/程序作者请查看readme.md\n本软件完全免费，请勿套壳销售，如发现此类行为请使用以下方式联系作者\n联系方式：\nQQ：2379056156\nwx:oyr_nszbd\nGitHub：azkbbys\n（联系方式可能会失效，届时请尝试其他方式）\n')
# info('将在1秒内运行程序')
# sleep(1)
try:
    with open('config.txt') as f:
        pass
except:
    error('配置文件不存在，正在创建')
    with open('config.txt','w') as f:
        f.write('version: {v}\n'.format(v=functions.info.version))
    info('配置文件创建成功！请尝试重新运行程序！')
    exitnow()
with open('config.txt') as f:
    config = f.readlines()
info('配置文件读取成功')
info('正在检查更新')
if(functions.update.check()=='已是最新版本'):
    info('已是最新版本'+functions.info.version)
elif(functions.update.check()=='无法连接到更新服务器，请检查网络连接'):
    warn('无法连接到更新服务器，请检查网络连接')
elif(functions.update.check().startswith('有新版本可用')):
    warn('有新版本可用，正在弹出更新窗口')
    if(tkinter.messagebox.askyesno('有新版本可用','有新版本可用，是否更新？')):
        system('start https://github.com/azkbbys/bysTools/releases')
info('尝试打开主界面')
warn('请不要关闭本界面')
root = tkinter.Tk()
root.title('bysTools-v'+functions.info.version)
root.geometry('500x500')
root.iconbitmap('./images/作品快速点赞.ico')
root.resizable(False, False)
lable = tkinter.Label(root, text='bysTools\n请点击下方按钮选择功能', font=('微软雅黑', 15))
lable.pack()
website_button = tkinter.Button(root, text='官方网站', font=('微软雅黑', 10), command=lambda: system('start https://azkbbys.github.io'))
website_button.place(x=500-70, y=500-30, width=70, height=30)
button1 = tkinter.Button(root, text='时间戳转换', font=('微软雅黑', 15), command=lambda: system('start https://azkbbys.github.io'))
button1.place(x=100, y=100, width=300, height=50)
root.mainloop()