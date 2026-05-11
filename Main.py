from colorama import Fore
from Banner import Banner
from time import sleep
from Encrypted import Encryption
from Decoding import Decoding
import sys
import os
def main():
    os.system("clear")
    Banner.Banner()
    print(Fore.RED+"["+Fore.CYAN+"+"+Fore.RED+"]"+Fore.GREEN+" Instagram:"+Fore.CYAN+"Mr.Hack_313")
    print(Fore.RED+"["+Fore.CYAN+"+"+Fore.RED+"]"+Fore.GREEN+" Telegram:"+Fore.CYAN+"0782034982")
    print()
    print(Fore.RED+"loading packages....")
    sleep(6)
    print()
    
    while True:
        print("  "+Fore.RED+"["+Fore.CYAN+"1"+Fore.GREEN+"]"+" "*10+Fore.CYAN+"《:Password Encryption:》")
        print()
        print("  "+Fore.RED+"["+Fore.CYAN+"2"+Fore.GREEN+"]"+" "*10+Fore.CYAN+"《:Password Decoding:》")
        print()
        print("  "+Fore.RED+"["+Fore.CYAN+"0"+Fore.GREEN+"]"+" "*10+Fore.CYAN+"《: Exit of this script:》")
        try:
            
            select_options = int(input(Fore.GREEN+"Choice a option :"+Fore.RED))
            
            if select_options == 1:
                
                Password = input(Fore.CYAN+"Enter Password:"+Fore.RED)
                hash = Encryption.Encrypt(Password)
                print(Fore.RED+"Waiting for Hashing Password....")
                sleep(3)
                print(Fore.CYAN+"Hash Password :"+Fore.GREEN+hash)
                file = open("Hash_Paswords.txt","w+")
                file.write(f"Hash Password : {hash}\n")
                file.close()
                break
                    
            elif select_options == 2:
                    
                Hashed = input(Fore.GREEN+"Enter Hash Password :"+Fore.RED)
                Hash_crack = Decoding.dic(Hashed)
                if Hash_crack == 1:
                    break
                print(Fore.RED+"Waiting for Cracking Password ....")
                sleep(3)

                print(Fore.CYAN+"Crack Password :"+Fore.GREEN+Hash_crack)
                file2 = open("Crack_Paswords.txt","w+")
                file2.write(f"Hash Password : {Hash_crack}\n")
                file2.close()
                break
            elif select_options == 0:
                print()
                print(Fore.GREEN+"thanks a lot for use this script.")
                break
            elif type(select_options) == str():
                print()
                print(Fore.RED+"Error! \nplease Choice options")
                break
                
            else:
                print()
                print(Fore.RED+"Error! \nplease Choice options")       
                break
                
            
        except:
            #print(" "*6+"Error input!")
            #break
            pass
main()