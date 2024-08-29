import requests

# 请求获取 JSON 数据
url = "http://vv.ejym.site/opconf.json"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    # 提取所有的 "ovpn" 信息
    ovpn_links = []
    items = data.get("data", {}).get("items", [])
    
    for group in items:
        for item in group.get("items", []):
            ovpn_link = item.get("ovpn")
            if ovpn_link:
                ovpn_links.append(ovpn_link)

    if not ovpn_links:
        print("没有找到任何 OVPN 链接")  # 如果没有提取到链接，输出调试信息

    # 将所有链接连接成字符串
    ovpn_content = "\n".join(ovpn_links)
    
    # 保存到 TXT 文件
    with open("v2rayN_subscription.txt", "w") as f:
        f.write(ovpn_content)

    print("OVPN 链接已保存到 v2rayN_subscription.txt")
else:
    print(f"无法获取数据，HTTP状态码：{response.status_code}")
