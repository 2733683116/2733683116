import tkinter as tk
import tkinter.messagebox
import pickle


window = tk.Tk()
window.title('欢迎进入学习系统，希望你使用愉快')
window.geometry('450x300')
tk.Canvas(window, heigh=400, width=300)
canvas = tk.Canvas(window, height=300, width=500)
image_file = tk.PhotoImage(file=r'D:\python代码区\照片素材\001.png')
image = canvas.create_image(0, 0, anchor='nw', image=image_file)
canvas.pack(side='top')
tk.Label(window, text='用户名:').place(x=100, y=150)
tk.Label(window, text='密码').place(x=100, y=190)
var_usr_name = tk.StringVar()
entry_usr_name = tk.Entry(window, textvariable=var_usr_name)
entry_usr_name.place(x=160, y=150)
var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')
entry_usr_pwd.place(x=160, y=190)


def usr_in():
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    try:
        with open('usr_info.pickle', 'rb') as usr_file:
            usr_info = pickle.load(usr_file)
    except FileExistsError:
        with open('usr_info.pickle', 'wb') as usr_file:
            usrs_info = {'admin': 'admin'}
            pickle.dump(usrs_info, usr_file)
    f = 1
    for i in usr_name:
        if 255 >= ord(i) >= 128:
            f = 0
    k = 1
    for ii in usr_pwd:
        if 255 >= ord(ii) >= 128:
            k = 0
    if usr_name in usr_info:
        if usr_pwd == usr_info[usr_name]:
            tk.messagebox.showinfo(title='Welcome', message='欢迎您：' + usr_name)
        else:
            tk.messagebox.showinfo(message='密码错误')
    elif usr_name == '':
        tk.messagebox.showinfo(message='用户名不能为空')
    elif usr_pwd == '':
        tk.messagebox.showinfo(message='密码不能为空')
    elif ' ' in usr_name:
        tk.messagebox.showinfo(message='用户名内不可存在空格')
    elif ' ' in usr_pwd:
        tk.messagebox.showinfo(message='密码内不可存在空格')
    elif f == 0:
        tk.messagebox.showinfo(message='用户名不可存在中文')
    elif k == 0:
        tk.messagebox.showinfo(message='密码内不可存在中文')
    else:
        is_signup = tk.messagebox.askyesno('欢迎', '系统检测到您还未有注册， 是否现在注册？')


def usr_up():
    def sign_cg():
        nn = new_name.get()
        np = new_pwd.get()
        npf = new_pwd_confirm.get()
        f = 1
        for i in nn:
            if 255 >= ord(i) >= 128:
                f = 0
        k = 1
        for ii in np:
            if 255 >= ord(ii) >= 128:
                k = 0
        try:
            with open('usr_info.pickle', 'rb') as usr_file:
                exist_usr_info = pickle.load(usr_file)
        except FileExistsError:
            exist_usr_info = {}
        if nn in exist_usr_info:
            tk.messagebox.showerror('注册错误', '该用户名已存在，无法注册，请登录')
        elif nn == '':
            tk.messagebox.showerror('注册失败', '用户名内未检测到数据')
        elif np == '':
            tk.messagebox.showerror('注册失败', '密码内未检测到数据')
        elif f == 0:
            tk.messagebox.showerror('注册失败', '用户名不可存在中文')
        elif k == 0:
            tk.messagebox.showerror('注册失败', '密码不可存在中文')
        elif np != npf:
            tk.messagebox.showerror('注册失败', '密码前后不一致')
        else:
            exist_usr_info[nn] = np
            with open('usr_info.pickle', 'wb') as usr_file:
                pickle.dump(exist_usr_info, usr_file)
            tk.messagebox.showinfo('欢迎', '注册成功!恭喜你成为学习系统的一员!!!')
            window_sign_up.destroy()

    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry('350x200')
    window.title('学习系统注册')
    window.geometry('450x300')
    tk.Canvas(window, heigh=400, width=300)
    canvas = tk.Canvas(window, height=300, width=500)
    image_file = tk.PhotoImage(file=r'D:\python代码区\照片素材\001.png')
    image = canvas.create_image(0, 0, anchor='nw', image=image_file)
    canvas.pack(side='top')
    new_name = tk.StringVar()
    tk.Label(window_sign_up, text='用户名： ').place(x=10, y=10)
    tk.Entry(window_sign_up, textvariable=new_name).place(x=150, y=10)
    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text='请输入密码： ').place(x=10, y=50)
    tk.Entry(window_sign_up, textvariable=new_pwd, show='*').place(x=150, y=50)
    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text='请再次输入密码： ').place(x=10, y=90)
    tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*').place(x=150, y=90)
    bt_confirm_sign_up = tk.Button(window_sign_up, text='确认注册', command=sign_cg)
    bt_confirm_sign_up.place(x=150, y=130)


def usr_sign_quit():
    window.destroy()


bt_in = tk.Button(window, text='登录', command=usr_in)
bt_in.place(x=140, y=230)
bt_up = tk.Button(window, text='注册', command=usr_up)
bt_up.place(x=210, y=230)
bt_quit = tk.Button(window, text='退出', command=usr_sign_quit)
bt_quit.place(x=280, y=230)
window.mainloop()
