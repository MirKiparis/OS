#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <time.h>


extern "C" int cicle();


int main()
{
	printf("Hello\n");
	double start, end;
	int t;
	start = clock();
	t = cicle();
	end = clock();
	double seconds = end - start;
	printf("The time: %f ms\n", seconds);
	
	return 0;
}




