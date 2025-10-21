#include<stdio.h>

float tinhDtb(float van, float toan, float anh)
{
   return (van*2 + toan*2 +anh)/5;
}
float xepLoaiHocLuc(float dtb)
{
   
   if(dtb<3)
      printf("Yeu\n");
   else if(dtb<5)
      printf("Trung binh\n");
   else if(dtb<7.9)
      printf("Kha\n");
   else
      printf("Gioi\n");
}

int main()
{
   float van, toan, anh;
   printf("Nhap diem van, toan, anh: "); scanf("%f%f%f",&van, &toan, &anh);
   float dtb = tinhDtb(van,toan,anh);
   printf("Dien trung binh La: %.2f, Hoc luc: ",dtb);
   xepLoaiHocLuc(dtb);
   return 0;
}
