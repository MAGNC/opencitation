from habanero import Crossref
import requests
import json
# 定义一个DOI
doi = "10.1145/3491102.3502068"  # 替换成你要查询的DOI

def get_information(title):
    base_url = "https://api.crossref.org/works"
    params = {"query.bibliographic": title}
    # 发送 GET 请求
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        # 解析 JSON 响应并获取 DOI
        data = response.json()
        with open("crossref.json", "w+") as f:
            json.dump(data, f)
        if data["message"]["items"]:
            items = data["message"]["items"]
        print(items)
    else:
        return "Request failed"

get_information("Characterizing Practices, Limitations, and Opportunities Related to Text Information Extraction Workflows: A Human-in-the-loop Perspective")