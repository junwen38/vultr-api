'''
Created on 2017年10月28日

@author: junwen38
'''
from requests.exceptions import HTTPError

__api_info = None

def api_info_initial(api_info = None):
    if not api_info:
        from requests import get
        import re
        global __api_info
        res = get("https://www.vultr.com/api/")
        html = res.text
        methods = (m.group(1) for m in re.finditer(r"<td>(POST|GET)</td>", html))
        names = (m.group(1) for m in re.finditer(r"<li><a href=\"#.*\">/v1/(.*?)</a></li>", html))
        __api_info = dict(zip(names, methods))
    else:
        __api_info = api_info
    
class __RPC:
    def __init__(self, api_key, name):
        self.api_key = api_key
        self.name = name
        
    def __getattr__(self, name):
        return eval("__RPC")(self.api_key, self.name + "/" + name)
    
    def __call__(self, **kwargs):
        import requests
        
        api_info = eval("__api_info")
        if (not api_info):
            api_info_initial()
            api_info = eval("__api_info")
        if (self.name not in api_info):
            raise ValueError("The API is not exists.")
        
        if (api_info[self.name] == "GET"):
            res = requests.get("https://api.vultr.com/v1/" + self.name, headers={"API-Key": self.api_key}, params=kwargs)
        elif (api_info[self.name] == "POST"):
            res = requests.post("https://api.vultr.com/v1/" + self.name, headers={"API-Key": self.api_key}, data=kwargs)
        
        if (res.status_code == 200):
            if res.text.strip() == "":
                return res.text
            else:
                return res.json()
        else:
            res.raise_for_status()

class Vultr:
    def __init__(self, api_key):
        self.api_key = api_key
    
    def __getattr__(self, name):
        return eval("__RPC")(self.api_key, name)
        
