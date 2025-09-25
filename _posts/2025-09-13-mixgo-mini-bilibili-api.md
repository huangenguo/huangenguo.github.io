---
title: "基于 Mixgo Mini 的B站粉丝计数器"
excerpt_separator: "<!--more-->"
categories:
  - Tech
  - Education
tags:
  - 米思齐
  - Mixgo Mini
  - 粉丝计数器
  - Bilibili
---
{% include video id="BV1qZHfzPER9" provider="bilibili" danmaku="1" %}

## 项目介绍

制作一个实时显示B站粉丝数的计数器，基于 Mixgo Mini 开发板实现。

<!--more-->
## 测试官方示例

官方提供了利用HTTPS协议获取互联网中的数据的例程，测试没问题，说明固件的基础网络功能（HTTP 请求、DNS 解析）是正常的。

## Bilibili API

### 方案一：直接调用B站API（推荐）

```python
UID=32828583
String followerUrl = "https://api.bilibili.com/x/relation/stat?vmid=" + UID;   // 粉丝数 follower 的值
String viewAndLikesUrl = "https://api.bilibili.com/x/space/upstat?mid=" + UID; // 播放数 archive 的 view 键的值、点赞数 likes 的值
```

[B站粉丝计数器 \| ESP32学习之旅-Arduino版 DF创客社区](https://mc.dfrobot.com.cn/thread-303095-1-1.html)

Markdown 会把 \| 竖杠理解成表格，尝试用\斜杠来转义

### 方案二：Substats API

代码年久失修，部分功能失效。

```python
https://api.spencerwoo.com/substats/?source=github&queryKey=spencerwooo
https://api.spencerwoo.com/substats/?source=bilibili&queryKey=32828583
```

[Substats Docs](https://substats.spencerwoo.com/builder/)

### 方案三：Mixio 物联网平台返参

第三种方法是借助 Mixio 物联网平台传参。

## 注意事项

1. HTTPS 问题解决
   - 尝试降级使用 HTTP API
   - 或更新支持 SSL 的固件

2. 优化建议
   - 添加错误处理
     - 添加网络重连机制
     - 请求失败后延时重试
     - 显示错误状态提示
   - 性能优化
     - 实现数据缓存
     - 控制请求频率，比如10分钟请求一次
     - 添加无法连接网络或等待超时时的休眠模式
   - 功能扩展
     - 支持多UP主切换
     - 添加更多数据指标
     - 实现按键交互

## HTTPS 请求错误

> 遇到 ImportError: no module named 'ussl' 错误

前面测试过官方示例，出现这个问题，更多是在 B 站 API 的特殊性 上（比如强制 HTTPS 重定向、需要特定请求头、反爬虫限制等）。

B 站 API 可能强制 HTTPS 重定向，所以需要使用 HTTPS 请求。
另外，B 站 API 可能会拒绝 “无标识” 的请求（认为是爬虫），添加User-Agent请求头模拟浏览器。

## API调试工具

[Postman API Platform](https://web.postman.co/)

## 常见错误码解释

-202：域名解析失败（DNS 问题）。同一IP地址的反爬限制。同样是接入手机热点，一是使用手机移动蜂窝网络，二是使用路由器WiFi。

-103：连接超时

-110：连接被拒绝

-104：连接重置

## B站粉丝数获取代码示例

```python
import network
import mixiot
import urequests
import machine

def main():
    wlan = network.WLAN(network.STA_IF)
    print("连接WiFi...")
    # 修改热点名称和密码
    mixiot.wlan_connect('iPhone', '666666')
    if not wlan.isconnected():
        print("WiFi连接失败")
        return
    
    # 切换DNS
    ip, subnet, gateway, _ = wlan.ifconfig()
    wlan.ifconfig((ip, subnet, gateway, '223.5.5.5'))
    print(f"网络配置：{wlan.ifconfig()}")
    
    # 关键：添加请求头，模拟浏览器
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        url = 'http://api.bilibili.com/x/relation/stat?vmid=32828583'
        # 带请求头发送请求
        response = urequests.get(url, headers=headers)
        print(f"状态码：{response.status_code}")
        # 检查是否被重定向（状态码301/302表示重定向）
        if 300 <= response.status_code < 400:
            print(f"被重定向到：{response.headers.get('Location')}")
        else:
            print(f"响应内容：{response.text[:100]}")
        response.close()
    except OSError as e:
        print(f"网络错误：{e}")
        if hasattr(e, 'errno'):
            if e.errno == -202:
                print("→ DNS解析失败（已自动切换公共DNS，建议重试）")
            elif e.errno == -103:
                print("→ 连接超时（urequests无timeout参数，需手动等待）")        
    except Exception as e:
        print(f"其他错误：{e}")

if __name__ == "__main__":
    main()
```

## B站粉丝数代码示例升级

升级需求
JOSN反序列化处理成字典并显示字典的follower字段，点阵屏会不断滚动显示当前粉丝数，每 10 分钟自动更新一次数据

```python
import network
import mixiot
import urequests
import time
from mixgo_mini import onboard_matrix  # 导入矩阵屏模块

# 配置参数
WIFI_SSID = 'iPhone'
WIFI_PWD = '666666'
API_URL = 'http://api.bilibili.com/x/relation/stat?vmid=32828583'  # B站API
UPDATE_INTERVAL = 600  # 10分钟(600秒)更新一次数据
DISPLAY_INTERVAL = 5  # 每次显示后间隔5秒，控制循环显示频率
last_follower = "初始化中"  # 存储最新粉丝数，初始值为提示文本

def connect_wifi():
    """连接WiFi并设置DNS"""
    wlan = network.WLAN(network.STA_IF)
    if not wlan.isconnected():
        onboard_matrix.scroll("连WiFi中...")
        mixiot.wlan_connect(WIFI_SSID, WIFI_PWD)
        time.sleep(2)
    if wlan.isconnected():
        ip, subnet, gateway, _ = wlan.ifconfig()
        wlan.ifconfig((ip, subnet, gateway, '223.5.5.5'))  # 固定DNS
        onboard_matrix.scroll(f"WiFi已连 IP:{ip.split('.')[-1]}")
        return True
    else:
        onboard_matrix.scroll("WiFi失败")
        return False

def update_follower():
    """更新粉丝数，返回最新值"""
    global last_follower
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0',
            'Host': 'api.bilibili.com'
        }
        response = urequests.get(API_URL, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            if data.get('code') == 0 and 'data' in data:
                last_follower = str(data['data'].get('follower', '未知'))
                print(f"已更新粉丝数: {last_follower}")
            else:
                last_follower = "API异常"
        else:
            last_follower = f"状态码:{response.status_code}"
        
        response.close()
    except Exception as e:
        last_follower = f"获取失败"
        print(f"更新错误: {e}")
    return last_follower

def main():
    # 初始化WiFi
    if not connect_wifi():
        while True:
            onboard_matrix.scroll("请检查WiFi")
            time.sleep(DISPLAY_INTERVAL)
    
    # 首次获取粉丝数
    update_follower()
    
    while True:
        # 记录本轮循环开始时间
        loop_start = time.time()
        
        # 在10分钟内循环显示最新粉丝数
        while time.time() - loop_start < UPDATE_INTERVAL:
            # 持续滚动显示当前粉丝数
            onboard_matrix.scroll(f"B站粉丝数: {last_follower}")
            # 每次显示后间隔一段时间，控制频率
            time.sleep(DISPLAY_INTERVAL)
        
        # 10分钟后更新数据
        onboard_matrix.scroll("更新中...")
        update_follower()
        time.sleep(2)  # 等待更新提示显示完毕

if __name__ == "__main__":
    main()
```

## 参考资源

[Bilibili API 文档](https://github.com/SocialSisterYi/bilibili-API-collect)

[Mixly 官方文档](https://mixly.cn/)

[MicroPython 网络编程](https://docs.micropython.org/en/latest/library/network.html)

## 升级需求

按键重置

网页配置新的热点

休眠模式
