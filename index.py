from PySimpleGUI import PySimpleGUI as pg

lista = [['Tiago', 1234]]

# LAYOUT

pg.theme('Reddit')
layout = [
    [pg.Text('Nome: '), pg.Input(key='nome')],
    [pg.Text('Senha: '), pg.Input(key='senha', password_char='*')],
    [pg.Button('Add', key='add')],
    [[pg.Column([[pg.Text(f'{lista[0][0]} - {lista[0][1]}')]], element_justification='center', key='coluna')]]
]

# JANELA
janela = pg.Window('Lista', layout=layout)

# LER EVENTOS
while True:
    eventos, valores = janela.read()
    if eventos == pg.WIN_CLOSED:
        print(layout)
        print('Programa finalizado.')
        break
    quant_nome = len(valores['nome'])
    quant_senha = len(valores['senha'])
    if eventos == 'add':
        if quant_nome == 0 or quant_senha == 0:
            print('Valores necessarios não foram adicionados.')
        else:
            nome = valores['nome']
            senha = valores['senha']
            lista += [[nome, senha]]
            print(lista)
            janela.extend_layout(janela['coluna'], [[pg.Text(f'{nome} - {senha}')]])
