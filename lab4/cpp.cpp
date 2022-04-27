#include <stdio.h>
#include <stdlib.h>
#include <time.h>
 
int main()
{
    clock_t start, end;
    int a = 0;
    int b = 3;
    int c = 3;
    long noIterations = 100000000;
    start = clock();
    for ( int i=0; i<noIterations; i++ )
            a += b*2 + c - i;
    end = clock();
    printf(" %.4f ms\n", ((double) end - start) / ((double) CLOCKS_PER_SEC)*1000);
    return 0;
}
