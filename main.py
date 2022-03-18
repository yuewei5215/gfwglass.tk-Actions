import requests
import json
import time
import re
import logging
import traceback
import os
import random
import datetime
import utils
# import base64


def main(event, context):
    # 初始化日志文件
    utils.initLog('log.txt')
    utils.clearLog()
#    savePoint(
#        'https://subsc.ednovas.xyz/sub?target=clash&url=https://raw.githubusercontent.com/ldir92664/Vmess-Actions/main/subscribe/vmess.txt&insert=false&config=https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/config/ACL4SSR_Online_Mini_MultiMode.ini&emoji=true&list=false&tfo=false&scv=false&fdn=false&sort=false&expand=true&new_name=true', 'clash.yml')

#    savePoint(
#        'https://suo.yt/RvwZNEH', 'clash.yml')

#    savePoint(
#        'https://suc.bihai.ml/sub?target=clash&new_name=true&url=https%3A%2F%2Fraw.githubusercontent.com%2Fldir92664%2FVmess-Actions%2Fmain%2Fsubscribe%2Fvmess.txt%7Chttps%3A%2F%2Fraw.githubusercontent.com%2Fldir92664%2FVmess-Actions%2Fmain%2Fsubscribe%2Ftrojan.txt&insert=false&config=https%3A%2F%2Fraw.githubusercontent.com%2FACL4SSR%2FACL4SSR%2Fmaster%2FClash%2Fconfig%2FACL4SSR_Online.ini', 'clash.yml')

    savePoint(
        'https://api.dler.io/sub?target=clash&new_name=true&url=https%3A%2F%2Fgfwglass.tk%2Fclash%2Fproxies%3Fnc%3DCN%2CHK%2CTW%26speed%3D30%2C100%26type%3Dvmess%2Ctrojan%2Cssr%2Css&insert=false&config=https%3A%2F%2Fraw.githubusercontent.com%2FACL4SSR%2FACL4SSR%2Fmaster%2FClash%2Fconfig%2FACL4SSR_Online.ini', 'clash.yml')

    savePoint(
        'https://api.dler.io/sub?target=clash&new_name=true&url=https%3A%2F%2Fsspool.herokuapp.com%2Fclash%2Fproxies%3Fnc%3DCN%2CHK%2CTW%26speed%3D30%26type%3Dvmess%2Ctrojan%2Cssr%7Chttps%3A%2F%2Fgfwglass.tk%2Fclash%2Fproxies%3Fnc%3DCN%2CHK%2CTW%26speed%3D30%26type%3Dvmess%2Ctrojan%2Cssr%7Chttps%3A%2F%2Fednovas.design%2Fclash%2Fproxies%3Fnc%3DCN%2CHK%2CTW%26speed%3D30%26type%3Dvmess%2Ctrojan%2Cssr&insert=false&config=https%3A%2F%2Fraw.githubusercontent.com%2FACL4SSR%2FACL4SSR%2Fmaster%2FClash%2Fconfig%2FACL4SSR_Online.ini', 'clash-pro.yml')

    savePoint(
        'https://api.dler.io/sub?target=clash&new_name=true&url=https%3A%2F%2Fednovas.design%2Fclash%2Fproxies%3Fnc%3DCN%2CHK%2CTW%26speed%3D30%2C100%26type%3Dvmess%2Ctrojan%2Cssr%2Css&insert=false&config=https%3A%2F%2Fraw.githubusercontent.com%2FACL4SSR%2FACL4SSR%2Fmaster%2FClash%2Fconfig%2FACL4SSR_Online.ini', 'ednovas.design.yml')
    
    savePoint(
        'https://api.dler.io/sub?target=clash&new_name=true&url=https%3A%2F%2Fraw.githubusercontent.com%2Fimyaoxp%2Fgetclash%2Fmaster%2Fsub%2Fsub_merge_yaml.yml&insert=false&config=https%3A%2F%2Fraw.githubusercontent.com%2FACL4SSR%2FACL4SSR%2Fmaster%2FClash%2Fconfig%2FACL4SSR_Online.ini', 'imyaoxp-getclash.yml')
    
    savePoint(
        'https://api.dler.io/sub?target=clash&new_name=true&url=https%3A%2F%2Fraw.githubusercontent.com%2Fldir92664%2FTop-FreeProxies%2Fmaster%2Fupdate%2Fprovider%2Fprovider-all.yml&insert=false&config=https%3A%2F%2Fraw.githubusercontent.com%2FACL4SSR%2FACL4SSR%2Fmaster%2FClash%2Fconfig%2FACL4SSR_Online.ini&exclude=HK%7CTW%7CCN&append_type=true&emoji=true&list=false&udp=true&tfo=false&scv=false&fdn=true&sort=true', 'Top-FreeProxies.yml')
    
    savePoint(
        'https://raw.githubusercontent.com/lizisan/Free-Proxies/main/README.md', 'README.md')
    
    # 获取文章地址


def savePoint(url, name):
    resp = requests.get(url)
    dirs = './subscribe'
    day = time.strftime('%Y.%m.%d', time.localtime(time.time()))
    if 'proxies' in resp.text:
        if not os.path.exists(dirs):
            os.makedirs(dirs)
        with open(dirs + '/' + name, 'w', encoding='utf-8') as f:
            f.write(resp.text.replace('Relay_', day+'_'))
            print(name+'生成成功')


# 主函数入口
if __name__ == '__main__':
    main("", "")
