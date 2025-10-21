#include<stdio.h>

void inTamGiacSao(int n)
{
   for (int i=1; i<=n; i++)
   {
      for (int j = i; j<=n; j++) 
      {
         printf(" ");
      }
      for (int k = 1; k<=(2*i-1); k++) 
      {
         printf("*");
      }
      printf("\n");
   }
}

int main()
{
   int n;
   printf("Nhapp n: "); scanf("%d", &n);
   inTamGiacSao(n);
   return 0;
}
