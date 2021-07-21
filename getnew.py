import sqlite3
import requests,json,subprocess,os


public_prog_url="https://raw.githubusercontent.com/projectdiscovery/public-bugbounty-programs/master/chaos-bugbounty-list.json"


jsondata=requests.get(public_prog_url)
programs_dict=json.loads(jsondata.text)

with open("newdomains.txt","w") as f:
    for i in programs_dict['programs']:
        for j in i['domains']:
            f.write(j+"\n")

os.system("cat newdomains.txt | anew domain.txt")