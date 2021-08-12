import requests
key='b8d95839abdd43dd779e29886ad95932'
proxy=[{
"http":"http://27.72.149.205:8080",
   "https":"https://27.72.149.205:8080"
},{
    "http":"http://140.227.69.170:6000",
    "https":"https://140.227.69.170:6000"
}
][1]
ck='sb=Vma2X7D6JF_aBy6ESWdwm-OL; datr=Vma2X2YjSxJ-JzCD368WGfmL; wd=1366x657; _fbp=fb.1.1628083018284.1868881933; c_user=100029745455196; dpr=0.8999999761581421; spin=r.1004238106_b.trunk_t.1628736860_s.1_v.2_; xs=11:9-r-EW2k485iGg:2:1628517108:-1:6265::AcWeQhUlcmljtMnh-iXebGjO_gN9GFuwFUckmWXrjOI; fr=1wY3KwcB3YKnaswMn.AWUwnACHDLOEMKZbztcgELEHdto.BhFPbE.53.AAA.0.0.BhFPbE.AWUEiDL64Xs'
respondse=requests.get("https://mbasic.facebook.com/", proxies=proxy,headers={'cookie':ck})
try:
    IP=requests.get('http://api.whatismyip.com/ip.php?key='+key,proxies=proxy).text
    data=requests.get("http://api.whatismyip.com/ip-address-lookup.php?key="+key+"&input="+IP).text
except requests.exceptions.ProxyError as e:
    data=e
with open("data.txt","w+") as fi:
    fi.write(str(data))

