# demacia
## 简介
> 最近在研究 virjar 大佬的 sekiro 项目，发现贼好用，但因为是使用 java 开发的，本人也是 java 菜鸡，就研究了下其原理，使用 python 的 tornado 框架写了个简陋版的

## 目录结构
```
demacia  --项目目录
    demo  --demo，示例代码
        app  --app demo
            action.py       --注册函数具体实现逻辑
            frida_hook.py   --frida hook app 脚本
            script.js       --frida js 脚本
            test_api.py     --测试 http 请求，调用转发
            ws_client.py    --客户端连接服务端 websocket 脚本
        js  --js demo
            demacia_client.html
            demacia_client.js

    src  --server服务端代码
        handler
            group.py            --group 统一处理脚本
            response.py         --返回 response 统一处理
        http
            async_invoke.py     --注册函数调用转发
            get_group_list.py   --获取 注册的 group list
            index.py            --测试接口，主要用于校验服务是否有问题
        utils
            log_settings.py     --log
        socket_server.py        --socket 处理逻辑

    .gitignore      
    install.sh  --手机端工具包一键安装sh脚本
    README.md
    requirements.txt  --python项目依赖包
    run.py  --server启动文件
    yuan.sh  --apt切换源sh脚本
```

## 使用
### 1、快速体验
```
1、启动 tornado server 运行 run.py
2、运行 demo.app.ws_client.py 连接 tornado server socket
    tips: 
    1、需要手机启动 frida-server。
    2、frida_hook.py 脚本需要修改设备ID。
    device = frida.get_device('73fe1d8a')
    3、需要手机启动 天猫 app，版本 8.11 自行下载
3、运行 test_api.py 获取结果
```

### 2、手机运行 frida hook 脚本
```
1、手机安装 termux 软件，这个自行下载
2、打开 termux 切换源，命令在 yuan.sh 脚本里，可以直接执行
3、安装软件，命令在 install.sh 脚本里
4、安装完成后使用 tsu 切换到 root 权限，然后执行 ws_clien.py 脚本即可
    tips:
    1、frida_hook.py 脚本获取设备这里，直接修改为
    device = frida.get_local_device()
    2、需要修改脚本里的 IP 地址，默认是 127.0.0.1 改成电脑 IP
    3、此方法，不需要启动 frida-server 需要启动 app
5、电脑端直接运行 test_api.py 获取结果，即可
```
