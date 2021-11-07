#-*- coding : utf-8-*-
# coding:utf-8
import pickle
import tkinter as tk
import tkinter.messagebox
import time
import datetime


def acdincrease(code=None):
    acd = []
    acd.append(code)
    return acd
def codda():
    global npff
    npff = '建设者牛逼'
    return npff
def at2():
    global miyaos
    window_sign_up2 = tk.Tk()
    window_sign_up2.geometry('350x200')
    window_sign_up2.title('内部人员登录')
    new_pwd = tk.StringVar()
    tk.Label(window_sign_up2, text='请输入秘钥： ').place(x=60, y=50)
    miyao = tk.StringVar()
    miyaos = tk.Entry(window_sign_up2, textvariable=miyao, show='*')
    miyaos.place(x=170, y=50)
    bt_confirm_sign_up2 = tk.Button(window_sign_up2, text='确认登录', command=at3, bg='red')
    bt_confirm_sign_up2.place(x=150, y=120)
    window_sign_up2.mainloop()
    time.sleep(30)
    at3()
def at3():
    global acd
    miyao = miyaos.get()
    if miyao != npff:
        tk.messagebox.askyesno('认定失败', '请核对好后再等')
    else:
        windows = tk.Tk()
        # 图
        windows.title('激活码')
        windows.geometry('450x300')
        tk.Canvas(windows, heigh=400, width=300)
        # 提示语（文本框）
        tk.Label(windows, text='激活码：').place(x=100, y=150)
        # 输入框
        calds = tk.StringVar()
        colds = tk.Entry(windows, textvariable=calds)
        colds.place(x=160, y=150)
        def acdincrease(code):
            open('code.text', 'a').write(code+"\n")
            # data=pd.read_csv(io,encoding='utf-8')
            have_code = open('code.text', 'r').read()
        def yes():
            code = colds.get()
            acdincrease(code)
        # 确定键
        bt_up = tk.Button(windows, text='确定', command=yes, bg='blue')
        bt_up.place(x=210, y=230)
        # 退出键
        bt_quit = tk.Button(windows, text='退出', command=quit, bg='grey')
        bt_quit.place(x=280, y=230)
        '''
        删除激活码
        '''
