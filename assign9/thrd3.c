#include<pthread.h>
#include<stdlib.h>
#include<stdio.h>
#include <unistd.h>



void* threadfunction(void *args)
{
	int i;
	while(1)
	{
		printf("Hello \n");
		sleep(1);
	}
}


int main()
{
	pthread_t newthread;
	pthread_t newthread2;
	int ret;

	ret=pthread_create(&newthread,NULL,threadfunction,NULL);
	

	if(ret==0)
		printf("Created succesfuly\n");
	else
		printf("Not created \n");

	pthread_join(newthread,NULL);
	
	return 0;
}




