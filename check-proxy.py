if __name__ == '__main__':
    try:
        from proxy_checker import ProxyChecker
    except:
        import os
        os.system("pip install proxy_checker")
        from proxy_checker import ProxyChecker
    list_proxy=['<ip>:<port>']
    for proxy in list_proxy:
        check=ProxyChecker().check_proxy(proxy=proxy)
        print(proxy+" # "+str(check))
        # if "False" -> proxy die 
        #==========================================
        # example proxy live 
        # {
        # "country": "United States",
        # "country_code": "US",
        # "protocols": [
        #   "socks4",
        #   "socks5"
        #  ],
        # "anonymity": "Elite",
        # "timeout": 1649
        # }
