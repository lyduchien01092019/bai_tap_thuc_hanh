#include<stdio.h>

void inTamGiacSo(int n)
{
   for (int i=1; i<=n; i++){
      for (int j=1; j<=i; j++)
         printf("%d ",j);
      printf("\n");
   }
}

int main()
{
   int n;
   printf("Nhap n: "); scanf("%d",&n);
   inTamGiacSo(n);
   return 0;
}
