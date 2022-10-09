from datetime import date
import requests
from bs4 import BeautifulSoup as bs


def ano_atual():
    return date.today().year


headers: dict = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'DNT': '1',  # Do Not Track Request Header
    'Connection': 'close',
}

# Mostra informações da próxima corrida, busca os dados no site da band!
def proxima_corrida_f1():
    urlsite = 'https://www.band.uol.com.br/esportes/automobilismo/formula-1/classificacao'
    requisicao = requests.get(urlsite, headers=headers).content
    html = bs(requisicao, 'lxml')
    data_corrida = html.find('time', class_='date').get_text(' ', strip=True)
    horario_corrida = html.find('div', class_='time').get_text(strip=True)
    circuito_corrida = html.find('span', class_='locale').get_text(strip=True)
    grande_premio = html.find('span', class_='circuit__name').get_text(
        strip=True
    )
    etapa_no_ano = html.find('span', class_='phase').get_text(strip=True)
    dia_da_classificacao = (
        html.find('div', class_='phase-classificacao training')
        .getText(';', strip=True)
        .split(';')
    )
    primeiro_treino_tl1 = (
        html.find('div', class_='phase-1-treino-livre training')
        .getText(';', strip=True)
        .split(';')
    )
    segundo_treino_tl2 = (
        html.find('div', class_='phase-2-treino-livre training')
        .getText(';', strip=True)
        .split(';')
    )
    terceiro_treino_tl3 = (
        html.find('div', class_='phase-3-treino-livre training')
        .getText(';', strip=True)
        .split(';')
    )

    try:
        corrida_sprint = (
            html.find('div', class_='phase-treino-classificatorio training')
            .getText(';', strip=True)
            .split(';')
        )

    except AttributeError:
        return f"""
\U0001f193  **1° TREINO LIVRE (TL1)**\n
Dia da semana:  {primeiro_treino_tl1[0]}
Data:  {primeiro_treino_tl1[1]}
Horário:  {primeiro_treino_tl1[3]}\n
\U0001f193  **2° TREINO LIVRE (TL2)**\n
Dia da semana:  {segundo_treino_tl2[0]}
Data:  {segundo_treino_tl2[1]}
Horário:  {segundo_treino_tl2[3]}\n
\U0001f193  **3° TREINO LIVRE (TL3)**\n
Dia da semana:  {terceiro_treino_tl3[0]}
Data:  {terceiro_treino_tl3[1]}
Horário:  {terceiro_treino_tl3[3]}\n
\U0001f947 \U0001f948 \U0001f949  **DIA DA CLASSIFICAÇÃO**\n
Dia da semana:  {dia_da_classificacao[0]}
Data:  {dia_da_classificacao[1]}
Horário:  {dia_da_classificacao[3]}\n
\U0001f3c1  **DIA DA CORRIDA**\n
Data:  {data_corrida}
Horário:  {horario_corrida}
Circuíto:  {circuito_corrida}
Grande Prêmio:  {grande_premio}
Total corridas no ano:  {etapa_no_ano}\n
Fonte: band.uol.com.br"""

    else:
        return f"""
\U0001f193  **1° TREINO LIVRE (TL1)**\n
Dia da semana:  {primeiro_treino_tl1[0]}
Data:  {primeiro_treino_tl1[1]}
Horário:  {primeiro_treino_tl1[3]}\n
\U0001f3ce\uFE0F  **CORRIDA SPRINT**\n
Dia da semana:  {corrida_sprint[0]}
Data:  {corrida_sprint[1]}
Horário:  {corrida_sprint[3]}\n
\U0001f193  **2° TREINO LIVRE (TL2)**\n
Dia da semana:  {segundo_treino_tl2[0]}
Data:  {segundo_treino_tl2[1]}
Horário:  {segundo_treino_tl2[3]}\n
\U0001f947 \U0001f948 \U0001f949  **DIA DA CLASSIFICAÇÃO**\n
Dia da semana:  {dia_da_classificacao[0]}
Data:  {dia_da_classificacao[1]}
Horário:  {dia_da_classificacao[3]}\n
\U0001f3c1  **DIA DA CORRIDA**\n
Data:  {data_corrida}
Horário:  {horario_corrida}
Circuíto:  {circuito_corrida}
Grande Prêmio:  {grande_premio}
Total corridas no ano:  {etapa_no_ano}\n
Fonte: band.uol.com.br"""


if __name__ == '__main__':
    print(proxima_corrida_f1())
    print(ano_atual())
