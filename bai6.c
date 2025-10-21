#include<stdio.h>

void bangCuuChuong(int n)
{
   for (int i=1; i<=9; i++)
      printf("%d x %d = %d\n", n, i, n*i);
}

int main()
{
   int n;
   printf("Nhap so chuong: "); scanf("%d",&n);
   bangCuuChuong(n);
   return 0;
}
