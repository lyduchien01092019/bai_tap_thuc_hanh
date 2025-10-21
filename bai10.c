#include<stdio.h>

void fibonacci(int n)
{
   int a=0, b=1, c;
   while (a<n)
   {
      printf("%d", a);
      c=a+b;
      a=b;
      b=c;
   }
   printf("\n");
}

int main()
{
   int n;
   printf("Nhap n: "); scanf("%d", &n);
   fibonacci(n);
   return 0;
}
