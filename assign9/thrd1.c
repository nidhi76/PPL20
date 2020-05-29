#include<pthread.h>
#include<stdlib.h>
#include<stdio.h>
#include <unistd.h>



void* threadfunction(void *args)
{
	int i;
	while(1)
	{
		printf("Hello world \n");
		sleep(1);
	}
}

void* threadfunction2(void *args)
{

	while(1)
	{
		printf("Goodbye world \n");
		sleep(1);
	}


}
int main()
{
	pthread_t newthread;
	pthread_t newthread2;
	int ret,ret2;

	ret=pthread_create(&newthread,NULL,threadfunction,NULL);
	ret2=pthread_create(&newthread,NULL,threadfunction2,NULL);

	if(ret==0 && ret2==0)
		printf("Created succesfuly\n");
	else
		printf("Not created \n");

	pthread_join(newthread,NULL);
	pthread_join(newthread2,NULL);
	return 0;
}




