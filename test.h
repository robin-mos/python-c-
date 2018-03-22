#include <stdio.h>
#include <string.h>

/**
@license: LiXiangping
@author: LiXiangping
@description: python调用c动态库
@date: 2018/03/21
 */

// 人物描述
typedef struct Person{
	char name[10];
	int age;
}Person;

int add(int a, int b);

float addFloat(int a, float b);

char * getVersion(void);

char * setVersion(char* version);

Person getPerson();

int setPerson(Person person);

int getAge(int(*callback)(int), int);

void setIntArray(int array[], int);
