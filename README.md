python调用c动态库

1.编译c语音动态库   gcc test.c -fPIC -shared -o libtest.so

2.python下载模块ctypes 
ctypes参考文档路径 https://docs.python.org/3.5/library/ctypes.html

实现的调用类型
1.int、float类型的传入和返回
2.字符串的传入和返回
3.类、结构体的传入和返回
4.回调函数的定义和使用方式
