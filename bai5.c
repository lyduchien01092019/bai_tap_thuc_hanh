#include<stdio.h>

long tinhTienDien(int soDien)
{
   long tien = 0;
   if(soDien <= 100)
      tien = soDien * 500;
   else if (soDien <= 350)
      tien = 100*500 + (soDien - 100) *550;
   else if (soDien<=650)
      tien = 100*500 + 250*550 + (soDien - 350) * 650;
   else
      tien = 100*500 + 250*550 + 300*650 + (soDien -650) *800;
   return tien;
}

int main()
{
   int soDien;
   printf("Nhap so dien: "); scanf("%d",&soDien);
   printf("So tien phai tra laf: %ld", tinhTienDien(soDien));
   return 0;
}
