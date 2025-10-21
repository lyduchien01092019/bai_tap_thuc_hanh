#include<stdio.h>

int namNhuan(int nam)
{ 
   return (( nam % 4 == 0 & nam % 100 != 0 ) ||  nam % 400 == 0 );
}

int main()
{
   int nam;
   printf("Nham nam: "); scanf("%d", &nam);
   
   if(namNhuan)
      printf("%d la nam nhuan\n",nam);
   else 
      printf("%d la nam khong nhuan\n",nam);
      
return 0;
}
