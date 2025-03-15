from time import sleep
from functions.easyprompt import *
import functions.info
import tkinter
def exitnow():
    sleep(1)
    info('程序运行结束')
    exit()
print('欢迎使用bysTools!\n本程序为@阿兹卡班毕业生 制作，保留所有权利，部分外部软件/程序作者请查看readme.md\n本软件完全免费，请勿套壳销售，如发现此类行为请使用以下方式联系作者\n联系方式：\nQQ：2379056156\nwx:oyr_nszbd\nGitHub：azkbbys\n（联系方式可能会失效，届时请尝试其他方式）\n')
info('将在1秒内运行程序')
sleep(1)
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
info('尝试打开主界面')
warn('请不要关闭本界面')
root = tkinter.Tk()
root.title('bysTools-v'+functions.info.version)
root.geometry('300x300')
root.iconbitmap('./images/作品快速点赞.ico')
root.mainloop()