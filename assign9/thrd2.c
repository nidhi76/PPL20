#include<stdio.h> 
#include<time.h>  
#include<stdlib.h>     
#include<unistd.h>
#include<pthread.h>
void* threadfunction(void *args)
{
    
    time_t rawtime = time(NULL);
    
    if (rawtime == -1) {
        
        puts("The time() function failed");
      //  return 1;
    }
    
    struct tm *ptm = localtime(&rawtime);
    
    if (ptm == NULL) {
        
        puts("The localtime() function failed");
    //    return 1;
    }
    
    printf(" %d:", ptm->tm_hour);

    
}

void* threadfunction2(void *args)
{
    
    time_t rawtime2 = time(NULL);
    
    if (rawtime2 == -1) {
        
        puts("The time() function failed");
        
    }
    
    struct tm *ptm2 = localtime(&rawtime2);
    
    if (ptm2 == NULL) {
        
        puts("The localtime() function failed");
        
    }
    
    printf(" %d:", ptm2->tm_min);

    
}

void* threadfunction3(void *args)
{
    
    time_t rawtime3 = time(NULL);
    
    if (rawtime3 == -1) {
        
        puts("The time() function failed");
       
    }
    
    struct tm *ptm3 = localtime(&rawtime3);
    
    if (ptm3 == NULL) {
        
        puts("The localtime() function failed");
       
    }
    
    printf("%02d", ptm3->tm_sec);

    
}


int  main()
{

	pthread_t newthread;// thread for hour
	pthread_t newthread2;// thread for min
	pthread_t newthread3;// thread for sec


	int ret,ret2,ret3;

	ret=pthread_create(&newthread,NULL,threadfunction,NULL);
	ret2=pthread_create(&newthread2,NULL,threadfunction2,NULL);
        ret3=pthread_create(&newthread3,NULL,threadfunction3,NULL);


	if(ret==0 && ret2==0 && ret3==0)
		printf("Created succesfully\n");// all the threads are present
	else
		printf("Not created \n");

	pthread_join(newthread,NULL);
	pthread_join(newthread2,NULL);
	pthread_join(newthread3,NULL);

	return 0;

}




 
	
