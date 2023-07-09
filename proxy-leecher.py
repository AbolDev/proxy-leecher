import requests, time, os, sys
from colorama import Fore


t_id = "@IranCrackersTeam" # Enter your Telegram channel ID here.


def remove_empty_lines(text):
    out = ''
    for i in text.splitlines():
        if i:
            out += i + '\n'
    return out


def get_proxy(type_):
    try:
        response = requests.get(f"https://api.voidevs.com/v1/proxy-list?protocol={type_}").text
        response = remove_empty_lines(response)
        return response
    except:
        return False


os.system("title PROXY Leecher By @ABOL_CRACKER")
os.system("cls")


print(Fore.RED+"""

██████╗░██████╗░░█████╗░██╗░░██╗██╗░░░██╗  ██╗░░░░░███████╗███████╗░█████╗░██╗░░██╗███████╗██████╗░
██╔══██╗██╔══██╗██╔══██╗╚██╗██╔╝╚██╗░██╔╝  ██║░░░░░██╔════╝██╔════╝██╔══██╗██║░░██║██╔════╝██╔══██╗
██████╔╝██████╔╝██║░░██║░╚███╔╝░░╚████╔╝░  ██║░░░░░█████╗░░█████╗░░██║░░╚═╝███████║█████╗░░██████╔╝
██╔═══╝░██╔══██╗██║░░██║░██╔██╗░░░╚██╔╝░░  ██║░░░░░██╔══╝░░██╔══╝░░██║░░██╗██╔══██║██╔══╝░░██╔══██╗
██║░░░░░██║░░██║╚█████╔╝██╔╝╚██╗░░░██║░░░  ███████╗███████╗███████╗╚█████╔╝██║░░██║███████╗██║░░██║
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░  ╚══════╝╚══════╝╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝""",Fore.YELLOW + '''

  By @ABOL_CRACKER
''')

time.sleep(0.5)


print("  1 => http")
print("  2 => socks4")
print("  3 => socks5")
print("  4 => all")
print()
aaa = input(Fore.CYAN + "  Enter Your Proxy Type => ")
print()

if aaa == "1":
    type_ = "http"
    print("  Your Proxy Type: http")
elif aaa == "2":
    type_ = "socks4"
    print("  Your Proxy Type: socks4")
elif aaa == "3":
    type_ = "socks5"
    print("  Your Proxy Type: socks5")
elif aaa == "4":
    type_ = "http & socks4 & socks5"
    print("  Your Proxy Type: http & socks4 & socks5")
else:
    sys.exit()


filename = f'{type_}-Proxy.txt'

proxy = get_proxy(type_)

if proxy:
    file = open(filename, 'a+', encoding="utf-8")
    file.write(proxy)
    file.close()
    print()
    print(Fore.GREEN + "  The proxy was successfully leeched")
    print()
    print("  Proxies Saved File name: " + filename)
    print()
    print("  This software will close in 10 seconds")
    print()
    print(Fore.LIGHTRED_EX + f'  Join In My Telegram Cannel => {t_id}')
    time.sleep(10)
    sys.exit()
else:
    print()
    print(Fore.RED + "  Error Connection To The Server")
    print()
    print(Fore.GREEN + "  Please Check Your Computer Internet Connection")
    print()
    print(Fore.YELLOW + f"  Join In My Telegram Cannel => {t_id}")
    print()
    print("  This software will close in 10 seconds")
    print()
    time.sleep(10)
    sys.exit()


