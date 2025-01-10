import os,uuid,random,re,time
import requests,json

def sxr_main():
    os.system("clear")
    print("\033[1;37m")
    uid = "0m19gy9egx@gonetor.com"
    pww = "0m19gy9egx@gonetor#"
    amazon = ("E6653","E6633","E6853","E6833","F3111","F3111 F3113","F5122","F3111 F3113","SO-04H","F3212","F3311","F8331","SO-02J","G3116","G8232")
    ua = "Mozilla/5.0 (Linux; Android "+str(random.randint(4,13))+"; "+str(random.choice(amazon))+"; Windows 10 Mobile) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/"+str(random.randint(84,106))+".0."+str(random.randint(4200,4900))+"."+str(random.randint(40,140))+" Mobile Safari/537.36"
    check(uid,pww,ua)

oks=[]
cps=[]
def check(uid,pww,ua):
    try:
        session = requests.Session()
        git_fb = session.get("https://touch.facebook.com/pages/create/?ref_type=registration_form").text
        _data = {
            'lsd': re.search(r'"lsd":"(.*?)"', str(git_fb)).group(1),
            'email': uid,
            'encpass': '#PWD_BROWSER:0:'+str(int(time.time()))+':'+pww}
        _header = {'authority': 'touch.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'en-GB,en-US;q=0.9,en;q=0.8','cache-control': 'max-age=0','content-type': 'application/x-www-form-urlencoded','dpr': '1.8937500715255737','origin': 'https://touch.facebook.com','referer': 'https://touch.facebook.com/','sec-ch-prefers-color-scheme': 'dark','sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"','sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"','sec-ch-ua-mobile': '?1','sec-ch-ua-model': '""','sec-ch-ua-platform': '"Android"','sec-ch-ua-platform-version': '""','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': ua,'viewport-width': '980'}
        url = 'https://touch.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=110'
        sxr_respns = session.post(url,data=_data, headers=_header,allow_redirects=False).text
        login_coki=session.cookies.get_dict().keys()
        print(login_coki)
        print('\033[1;92m══════════════════════════════════════════════════')
        if "c_user" in login_coki:
            print(" Login Done")
            coki = ";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
            print(coki)
        else:
            print(f'\n login failed')
    except Exception as e:print(e)

sxr_main()
