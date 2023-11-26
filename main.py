#版本 1.0 (2023/11/26)
import wget
import os
print('欢迎使用 Minecraft Server 部署程序！')
print('本程序由 Ad_closeNN 所制作')
ver = input('请输入你需要安装的 Minecraft 正式版版本号\n>>1.16.5, 1.17.1, 1.18.2, 1.19.4, 1.20.1, 1.20.2<<\n版本: ')
if ver == '1.16.5': #版本1.16.5
    url = 'https://piston-data.mojang.com/v1/objects/1b557e7b033b583cd9f66746b7a9ab1ec1673ced/server.jar'
    print("正在下载中...")  
    dir = "./servers"+"/"+ver+"/"
    if os.path.exists(os.path.join(dir, './server')):
        print('\n由于目录已存在，可直接使用')
        wget.download(url,'./servers/'+ver+'/')
    else:      
        os.mkdir("./servers/")
        os.mkdir("./servers"+"/"+ver+"/")
        wget.download(url,'./servers/'+ver+'/')