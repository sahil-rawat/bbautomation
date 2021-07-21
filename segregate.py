import requests,json,os,subprocess,re

domains=[]
with open("domain.txt","r") as f:
    a=f.read()
    domains=a.split("\n")
    
mail=re.compile(r".*\smail.*")
ip=re.compile(r".*\shas\saddress\s(.*)")
alias=re.compile(r".*\sis\san\salias\sfor\s.*")

with open("alias.txt","w") as aliasf,open("ip.txt","w") as ipf,open("mail.txt","w") as mailf:
    for i in domains:
        try:
            out=subprocess.check_output(["host",i])
        except:
            pass
        dump=out.decode().split("\n")
        for i in dump:
            m=mail.search(i)
            n=ip.search(i)
            o=alias.search(i)
            if(m):
                print(m.group())
                mailf.write(m.group()+"\n")
            if(n):
                print(n.groups()[0])
                ipf.write(n.groups()[0]+"\n")
            if(o):
                print(o.groups())
                aliasf.write(o.group()+"\n")

