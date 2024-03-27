#%%
print("Foi?")
# %%
import requests 

#%%
url = "https://www.residentevildatabase.com/personagens/alex-wesker/"

cookies = {
    '_gid': 'GA1.2.1514768992.1711414075',
    '_ga_DJLCSW50SC': 'GS1.1.1711414068.1.1.1711414088.40.0.0',
    '_ga_D6NF5QC4QT': 'GS1.1.1711414075.1.1.1711414089.46.0.0',
    '_ga': 'GA1.2.672223994.1711414068',
    'FCNEC': '%5B%5B%22AKsRol-sWrok5v2CeprQ0vP8vqyYkJe-GsiBLhYbeeYGpkbZRr-s2BwXz2d3JgF37ovTHr6AGBFiuEImToutxhJBjmZA-jt2NpTDJxntq-EM0XoxQwJsmeGzEzS8A883pffyxVtD1heuX_hTrG90sPgIGHZ4RT_jhA%3D%3D%22%5D%5D',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': '_gid=GA1.2.1514768992.1711414075; _ga_DJLCSW50SC=GS1.1.1711414068.1.1.1711414088.40.0.0; _ga_D6NF5QC4QT=GS1.1.1711414075.1.1.1711414089.46.0.0; _ga=GA1.2.672223994.1711414068; FCNEC=%5B%5B%22AKsRol-sWrok5v2CeprQ0vP8vqyYkJe-GsiBLhYbeeYGpkbZRr-s2BwXz2d3JgF37ovTHr6AGBFiuEImToutxhJBjmZA-jt2NpTDJxntq-EM0XoxQwJsmeGzEzS8A883pffyxVtD1heuX_hTrG90sPgIGHZ4RT_jhA%3D%3D%22%5D%5D',
    'referer': 'https://www.residentevildatabase.com/personagens/',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}
#%%
resp = requests.get(url, cookies=cookies, headers=headers)

# %%
resp.status_code
# %%
## 54 min - aula 1

# %%
