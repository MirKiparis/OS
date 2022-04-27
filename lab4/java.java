
/********************Computes an optimized version of this code:
;;;
;;;   int a=0, b=3, c=3
;;;   for ( int i=0; i<noIterations; i++ )
;;;            a += b*2 + c - i;
**************/
public class Main
{
	public static void main(String[] args) {
		int a = 0;
        int b = 3;
        int c = 3;
        long noIterations = 100000000;
        long time = System.currentTimeMillis();
        for ( int i=0; i<noIterations; i++ )
            a += b*2 + c - i;
        System.out.println(System.currentTimeMillis() - time + " ms");
	}
}

