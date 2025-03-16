from time import sleep
import tkinter.messagebox
from functions.easyprompt import *
import functions.info
from os import system
import tkinter
import functions.update
from os import listdir
from os.path import isdir
import subprocess
import os
def exitnow():
    sleep(1)
    info('程序运行结束')
    exit()
def program(name:str):
    add_ons = listdir(path+'add-ons')
    # info('查找到程序'+str(add_ons))
    add_ons = [i for i in add_ons if isdir(path+'add-ons/'+i)]
    # 判断是否有这个程序
    if name in add_ons:
        # 执行这个程序
        info('运行程序'+name)
        system('start '+path+'add-ons/'+name+'/main.exe')
    else:
        warn('找不到程序'+name+'，正在引导下载')
        not tkinter.messagebox.askyesno('下载附加程序', '要运行此功能，您需要下载附加包'+name+'，点击“是”将打开下载页面') or system('start https://github.com/azkbbys/'+name+'/releases')

print('欢迎使用bysTools!\n本程序为@阿兹卡班毕业生 制作，保留所有权利，部分外部软件/程序作者请查看readme.md\n本软件完全免费，请勿套壳销售，如发现此类行为请使用以下方式联系作者\n联系方式：\nQQ：2379056156\nwx:oyr_nszbd\nGitHub：azkbbys\n（联系方式可能会失效，届时请尝试其他方式）\n')
# info('将在1秒内运行程序')
# sleep(1)
try:
    with open('config.txt') as f:
        pass
except:
    error('配置文件不存在，正在创建')
    info('请在下方输入本程序安装路径，以你的盘符开始，以“bysTools\\”结尾')
    path = input()
    # 用户输入路径并写入系统环境变量
    subprocess.run(['setx', 'BYSTOOLS', path, '/M'], shell=True)
    info(f'已将路径 {path} 写入系统环境变量 BYSTOOLS')
    with open('config.txt','w') as f:
        f.write('version: {v}\n'.format(v=functions.info.version))
    info('配置文件创建成功！请尝试重新运行程序！')
    exitnow()
with open('config.txt') as f:
    config = f.readlines()
info('配置文件读取成功')
path = os.getenv('BYSTOOLS').replace('\\','/')
info('已获取环境变量BYSTOOLS:'+str(path))
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
root.iconbitmap(path+'images\icon.ico')
root.resizable(False, False)
lable = tkinter.Label(root, text='bysTools\n请点击下方按钮选择功能', font=('微软雅黑', 15))
lable.pack()
website_button = tkinter.Button(root, text='官方网站', font=('微软雅黑', 10), command=lambda: system('start https://azkbbys.github.io'))
website_button.place(x=500-70, y=500-30, width=70, height=30)
button1 = tkinter.Button(root, text='时间转时间戳', font=('微软雅黑', 15), command=lambda: program('timeToStamp'))
button1.place(x=100, y=100, width=300, height=50)
root.mainloop()