import requests
import json
import base64

# 请求获取 JSON 数据
url = "http://vv.ejym.site/opconf.json"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    # 提取 VLESS 信息并转换为 v2rayN 可订阅的格式
    vless_links = []
    for item in data.get("inbounds", []):
        if item.get("protocol") == "vless":
            # 构建 v2rayN 链接格式
            address = item["settings"]["clients"][0]["address"]
            port = item["port"]
            id = item["settings"]["clients"][0]["id"]
            flow = item["streamSettings"]["flow"]
            network = item["streamSettings"]["network"]
            security = item["streamSettings"]["security"]
            path = item["streamSettings"]["path"]
            name = item.get("tag", "v2rayN-Subscription")
            
            link = f"vless://{id}@{address}:{port}?type={network}&security={security}&path={path}&flow={flow}#{name}"
            vless_links.append(link)
    
    # 将所有链接连接成字符串，并编码为 Base64
    vless_content = "\n".join(vless_links)
    vless_content_base64 = base64.urlsafe_b64encode(vless_content.encode()).decode()
    
    # 保存到 TXT 文件
    with open("v2rayN_subscription.txt", "w") as f:
        f.write(vless_content_base64)
else:
    print(f"无法获取数据，HTTP状态码：{response.status_code}")
