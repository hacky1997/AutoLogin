import pyfiglet
# import sys, os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from getpass import getpass


# is_windows = sys.platform.startswith('win')

# if is_windows:
#     # Windows deserves coloring too :D
#     G = '\033[92m'  # green
#     Y = '\033[93m'  # yellow
#     B = '\033[94m'  # blue
#     R = '\033[91m'  # red
#     W = '\033[0m'   # white
#     try:
#         import win_unicode_console , colorama
#         win_unicode_console.enable()
#         colorama.init()
#         #Now the unicode will work ^_^
#     except:
#         print("[!] Error: Coloring libraries not installed, no coloring will be used [Check the readme]")
#         G = Y = B = R = W = G = Y = B = R = W = ''
# else:
#     G = '\033[92m'  # green
#     Y = '\033[93m'  # yellow
#     B = '\033[94m'  # blue
#     R = '\033[91m'  # red
#     W = '\033[0m'   # white


# print("""%s
#                 ^         _        _                _
#                / \  _   _| |_ ___ | |    ___   __ _(_)_ __
#               / _ \| | | | __/ _ \| |   / _ \ / _` | | '_  \

#              / ___ \ |_| | || (_) | |__| (_) | (_| | | | | |
#             /_/   \_\__,_|\__\___/|_____\___/ \__, |_|_| |_|
#                                             | |__| |    
#                                              \____/        %s%s

#                             ~~~~~ Coded By Sayak Naskar ~~~~~
# """ % (R, W, Y))


# # def parser_error(errmsg):
# #     banner()
# #     print("Usage: python ")
# #     print(R + "Error: " + errmsg + W)
# #     sys.exit()

pyfiglet.print_figlet("                               AutoLogin")
print ("                                ~~~~~~~~~~ Created by Sayak Naskar ~~~~~~~~~~\n\n")

print ("Which one you want to login :   "+"1. Facebook.\n\t\t\t\t2. Gmail.\n\t\t\t\t3. Github.\n\t\t\t\t4. Twitter.\n\t\t\t\t5. Yahoo.\n\t\t\t\t6. Linkedin.\n\t\t\t\t7. Microsoft.\n\t\t\t\t8. Instagram.")
url = int(input("Enter your choice : "))

# # print("Choose your browser : \t"+"a. Chrome\tb. firefox\n")
# # drive = input("Choose your browser : ")

# # if drive == a :
# #     browser = webdriver.Chrome("")
# # elif drive == b:
# #     browser = webdriver.firefox("")

if url == 1:
    # def Facebook(uname,pwrd):
    uname = input("user name : ")
    pwrd = getpass("password  : ")


    browser = webdriver.Chrome("set the path where you have download your driver")
    url = "https://www.facebook.com"
    browser.get(str(url))

    elem1 = browser.find_element_by_id("email")
    elem1.send_keys(uname)

    elem2 = browser.find_element_by_name("pass")
    elem2.send_keys(pwrd)

    browser.find_element_by_id('loginbutton').click()

    # if __name__ == "__main__":
    #     uname = input("user name : ")
    #     pwrd = getpass("password  : ")
    #     Facebook(uname,pwrd)
    

elif url == 2:
    
    uname = input("user name : ")
    pwrd = getpass("password  : ")

    # def Gmail(uname,pwrd):
    browser = webdriver.Chrome("set the path where you have download your driver")
    url = "https://www.gmail.com"
    browser.get(str(url))

    emailid = browser.find_element_by_id("identifierId")
    emailid.send_keys(uname)
    browser.find_element_by_xpath("//*[@id='identifierNext']/content/span").click()

    browser.implicitly_wait(1)

    passw = browser.find_element_by_name("password")
    passw.send_keys(pwrd)
    browser.find_element_by_xpath("//*[@id='passwordNext']/content/span").click()

    # if __name__ == "__main__":
    #     uname = input("user name : ")
    #     pwrd = getpass("password  : ")
    #     Gmail(uname,pwrd)

elif url == 3:
    uname = input("user name : ")
    pwrd = getpass("password  : ")

    browser = webdriver.Chrome("set the path where you have download your driver")
    url = "https://github.com/login?return_to=%2Fjoin%3Fsource%3Dheader-home"
    browser.get(str(url))

    emailid = browser.find_element_by_id("login_field")
    emailid.send_keys(uname)

    passw = browser.find_element_by_id("password")
    passw.send_keys(pwrd)
    browser.find_element_by_name('commit').click()


elif url == 4:
    uname = input("user name : ")
    pwrd = getpass("password  : ")

    browser = webdriver.Chrome("set the path where you have download your driver")
    url = "https://twitter.com/login?lang=en"
    browser.get(str(url))

    emailid = browser.find_element_by_class_name("js-username-field")
    emailid.send_keys(uname)
    browser.implicitly_wait(1)

    passw = browser.find_element_by_class_name("js-password-field")
    passw.send_keys(pwrd)
    browser.implicitly_wait(1)
    browser.find_element_by_class_name("EdgeButtom--medium").click()


elif url == 5:
    uname = input("user name : ")
    pwrd = getpass("password  : ")

    browser = webdriver.Chrome("set the path where you have download your driver")
    url = "https://login.yahoo.com/?.src=ym&.partner=none&.lang=en-IN&.intl=in&.done=https%3A%2F%2Fmail.yahoo.com%2Fd%3F.intl%3Din%26.lang%3Den-IN%26.partner%3Dnone%26.src%3Dfp"
    browser.get(str(url))

    emailid = browser.find_element_by_id("login-username")
    emailid.send_keys(uname)
    browser.find_element_by_id("login-signin").click()

    browser.implicitly_wait(1)

    passw = browser.find_element_by_id("login-passwd")
    passw.send_keys(pwrd)
    browser.find_element_by_id('login-signin').click()

elif url == 6:
    uname = input("user name : ")
    pwrd = getpass("password  : ")

    browser = webdriver.Chrome("set the path where you have download your driver")
    url = "https://in.linkedin.com/"
    browser.get(str(url))

    emailid = browser.find_element_by_id("login-email")
    emailid.send_keys(uname)

    passw = browser.find_element_by_id("login-password")
    passw.send_keys(pwrd)
    browser.find_element_by_id('login-submit').click()

elif url == 7:
    uname = input("user name : ")
    pwrd = getpass("password  : ")

    browser = webdriver.Chrome("set the path where you have download your driver")
    url = "https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1541937569&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3da4f676f3-a503-3fcc-5e32-f5b507c846d2&id=292841&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015"
    browser.get(str(url))

    emailid = browser.find_element_by_id("i0116")
    emailid.send_keys(uname)
    browser.find_element_by_id('idSIButton9').click()

    browser.implicitly_wait(1)

    passw = browser.find_element_by_id("i0118")
    passw.send_keys(pwrd)
    browser.find_element_by_id('idSIButton9').click()
    
elif url == 8:
    uname = input("user name : ")
    pwrd = getpass("password  : ")

    browser = webdriver.Chrome("set the path where you have download your driver")
    url = "https://www.instagram.com/accounts/login/"
    browser.get(str(url))

    browser.implicitly_wait(1).sleep(5)

    emailid = browser.find_element_by_class_name("_2hvTZ pexuQ zyHYP")
    emailid.send_keys(uname)

    passw = browser.find_element_by_class_name("_2hvTZ pexuQ zyHYP")
    passw.send_keys(pwrd)
    browser.find_element_by_class_name("_0mzm- sqdOP  L3NKy       ").click()
    

elif url != 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 :
    print ("[!] Invalid option!\n")
    exit()



                                  
