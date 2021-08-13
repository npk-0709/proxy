import requests
url='https://proxylist.geonode.com/api/proxy-list?limit=50&page=1&sort_by=lastChecked&sort_type=desc&filterUpTime=100&speed=fast&protocols=https&anonymityLevel=elite'
key='b8d95839abdd43dd779e29886ad95932'
json=requests.get(url=url).json()
data=list()
for i in range(len(json["data"])):
    arr=(json["data"][i]["ip"],json["data"][i]["port"])
    data.append(":".join(arr))
for list in data:
    proxy={
        "http":"http://"+list,
        "https":"https://"+list
    }
    try:
        IP=requests.get('http://api.whatismyip.com/ip.php?key='+key,proxies=proxy).text
        data=requests.get("http://api.whatismyip.com/ip-address-lookup.php?key="+key+"&input="+IP).text
    except requests.exceptions.ProxyError as e:
        data=False
    with open("data.txt","a") as fi:
        fi.write(str(data))
