import requests
import os
banner="""
    


                                                                             _____         _       __  _             _             
     /\                                                                     / ____|       | |     / _|(_)           | |            
    /  \    _ __    ___   _ __   _   _  _ __    ___   _ __  _ __ ___   ___ | (___   _   _ | |__  | |_  _  _ __    __| |  ___  _ __ 
   / /\ \  | '_ \  / _ \ | '_ \ | | | || '_ \  / _ \ | '__|| '_ ` _ \ / __| \___ \ | | | || '_ \ |  _|| || '_ \  / _` | / _ \| '__|
  / ____ \ | | | || (_) || | | || |_| || | | || (_) || |   | | | | | |\__ \ ____) || |_| || |_) || |  | || | | || (_| ||  __/| |   
 /_/    \_\|_| |_| \___/ |_| |_| \__, ||_| |_| \___/ |_|   |_| |_| |_||___/|_____/  \__,_||_.__/ |_|  |_||_| |_| \__,_| \___||_|   
                                  __/ |                                                                                            
                                 |___/                                                                                             

                                           subfinder V1.0
                                           Anonynorms

"""
print(banner)
def request(url):
    try:
        return requests.get("https://" + url, timeout=2)
        
    except requests.exceptions.ConnectionError:
        pass

target_url= input("\tEnter Your Testing  Url--->\t")
location = input("\tEnter Your Wordlist Location \t")
isExist = os.path.exists(location)
print("\tLOCATION EXIST:---", isExist)
try:
    with open(location,"r") as wordlist_file:
        print("\t\t\t\t\t\t\t\t\t\tTrying  to find hidden subdomain.")
        for line in wordlist_file:
            word = line.strip()
            test_url = word + "." + target_url
            response = request(test_url)
            if response:
                print("[+] DISCOVERED SUBDOMAIN --------->"  + test_url)
                
            else:
                print("[-] NOT SUBDOMAIN --------->"  + test_url)
            
       
         
except:
    exit()
       