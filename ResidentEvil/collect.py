# %%
import requests 
from bs4 import BeautifulSoup
from tqdm import tqdm
import pandas as pd

#%%
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

def get_links():
    url = 'https://www.residentevildatabase.com/personagens/'
    resp = requests.get(url, headers=headers, cookies=cookies)
    soup_personagens = BeautifulSoup(resp.text)
    ancoras = (soup_personagens.find('div', class_="td-page-content")
                            .find_all('a'))
    links = [i['href'] for i in ancoras]
    return links 

def get_content(url):
        resp = requests.get(url, cookies=cookies, headers=headers)
        return resp

def get_info(soup):
    div_page = soup.find('div',class_="td-page-content")
    paragrafo = div_page.find_all('p')[1]
    linhas = paragrafo.find_all('em')
    data = {}
    for i in linhas :
        chave, valor, *_ = i.text.split(':')
        chave= chave.strip(' ')
        valor = valor.strip(' ')
        data[chave]=valor
    return data 

def get_aparicoes(soup):
    lis = (soup.find('div', class_="td-page-content")
        .find('h4')
        .find_next()
        .find_all('li'))
    aparicoes = [i.text for i in lis]
    return aparicoes

def get_personagem(url):
    resp = get_content(url)

    # Verificar se deu certo e buscar infos
    if resp.status_code !=200:
        print ("Problema na extração")
    else:
        soup = BeautifulSoup(resp.text)
        data = get_info(soup)
        data['Aparicoes'] = get_aparicoes(soup)
    return data


# %%

links = get_links()
data = []

for i in tqdm(links):
     print(d)
     d=get_personagem(i)
     d['link']=i
     nome = i.strip('/').split('/')[-1].replace('-',' ').title()
     d["Nome"]=nome
     data.append(d)


# %%
df = pd.DataFrame(data) 
df.to_csv("dados_re", index=False, sep=';')
# %%
