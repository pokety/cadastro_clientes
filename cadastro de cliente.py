import random
import sqlite3
import PySimpleGUI as sg
from PySimpleGUI import popup


def Tela():
    sg.theme("Reddit")

    layout = [
        [sg.Text("Cadastro de Clientes")],
        [sg.Text("NOME COMPLETO  "), sg.Input("" ,size=(40, 1))],
        [sg.Text("CPF                        "), sg.Input("",size=(40, 1))],
        [sg.Text("TELEFONE              "), sg.Input("", size=(40, 1))],
        [sg.Text("ENDERECO             "), sg.Input("", size=(40, 1))],
        [sg.Text("E-MAIL                    "), sg.Input("", size=(40, 1))],
        [sg.Button("SALVAR"),sg.Button("PESQUISAR")],
        [sg.Text('', key='-OUTPUT-')]
    ]

    janela1 = sg.Window("CADASTRO DE CLIENTE", layout,finalize=True)
    while True:

        eventos, valor = janela1.read()
        print(valor)

        try:
            nome = valor[0]
        except:
            print("")
        try:
            cpf = valor[1]
        except:
            print("")
        try:
            telefone = valor[2]
        except:
            print("")
        try:
            endereco = valor[3]
        except:
            print("")
        try:
            email = valor[4]
        except:
            print("")
        banco = sqlite3.connect('dados.db')
        cursor = banco.cursor()
        if eventos == "PESQUISAR":
            cursor.execute(f"SELECT nome, cpf, telefone, endereco, email FROM cliente WHERE nome ='{nome}' OR cpf = '{cpf}' ORDER BY nome ASC")
            banco.commit()
            tabela1 = cursor.fetchall()
            print(tabela1)
            for c in tabela1:
                output = f" Nome:{c[0]}\n CPF:{c[1]}\n TELEFONE:{c[2]}\n ENDERECO:{c[3]}\n E-MAIL:{c[4]}"
                janela1['-OUTPUT-'].update(output)

        if eventos == "SALVAR":
            #banco = sqlite3.connect('dados.db')
            #cursor = banco.cursor()
            #cursor.execute("CREATE TABLE cliente (id integer,nome text,cpf text,telefone text,endereco text,email text)")
            cursor.execute(f"INSERT INTO cliente VALUES('{0}','{nome}','{cpf}','{telefone}','{endereco}','{email}')")
            cursor.execute("SELECT * FROM cliente")
            banco.commit()
            tabela = cursor.fetchmany()
            output=("CADASTRADO COM SUCESSO.")
            janela1['-OUTPUT-'].update(output)

        if eventos == sg.WINDOW_CLOSED:
            break

Tela()