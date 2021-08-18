import requests,json
url='https://proxylist.geonode.com/api/proxy-list?limit=50&page=1&sort_by=lastChecked&sort_type=desc&filterUpTime=100&speed=fast&protocols=http%2Chttps&anonymityLevel=elite'
url='https://proxylist.geonode.com/api/proxy-list?limit=50&page=1&sort_by=lastChecked&sort_type=desc&speed=fast&protocols=https&anonymityLevel=elite'
key='b8d95839abdd43dd779e29886ad95932'
json_=requests.get(url=url).json()
data=list()
proxy_list=list()
for i in range(len(json_["data"])):
    with open("data.txt","w") as fi:
        arr=(json_["data"][i]["ip"],json_["data"][i]["port"])
        s=":".join(arr)
        proxy={"http":"http://"+s,"https":"https://"+s}
        try:
            data=requests.get("http://api.whatismyip.com/ip-address-lookup.php?key="+key+"&input="+
                requests.get('http://api.whatismyip.com/ip.php?key='+key,proxies=proxy).text).text
            list=proxy_list.append({
                    "IP":json_["data"][i]["ip"],
                    "PORT":json_["data"][i]["port"]
                    })
            json.dump(list,fi)
        except:
            data="False"
