#修改 .bashhrc
    alias fy='python3 /home/yu/PycharmProjects/pyspider/baidu_translate.py'
    source .bashhrc
    
    fy 中国
    china
    
    开机自动运行脚本命令
    vim /etc/rc.local
    
    #!/bin/bash
    source /home/yu/.bashhrc
2、寻找登陆接口的方法
    a) 网页form表单中的action地址
    b) 通过抓包工具找到地址。