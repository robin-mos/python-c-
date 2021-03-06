#include "test.h"


//加法
int add(int a, int b){
	printf("func:%s a = %d,b = %d\n",__FUNCTION__, a,b);
	return (a+b);
}


float addFloat(int a, float b){
	printf("func:%s\n a = %d, b = %f \n", __FUNCTION__, a, b);
	return ((float)a+b);
}


//返回字符串
char * getVersion(void){
	printf("func:%s return string to python\n",__FUNCTION__);
	return "c version 1.0";
}


char * setVersion(char* version){
	printf("func:%s set version:%s\n",__FUNCTION__, version);
	return "set success!!";
}


Person getPerson(){
	Person person;
	strcpy(person.name,"robin");
	person.age = 20;
	return person;
}


int setPerson(Person person){
	printf("%s\n", person.name);
	printf("%d\n", person.age);
	return 0;
}


// 回调函数
int getAge(int(*callback)(int), int a){
	if(callback == NULL){
		return -1;
	}

	int age = 0;
	age = callback(a);
	printf("age : %d\n", age);
	if(age <= 0){
		return -2;
	}
	return 0;
}


//设置数组
void setIntArray(int array[], int len){
	int i = 0;

	for(i = 0; i < len;i++){
		printf("%d\n", array[i]);
	}
}

