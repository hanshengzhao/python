#!/usr/bin/env python
# coding=utf-8

'''
所使用的文件格式是
110000  北京市  0
代号	名称	上级代号

'''


# 判断输入的是否是exit或者quit 
def if_quit(cmd_str):
	if cmd_str == "quit" or cmd_str == "exit":
		print "感谢您的使用"
		return quit 

# 列出所有的省
def list_all_province():
	with open("/home/hansz/python/day_01/pcd_dic/province.txt",'r')as f1:
		content = f1.readlines()
		print "代号		名称"
		for i in content:		
			print "%s		%s" %(i.split()[0],i.split()[1])
		return content

#输入要查看的省
def input_province_choice(province_content):
	user_choice_province = raw_input("输入您要查看的省（代码或者名称）：")
	#if_quit(user_choice_province)
	province_result = ""
	for i in province_content:
		if user_choice_province == i.split()[0] or user_choice_province == i.split()[1]:
			province_result = i
			print "您要查看的是 %s" %province_result.split()[1]
			city_content = list_choice_province_city("/home/hansz/python/day_01/pcd_dic/city.txt",province_result.split()[0])
			input_city_choice(city_content)
	if province_result == "":
		print "您输入有误，请重新输入"
		input_province_choice(province_content)


#列出所有市	
def list_choice_province_city(filepath,result_code):
	with open(filepath,'r') as f2:
		city_content = f2.readlines()
		print "包含有以下市："
		for i in city_content:
			if i.split()[2] == result_code:
				print "	%s		 %s" %(i.split()[0],i.split()[1])	
				continue
		return city_content


#输入要选择的市
def input_city_choice(city_content):
	user_choice_city = raw_input("输入您要查看的市（代码或者名称）：")
	#if_quit(user_choice_city)
	city_result = ""
	for i in city_content:
		if user_choice_city == i.split()[0] or user_choice_city == i.split()[1]:
			city_result = i
			print "您要查看的是 %s" %city_result.split()[1]
			list_choice_city_district("/home/hansz/python/day_01/pcd_dic/district.txt",city_result.split()[0])
			break
	if city_result == "":
		print "您输入城市有误请重新输入"
		input_city_choice(city_content)


# 列出选择市的县区
def list_choice_city_district(filepath,result_code):
	with open(filepath,'r') as f:
		content = f.readlines()
		print "包含有以下区县："
		for i in content:
			if i.split()[2] == result_code:
				print "		%s		 %s" %(i.split()[0],i.split()[1])
				continue


print "下面是中国的省份直辖市，输入代号或者省市可查看更多。"
while True:
	a=list_all_province()
	input_province_choice(a)
	quit_or_continue = raw_input("是否要继续查询？yes/no")
	if quit_or_continue == "yes":
		continue
	else:
		print "感谢您的使用"
		break
	

