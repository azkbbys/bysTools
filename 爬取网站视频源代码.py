import sys
import time
from tkinter import messagebox
from tkinter import *
import os
os.system('attrib -h pz.pz')
try:
    pz = open('./pz.pz','r')
    lianjie = pz.readline()
except:
    pz = open('./pz.pz','w')
    pz.close()
    pz = open('./pz.pz','r')
    lianjie = pz.readline()
pz.close()
if lianjie == '':
    os.system('cls')
    print('正在进行初始配置...')
    print('|━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    time.sleep(0.4)
    os.system('cls')
    print('正在进行初始配置...')
    print('━━━━━━━━━━━━━━|━━━━━━━━━━━━━━━━━━━━━━━━━')
    time.sleep(0.4)
    os.system('cls')
    print('正在进行初始配置...')
    print('━━━━━━━━━━━━━━━━━━━|━━━━━━━━━━━━━━━━━━━━')
    time.sleep(0.4)
    os.system('cls')
    print('正在进行初始配置...')
    print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━|━━━━━━━━━━')
    time.sleep(0.4)
    os.system('cls')
    print('正在进行初始配置...')
    print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━|')
    time.sleep(0.4)
    os.system('cls')
    print('初始配置成功')
    if messagebox.askyesno('链接获取方式','手动输入链接（是）\n自动获取链接（否）\n建议手动输入，自动获取容易bug') == True:
        lianjie = input('请输入当前文件夹的完整（一定要完整！）位置：\n')
        print('正在写入配置文件...')
        time.sleep(1)
        print('写入成功！')
        time.sleep(1)
        os.system('cls')
    else:
        lianjie = os.path.dirname(os.path.realpath(__file__))
        print('链接自动获取成功，请确定本程序所处文件夹是否为'+lianjie)
    
    pz = open('./pz.pz','w')
    os.system('attrib ./pz.pz +h')
    pz.write(lianjie)
    pz.close()
    print('即将运行程序...')
    time.sleep(2)
    os.system('cls')

def del_pz():
    os.system('attrib pz.pz -h')
    os.system('del .\\pz.pz')
    print('删除成功！再次使用程序需要重新配置')
    time.sleep(2)
    sys.exit()

def get_url():
    global format
    format = entry_format.get()
    global url
    url = entry_url.get()
    ts_label1 = Label(root, text='正在爬取', font=('宋体', 15), fg='black', bg='white')  # 设置组件
    ts_label1.place(x=0, y=0, width=500, height=350)
    if format != '':
        ts_label2 = Label(root, text='命令已执行，请转到控制台窗口', font=('宋体', 15), fg='black', bg='white')  # 设置组件
        ts_label2.place(x=0, y=0, width=500, height=350)
        root.title('不要关掉窗口，不然会bug滴~')#窗口标题
        os.system(str(you_get_url)+' '+str(format)+' -o '+lianjie+'/下载后的视频 '+str(url))
        os.system('start '+lianjie+'/下载后的视频')
        print('下载成功！2s后自动关闭')
        time.sleep(2)
        sys.exit()
    else:
        ts_label2 = Label(root, text='命令已执行，请转到控制台窗口', font=('宋体', 15), fg='black', bg='white')  # 设置组件
        ts_label2.place(x=0, y=0, width=500, height=350)
        root.title('不要关掉窗口，不然可能会bug滴~')#窗口标题
        os.system(str(you_get_url)+' -o '+lianjie+'/下载后的视频 '+str(url))
        os.system('start '+lianjie+'/下载后的视频')
        print('下载成功！2s后自动关闭')
        time.sleep(2)
        sys.exit()

def jc():
    os.system('start '+lianjie+'/doc/程序使用教程.doc')

you_get_url = lianjie + '/you-get/you-get.exe'
root = Tk()
root.title('爬取网站视频')#窗口标题
root.geometry('500x500')
try:
    root.iconbitmap(lianjie+' /logo/logo.ico')
except:
    print('设置logo失败')

'''
设置视频清晰度
'''
entry_format = Entry(root,font = ('宋体',10))#设置输入框
entry_format.place(x = 50,y = 60,width = 400,height = 30)#显示组件
format_label = Label(root,text = '输入视频清晰度\n可不填',font = ('宋体',13),fg = 'black',bg = 'white')#设置组件
format_label.place(x = 175,y = 5,width = 150,height = 50)
'''
输入链接
'''
entry_url = Entry(root,font = ('宋体',10))#设置输入框
entry_url.place(x = 50,y = 260,width = 400,height = 30)#显示组件
url_label = Label(root,text = '输入视频链接',font = ('宋体',15),fg = 'black',bg = 'white')#设置组件
url_label.place(x = 175,y = 205,width = 150,height = 50)
get_url_button = Button(root,text = '确定',font = ('宋体',10),fg = 'black',bg = 'white',command = get_url)#设置按钮
get_url_button.place(x = 225,y = 300,width = 50,height = 40)#显示按钮
'''
删除配置文件pz.pz
'''
del_pz = Button(root,text = '删除配置文件',font = ('宋体',9),fg = 'white',bg = 'red',command = del_pz) # type: ignore
del_pz.place(x = 420,y = 480,width = 80,height = 20)
'''
教程
'''
ckjc = Button(root,text = '查看教程',font = ('宋体',9),fg = 'black',bg = 'white',command = jc)
ckjc.place(x = 420,y = 460,width = 80,height = 20)
'''
屏幕主循环
'''
root.mainloop()
