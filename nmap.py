import subprocess,re,json

with open("ip_port.json","r") as f:
    a=f.read()

b=json.loads(a)

for i in b.keys():
    ip=i
    ports=""
    for j in b[i]:
        ports+=j+","
    if ports !="":
        try:
            a=subprocess.run(["nmap","--script=vuln","-sC","-sV","-p"+ports[0:-1],ip])
            print(a)
        except:
            pass