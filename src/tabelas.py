from df2img import plot_dataframe, save_dataframe
from pandas import read_html


# Retorna uma tabela das equipes com resultados do ano vigente!
def tabela_equipes_f1():
    urlsite: str = 'https://www.formula1.com/en/results.html/2022/team.html'
    tabelaequipes = read_html(urlsite, encoding='utf-8')[0].set_index('Pos')
    tabelaequipes = tabelaequipes.drop(
        ['Unnamed: 0', 'Unnamed: 4'], axis=1
    ).rename(columns={'Pos': 'Posição', 'Team': 'Equipes', 'PTS': 'Pontos'})
    fig = plot_dataframe(
        tabelaequipes,
        col_width=[0.3, 2.0, 0.5],
        # title=dict(
        #     font_color="tomato",
        #     font_family="Times New Roman",
        #     font_size=18,
        #   text="TABELA DAS EQUIPES - F1 2022",
        # ),
        tbl_header=dict(
            align='center',
            fill_color='blue',
            font_color='white',
            line_color='white',
            font_size=20,
            line_width=2,
            height=45,
        ),
        tbl_cells=dict(
            align=['center', 'right', 'center'],
            line_color='white',
            font_color='black',
            height=50,
            line_width=2,
            font_size=20,
        ),
        row_fill_color=('#EBF0F8', '#FFFFFF'),
        fig_size=(875, 550),
    )
    save_dataframe(fig=fig, filename='tabelaequipes.png')


# Retorna uma tabela dos pilotos com resultados da temporada vigente!
def tabela_pilotos_f1():
    urlsite: str = 'https://www.formula1.com/en/results.html/2022/drivers.html'
    tabelapilotos = read_html(urlsite, encoding='utf-8')[0].set_index('Pos')
    tabelapilotos = tabelapilotos.drop(
        ['Unnamed: 0', 'Unnamed: 6'], axis=1
    ).rename(
        columns={
            'Pos': 'Posição',
            'Driver': 'Pilotos',
            'Nationality': 'Nacionalidade',
            'Car': 'Equipes',
            'PTS': 'Pontos',
        }
    )
    quant_pilotos = tabelapilotos['Pilotos'].count()
    fig = plot_dataframe(
        tabelapilotos,
        col_width=[1.0, 2.75, 1.75, 2.75, 1.5],
        tbl_header=dict(
            align='center',
            fill_color='blue',
            font_color='white',
            line_color='white',
            font_size=20,
            line_width=2,
            height=45,
        ),
        tbl_cells=dict(
            align=['center', 'right', 'center', 'right', 'center'],
            line_color='white',
            font_color='black',
            font_size=20,
            height=50,
            line_width=2,
        ),
        row_fill_color=('#EBF0F8', '#FFFFFF'),
        fig_size=(1575, (quant_pilotos * 52.40)),
    )
    save_dataframe(fig=fig, filename='tabelapilotos.png')


# Retorna uma tabela com os resultados e detahes de cada GP que aconteceram no ano!
def resultados_das_corridas():
    url: str = 'https://www.formula1.com/en/results.html/2022/races.html'
    resul_corridas = read_html(url, encoding='utf-8')[0].set_index(
        'Grand Prix'
    )
    resul_corridas = resul_corridas.drop(
        ['Unnamed: 0', 'Unnamed: 7'], axis=1
    ).rename(
        columns={
            'Date': 'Datas',
            'Winner': 'Ganhadores',
            'Car': 'Equipes',
            'Laps': 'Voltas',
            'Time': 'Tempo da Corrida',
        }
    )
    total_corridas = resul_corridas['Ganhadores'].count()
    fig = plot_dataframe(
        resul_corridas,
        col_width=[1.25, 1, 1.75, 1.75, 0.6, 1.5],
        tbl_header=dict(
            align='center',
            fill_color='blue',
            font_color='white',
            line_color='white',
            font_size=20,
            line_width=2,
            height=45,
        ),
        tbl_cells=dict(
            align=['right', 'center', 'right', 'right', 'center', 'center'],
            line_color='white',
            font_color='black',
            font_size=20,
            height=50,
            line_width=2,
        ),
        row_fill_color=('#EBF0F8', '#FFFFFF'),
        fig_size=(1675, (total_corridas * 54.40)),
    )
    save_dataframe(fig=fig, filename='tabelaresultados.png')


if __name__ == '__main__':
    tabela_equipes_f1()
    tabela_pilotos_f1()
    resultados_das_corridas()
