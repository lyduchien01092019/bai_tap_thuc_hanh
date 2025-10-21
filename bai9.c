#include<stdio.h>

void nhapDungDenN(int n)
{
   int so;
   for (int i =1; i<= n; i++)
   {
      printf("Nhap so thu %d: ",i);
      scanf("%d", &so);
      if (so != i)
      {
         printf("Sai roi! Nhap lai tu dau!\n");
         i=0;
      }
   }
   printf("Banj da nhap dung!\n");
}

int main()
{
   int n;
   printf("Nhap n: "); scanf("%d", &n);
   nhapDungDenN(n);
   return 0;
}
