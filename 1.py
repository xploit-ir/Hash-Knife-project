#!/usr/bin/env python
import os,sys
import hashlib
import subprocess
import platform
from time import sleep
from sys import exit

def main():  
    print " __    __       ___           _______. __    __      __  ___ .__   __.  __   _______  _______ "
    print "|  |  |  |     /   \         /       ||  |  |  |    |  |/  / |  \ |  | |  | |   ____||   ____|"
    print "|  |__|  |    /  ^  \       |   (----\|  |__|  |    |  '  /  |   \|  | |  | |  |__   |  |__   "
    print "|   __   |   /  /_\  \       \   \    |   __   |    |    <   |  . \` | |  | |   __|  |   __|  "
    print "|  |  |  |  /  _____  \  .----)   |   |  |  |  |    |  .  \  |  |\   | |  | |  |     |  |____ "
    print "|__|  |__| /__/     \__\ |_______/    |__|  |__|    |__|\__\ |__| \__| |__| |__|     |_______|"
    print "                                                                                              "
    print "=============================================================================================="
    print "                           In The Name Of World Programmer                                    "
    print "                                 Programmer : V30sharp                                        "
    print "Special Tnx : oxoptimous - sk0te_vahshat - ARTA - e2ma3n - mars - ArYaIeIrAn - Mr.Xhat        " 
    print"\t"
    print"\t"
    print"\t"
    print"\t"




    print " Your Option'ns  :\t"
    print " \t    1-Create Md5 Hash From Pass list\n\
            2-Create hash With this Algoritm md5(md5(password).salt))\n\
            3-Compare To find Password with reverse engineering \n\
            4-Find PassWord For Your Hash\n\
            q-Exit"

    print ""
    inputs=raw_input("Select One Option : ")
    try:
        
        if inputs == "1":
            print "[+]Your choice is : MD5 Hash Creator..."
            CreatHashMd5()
            wait()
        elif inputs == "2":
            clear()
            print "[+]Your choice is : Join Hash and Salt..."
            CreateHashWithSaltMd5()
            wait()
        elif inputs == "3":
            clear()
            print "[+]Your choice is : Compare Created Hash with Target Hash's... "
            compare()
            wait()
        elif inputs == "4":
            clear()
            print "[+]Your choice is : Find PassWord... "
            FindPassword()
            
       
    except:
        print "[+]Ops! Your Choice Not Found ! Try Again ;)"
        
            
    
def CreatHashMd5():
    
    
    Hfile=open('data/hash.txt',"w")
    print "[+] Opration Started For Create MD5 Hash..."+"\n"
    with open('data/pass.txt') as Ofile:
        for linePass in Ofile:
            Hpass=hashlib.md5(linePass.rstrip()).hexdigest()
            print "[-] Password is "+linePass+" and Hash For This Password :"+Hpass
            Hfile.write(Hpass+"\n")
        
        print "[+] All Hash Writed...!"
        Hfile.close()

        

def CreateHashWithSaltMd5():
    Tfile=open('data/tmp.txt',"w")
    Hfile=open('data/hWs.txt',"a")
    print "[+] Opration Started For join MD5 Hash With Salt..."+"\n"
    salt=raw_input("Enter Salt :")
    with open('data/hash.txt') as Ofile:
        for hashs in Ofile:
            sWh=hashlib.md5(hashs.rstrip()+salt).hexdigest()
            print "[-] passWd Md5 is "+hashs+" and join Hash with salt is :"+sWh
            Tfile.write("MD5 Is ->  "+hashs+"  "+"Salt is ->  "+salt+"  "+"Join is->  "+sWh+"\n")
            Hfile.write(sWh+"\n")
            
            
        print "[+] All md5(md5(password).salt) algorithm, Hash Saved in hWs.txt file"
        Hfile.close()
            
            
def compare():
    print "[+] Opration Started For Compare..."+"\n"
    target=open("data/target.txt").readlines()
    for i in target:
        hWs=open("data/hWs.txt").readlines()
        sleep(3)
        for j in hWs:
            if i==j:
                print "[+] Target Hash ["+i+"] Equal with One Of Your Hash list ["+j+"]"
                sleep(3)
            else:
                print "[-] Sorry Not Found :("


def FindPassword():
    
    inputs2=raw_input("Enter Your Md5 Hash  in tmp.txt file afther join with salt:")
    with open('data/pass.txt') as passWd:
        for i in passWd:
            Chash=hashlib.md5(i.rstrip()).hexdigest()
            if Chash==inputs2:
                print "[**]Your PassWord For Enter'ed hash is -> "+i
                
            else:
                print "[-]NotFound Sorry :("


                
def clear():
    subprocess.Popen( "cls" if platform.system() == "Windows" else "clear", shell=True)
def wait():
    
    inp=raw_input("\tFor Back The Main Menu press b :")
    if inp.lower()=="b":
        clear()
        main()
		
    else:
        print "input not correct ! Auto Back to main"
        mian()


if __name__ =='__main__':
    main()

        





