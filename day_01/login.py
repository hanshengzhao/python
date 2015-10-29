#!/usr/bin/env python
# _*_ coding:utf-8 _*_

'''
login program
if your faild 3th,your will be locked

输入用户名密码
认证成功后显示欢迎信息
输错三次后锁定


用户输入一次密码就写入到日志中去。记录成功或者失败状态。
每次登陆的时候先去看.user_lock文件，然后再看login.log 文件
如果login.log文件里在三分钟内登陆一直失败过，那么会算上次数。



.user_lock 文件的格式
hansz	2015-10-27 21:31:26.159738

'''
import getpass,datetime,time,os

# minutes
global error_time 
error_time=3
global count 
count = 3
def login_succeed(user_name):
	print "欢迎您，尊敬的 %s" %user_name
	now_time=str(datetime.datetime.now())
	with open("session.log","a") as f:
		login_info = "%s	login succeed in	%s \n" %(user_name ,now_time.split(".")[0])
		f.write(login_info)

def login_failed(user_name,count):
	count =count -1
	if count > 0:
		print "(密码输入错误，您还有%d次机会)" %count
		user_passwd = getpass.getpass("请输入密码：") 
		if_passwd_ok(user_name,user_passwd,count)
	else:
		print "错误次数超过三次，已锁定账号"
		os.system("sed -i '/%s/d' .user_lock" %user_name)
		lock_time=str(datetime.datetime.now())
		with open(".user_lock","a")as f:
			lock_info="%s %s\n" %(user_name,lock_time.split(".")[0])
			f.write(lock_info)
		with open("session.log","a")as f:
			faild_info = "%s	are locked in	%s \n " %(user_name,lock_time.split(".")[0])
			f.write(faild_info)





def user_lock(user_name,login_time):
	with open(".user_lock","a") as f:
		lock_user="%s/n" %user_name
		f.write(lock_user)

# 把字符串格式的时间转换为datetime格式
def str_to_date(str_date):
	date_date = datetime.datetime.fromtimestamp(time.mktime(time.strptime(str_date,"%Y-%m-%d %H:%M:%S")))
	return date_date

# 时间超过error_time之后 返回true
def date_compare(str_date_old,str_date_new):
	print "您现在登陆的时间是%s" %str_date_new
	date_date_new = str_to_date(str_date_new)
	date_date_old = str_to_date(str_date_old)
	diff = (date_date_new - date_date_old)
	diff_str = str(diff)
	#print "这个是时间差",int(diff_str.split(":")[0]),int(diff_str.split(":")[1])
	if int(diff_str.split(":")[0]) == 0:
		if int(diff_str.split(":")[1]) >= error_time:
			return True
		else:
			return False
	elif int(diff_str.split(":")[0]) > 0:
		return True
	else:
		return False

# 判断密码是否正确

def if_passwd_ok(user_name,user_passwd,count):
	if count >0:
		# 从用户列表里面读取用户名和密码
		status0 = 0 
		with open("user.list",'r')as f:
			for i in f.readlines():
				# 如果用户名密码正确
				if i.split()[1] == user_name:
					if i.split()[2] == user_passwd:
						login_succeed(user_name)
						status0 = 1
						break 
					else:
						login_failed(user_name,count)
						status0 = 1
						break
			if status0 == 0:
				print "没有这个用户"
	else:
		print "账号被锁定啦。"
# 从登陆日志查看是否近三分钟登陆过且登陆失败了

#判断是否被锁定
def if_lock(user_name,user_passwd,login_time):
	#读取.user_lock 文件
	status1 = 0
	with open(".user_lock",'r') as f:
		content = f.readlines() 
		if content == []:
			if_passwd_ok(user_name,user_passwd,count)
		else:
			for i in content:
				# 如果用户名存在在列表当中
				if i.split()[0] == user_name :
					# 查看写入lock文件时的时间，如果超过三分钟就把他删除，如果没有超过三分钟，就拒绝登陆
					date_old = "%s %s" %(i.split()[1],i.split()[2])
					if date_compare(date_old,login_time):
						if_passwd_ok(user_name,user_passwd,count)
						# 删除用户。用linux下的sed
						os.system("sed -i '/%s/d' .user_lock"% user_name)

						status1 = 1
						break
						#删除用户
					else:
						print  "您在三分钟之内登录三次错误，已被锁定，请稍后再试。"
						status1 = 1 
						break
				else:
					continue
			if status1 == 0:
				if_passwd_ok(user_name,user_passwd,count)

#datetime.datetime.fromtimestamp(time.mktime(time.strptime(stringDate,"%Y-%m-%d %H:%M:%S")))





print "欢迎登陆系统".center(100)
user_name = raw_input("请输入用户名：")
user_passwd = getpass.getpass("请输入密码：") 
d1 = datetime.datetime.now()
login_time = str(d1).split(".")[0]
if_lock(user_name,user_passwd,login_time)