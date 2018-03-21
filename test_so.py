# coding=utf-8

'''
@license: LiXiangpinge
@version: 1.0
@release: 1.0
@author: LiXiangping
@description: python调用c动态库
@date: 
'''

import ctypes

testso = ctypes.CDLL('libtest.so')

# int float测试
def int_test():
	print('test:add int:', testso.add(10, 20))
	print(float(20.1))
    # 显示声明参数和期望返回类型
	testso.addFloat.argtypes = [ctypes.c_int, ctypes.c_float]
	testso.addFloat.restype = ctypes.c_float
	print('test add float:', testso.addFloat(10,  20.4))

# 字符串的传入和获取
def str_test():
	# 获取字符串地址
	addr = testso.getVersion()  
	data = ctypes.string_at(addr,-1).decode('utf-8')
	print('python :',data)

	# 传入字符串
	addr = testso.setVersion('version 1.0'.encode())
	data = ctypes.string_at(addr,-1).decode('utf-8')
	print('python :',data)



class Person(ctypes.Structure):
	_fields_ = [('name', ctypes.c_char*10),
			('age', ctypes.c_int)]


# 设置结构体参数
def struct_test():
	func_set_person = testso.setPerson
	func_set_person.restype = ctypes.c_int
	func_set_person.argtypes = [Person]
	person = Person()
	person.age = 20
	person.name = 'robin'.encode()
	testso.setPerson(person)

	func_get_person = testso.getPerson
	func_get_person.restype = Person
	person = testso.getPerson()
	print(person.name)
	print(person.age)




def callback_func(age = 0):
	age += 5
	return age


def callback_test():
	# 定义回调函数类型，设置回调函数参数格式，第一个参数为返回值类型
	typecallback = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)  
	result = testso.getAge(typecallback(callback_func),-1)
	print('回调函数执行:%d'%result)


if __name__ == '__main__':
	int_test()
	str_test()
	struct_test()
	callback_test()
