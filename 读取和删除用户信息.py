import pickle
with open('./usr_info.pickle', 'rb') as usr_file:
    usr_info = pickle.load(usr_file)
print(usr_info)
usr = input('请输入需要删除的用户')
usr_info.pop(usr)
with open('usr_info.pickle', 'wb') as usr_files:
    usrs_info = usr_info
    usr_info = pickle.dump(usrs_info, usr_files)
print('已经成功删除', usr)
print('还剩下', usrs_info)
