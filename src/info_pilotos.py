from re import compile
import requests
from bs4 import BeautifulSoup as bs
from proxima_corrida import ano_atual
from py_trans import PyTranslator

headers: dict = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'DNT': '1',  # Do Not Track Request Header
    'Connection': 'close',
}


def removedor_tags_html(html: str):
    return compile(r'<[^>]*>').sub('', html).split(sep=',', maxsplit=9)


def tradutor_en_pt(texto: str):
    setup = PyTranslator(provider='google')
    texto_traduzido: dict = setup.translate(text=texto, dest_lang='pt')
    return texto_traduzido


def info_dos_pilotos_f1(nome: str):
    url_site: str = f'https://www.formula1.com/en/drivers/{nome}.html'
    requisicao = requests.get(url=url_site, headers=headers)
    html = bs(requisicao.content, 'lxml')
    detalhes = html.find_all('td', class_='stat-value')
    detalhes_string: str = (
        str(detalhes).replace('[', '').replace(']', '').replace(' ', '')
    )
    detalhes_string: str = removedor_tags_html(html=detalhes_string)
    biografia = (
        html.find('section', class_='biography')
        .get_text(strip=True)
        .replace('Biography', '')
    )
    biografia_traduzida = tradutor_en_pt(biografia)
    idade: int = abs(ano_atual() - int(detalhes_string[8][6:]))
    nome_piloto = html.find('h1', class_='driver-name').get_text(strip=True)
    numero_piloto = html.find('div', 'driver-number').get_text(strip=True)

    return f"""
\nNome do Piloto:  {nome_piloto}
Número do Piloto:  {numero_piloto}
Equipe:  {detalhes_string[0]} 
País:  {tradutor_en_pt(detalhes_string[1])["translation"]}
Pódios:  {detalhes_string[2]}
Pontos:  {detalhes_string[3]}
Campeonato(s) Mundial(ais):  {detalhes_string[5]}
Participações em GPs:  {detalhes_string[4]}
Melhor posição em corrida:  {detalhes_string[6]}
Posição mais alta do Grid:  {detalhes_string[7]}
Idade:  {idade}
Data de nascimento:  {detalhes_string[8]}
Local de nascimento:  {tradutor_en_pt(detalhes_string[-1])["translation"]}

Biografia:

{biografia_traduzida["translation"]}


Fonte: {url_site}"""


if __name__ == '__main__':
    print(info_dos_pilotos_f1())
