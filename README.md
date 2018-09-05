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

# 静态API列表
默认情况下，vultr模块会在第一次调用api函数时自动从[http://www.vultr.com/api/](http://www.vultr.com/api/)获取最新的API列表供向vultr.com发送请求时使用，这会一定程度上影响性能，因此，vultrapi模块的api_info_initial函数提供了一个api_info参数，调用api_info_initial时传入该参数可让vultrapi模块使用传入的API列表，不再从[http://www.vultr.com/api/](http://www.vultr.com/api/)获取最新的API列表，从而提高性能。该参数是一个dict类型的参数，键为API名称去掉“/v1/”（如“/v1/account/info”则取“account/info”作为键），值为API的“Request Type”。