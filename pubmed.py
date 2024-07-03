from Bio import Entrez

# 设置邮箱地址
Entrez.email = "aiden1705@outlook.com"

# 定义搜索函数
def search_pubmed(query):
    handle = Entrez.esearch(db="pubmed", term=query, retmax=5)
    record = Entrez.read(handle)
    handle.close()
    return record["IdList"]

# 获取文献摘要
def fetch_abstracts(id_list):
    ids = ",".join(id_list)
    handle = Entrez.efetch(db="pubmed", id=ids, rettype="abstract", retmode="text")
    abstracts = handle.read()
    handle.close()
    return abstracts

# 示例查询
query = "Autism"
id_list = search_pubmed(query)
abstracts = fetch_abstracts(id_list)
print(abstracts)
