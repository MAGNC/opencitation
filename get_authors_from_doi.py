import requests
import pandas as pd
def get_author_info_by_doi(doi):
    # 构建 CrossRef API 的请求 URL
    base_url = f"https://api.crossref.org/works/{doi}"

    # 发送 GET 请求
    response = requests.get(base_url)

    if response.status_code == 200:
        # 解析 JSON 响应并获取文章信息
        data = response.json()
        if "message" in data and "author" in data["message"]:
            authors_data = data["message"]["author"]

            # 合并作者姓名信息
            authors = []
            for author_info in authors_data:
                given_name = author_info.get("given", "")
                family_name = author_info.get("family", "")
                full_name = f"{given_name} {family_name}".strip()
                authors.append(full_name)

            # 返回文章信息
            return ", ".join(authors)#作者之间用, 隔开
        else:
            print("Article information not found")
            return None
    else:
        print("Request failed")
        return None

# 使用DOI查询文章信息示例
all_data = "all_data.xlsx"
# sheet = pd.read_excel(path_citation_imp, sheet_name="Sheet1")
data = pd.read_excel(all_data, sheet_name="Sheet1")#我们只用再把这个数据库的doi补全即可。
doi = data.loc[:, 'DOI']
doi_list = []
for t in range(len(doi)):
    print(doi[t])
    doi_list.append(doi[t])#提取doi列表

author_list_for_citation_title_list = []
for doi in doi_list:
    author_string = get_author_info_by_doi(doi)
    author_list_for_citation_title_list.append(author_string)#根据doi列表查询作者,并且生成作者列表。

print(author_list_for_citation_title_list)
data['Authors_new'] = pd.Series(author_list_for_citation_title_list)
output_file = "all_data.xlsx"
data.to_excel(output_file, index=False)
print("Data with Authors column written to", output_file)
    # 打印其他文章信息字段
