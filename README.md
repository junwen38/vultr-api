vultr-api是一个非官方的vultr.com API客户端类库，提供了一个友好的接口供Python应用程序调用vultr.com API使用。

# 特色
* 封装了vultr.com的所有API
* 可以自动支持新增的API而无需更新本类库

# 安装

    cd /path/to/vultr-api/src && pip install .

# 使用
以获取服务器列表的API-"/v1/server/list"为例进行说明：

    from vultrapi import Vultr
    api_key = API_KEY
    vultr = Vultr(api_key)
    #不带参数调用
    server_list = vultr.server.list()
    #带参数调用
    server = vultr.server.list(SUBID=server_list.values[0]["SUBID"])

更多API请参考[http://www.vultr.com/api/](http://www.vultr.com/api/)

