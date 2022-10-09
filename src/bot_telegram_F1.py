from os import getenv
from dotenv import load_dotenv
from info_pilotos import info_dos_pilotos_f1
from proxima_corrida import ano_atual, proxima_corrida_f1
from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
)
from tabelas import (
    resultados_das_corridas,
    tabela_equipes_f1,
    tabela_pilotos_f1,
)

load_dotenv()

app = Client(
    'F1BRUnofficial_Bot',
    api_id=getenv('API_ID'),
    api_hash=getenv('API_HASH'),
    bot_token=getenv('BOT_TOKEN'),
)


@app.on_message(filters.command(['start', 'help']))
async def menu_opcoes(cliente, mensagem):
    print(mensagem.chat.username, mensagem.text, mensagem.chat.id)
    await mensagem.reply(
        f"""
Olá {mensagem.chat.username}!\n
Seja muito bem-vindo ao **F1BRUnofficial**, aqui você encontrará várias informações sobre a **F1**, confira os comandos abaixo!\n
Esses são os comandos:\n
/start - Mostra o menu!
/proxima_corrida - Mostra os horários e datas da próxima corrida!
/tabela_equipes - Mostra uma tabela com o ranking das equipes!
/tabela_pilotos - Mostra uma tabela com o ranking dos pilotos!
/resultados - Mostra o resultado de todas as corridas do ano vigente!""",
        quote=True,
    )


@app.on_message(filters.command(['proxima_corrida', 'corrida']))
async def dh_proxima_corrida(cliente, mensagem):
    print(mensagem.chat.username, mensagem.text, mensagem.chat.id)
    await mensagem.reply(proxima_corrida_f1(), quote=True)


@app.on_message(filters.command('pilotos'))
async def pilotos(cliente, mensagem):
    await mensagem.reply_text(
        text="""
Escolha um piloto abaixo para ter um resumo sobre sua carreira!

/Alexander_Albon
/Carlos_Sainz
/Charles_Leclerc
/Daniel_Ricciardo
/Esteban_Ocon
/Fernando_Alonso
/George_Russell
/Guanyu_Zhou
/Kevin_Magnussen
/Lance_Stroll
/Lando_Norris
/Lewis_Hamilton
/Max_Verstappen
/Mick_Schumacher
/Nicholas_Latifi
/Pierre_Gasly
/Sebastian_Vettel
/Sergio_Perez
/Valtteri_Bottas
/Yuki_Tsunoda""",
quote=True,
    )


@app.on_message(
    filters.command(
        [
            'Alexander_Albon',
            'Carlos_Sainz',
            'Charles_Leclerc',
            'Daniel_Ricciardo',
            'Esteban_Ocon',
            'Fernando_Alonso',
            'George_Russell',
            'Kevin_Magnussen',
            'Lance_Stroll',
            'Lando_Norris',
            'Lewis_Hamilton',
            'Max_Verstappen',
            'Mick_Schumacher',
            'Nicholas_Latifi',
            'Pierre_Gasly',
            'Sebastian_Vettel',
            'Sergio_Perez',
            'Valtteri_Bottas',
            'Yuki_Tsunoda',
            'Guanyu_Zhou',
        ]
    )
)
async def escolhido(cliente, mensagem):
    print(mensagem.chat.username, mensagem.text, mensagem.chat.id)
    await mensagem.reply_text('Aguarde... \u23F3', quote=True)
    nome_piloto = str(mensagem.text).lower().replace('/', '').replace('_', '-')
    await mensagem.reply(info_dos_pilotos_f1(nome=nome_piloto), quote=True)


@app.on_message(filters.command(['tabela_equipes', 'tabelaequipes']))
async def tabela_equipes(cliente, mensagem):
    print(mensagem.chat.username, mensagem.text, mensagem.chat.id)
    await mensagem.reply_text('Aguarde... \u23F3', quote=True)
    tabela_equipes_f1()
    await app.send_photo(
        mensagem.chat.id,
        'tabelaequipes.png',
        caption=f'\U0001f4cb TABELA DE PONTUAÇÂO DAS EQUIPES - **F1 {ano_atual()}**!!!',
    )


@app.on_message(filters.command(['tabela_pilotos', 'tabelapilotos']))
async def tabela_pilotos(cliente, mensagem):
    print(mensagem.chat.username, mensagem.text, mensagem.chat.id)
    await mensagem.reply_text('Aguarde... \u23F3', quote=True)
    tabela_pilotos_f1()
    await app.send_photo(
        mensagem.chat.id,
        'tabelapilotos.png',
        caption=f'\U0001f4cb TABELA DE PONTUAÇÂO DOS PILOTOS - F1 **{ano_atual()}**!!!',
    )


@app.on_message(filters.command(['resultado_corridas', 'resultados']))
async def resultado_corridas_anteriores(cliente, mensagem):
    print(mensagem.chat.username, mensagem.text, mensagem.chat.id)
    await mensagem.reply_text('Aguarde... \u23F3', quote=True)
    resultados_das_corridas()
    await app.send_photo(
        mensagem.chat.id,
        'tabelaresultados.png',
        caption=f'\U0001f4cb TABELA DE RESULTADOS DE TODAS AS CORRIDAS DO ANO - F1 **{ano_atual()}**!!!',
    )


@app.on_message()
async def qualquer_outra_mensagem(cliente, mensagem):
    print(mensagem.chat.username, mensagem.text, mensagem.chat.id)
    await mensagem.reply(
        'Comando inválido!\U0001f9d0 \n\nDigite /start para ver todos os comandos que podem ser usados.',
        quote=True,
    )


app.run()