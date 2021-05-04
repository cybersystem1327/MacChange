import pyfiglet
import os
ascii_banner = pyfiglet.figlet_format("MAC CHANGE ")
print(ascii_banner)
print("Version 1.0 ")

x = int(input("\nMerhaba \n\nMac Adrresi Değiştirmek İçin 1'e Basın \nEski Mac addresiniz için 2' ye Basın  :"))
if x == 1 :
    os.system("ifconfig wlan0 down")
    os.system("macchanger -r wlan0")
    os.system("ifconfig wlan0 up")
    print("Mac Adresiniz Değiştirildi")
elif x == 2 :
    os.system("ifconfig wlan0 down")
    os.system("macchanger -p wlan0")
    os.system("ifconfig wlan0 up")
    print("Mac Adresiniz Eski Haline Getirildi")
else :
    print("yanlış komut girdiniz")
