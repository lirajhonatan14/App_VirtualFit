import flet as ft #importando flet
from models import Users
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

CONN = "sqlite:///projeto2.db"

engine = create_engine(CONN, echo = True)
Session = sessionmaker(bind=engine)
session = Session()


def highlight_link(e): #essa função controla a cor do botao para blue se o curso n estiver nele
        e.control.style.color = ft.colors.BLUE
        e.control.update()

def unhighlight_link(e):#essa função altera a cor para preto quando o cursor passa por cima
    e.control.style.color = None
    e.control.update()


def main(page: ft.Page): # define função main que é a interface
    page.title = "Cadastro" #nome da janela

    list_users = ft.ListView()

    def cadastrar(e):
        try:
            novo_user = Users(user=input_user.value, name=input_name.value, passwd=input_password.value)
            session.add(novo_user)
            session.commit()
            list_users.controls.append(ft.Text(input_name.value))
            txt_erro.visible = False
            txt_granted.visible = True
            page.update()
        except:
            txt_erro.visible = True
            txt_granted.visible = False
    txt_erro = ft.Container(ft.Text('Erro ao salvar o usuario!'), visible=False, bgcolor=ft.colors.RED)
    txt_granted = ft.Container(ft.Text('Salvo com Sucesso!'), visible=False, bgcolor=ft.colors.GREEN)


    txt_title = ft.Text("VirtualFit")
    txt_user = ft.Text('Nome de Usuario: ') #texto qlqr na tela, mas esse é o usuario
    input_user = ft.TextField(label="Digite seu nome de usuario...", text_align=ft.TextAlign.LEFT)#input onde o usuario escrevera
    txt_name = ft.Text('Nome: ')#texto pedindo nome 
    input_name = ft.TextField(label="Digite seu nome...", text_align=ft.TextAlign.LEFT) #input para o nome 
    btn_user = ft.ElevatedButton('Cadastrar', on_click=cadastrar) #botao para cadastrar
    txt_password = ft.Text("Senha: ") #texto para senha
    input_password = ft.TextField(label="Digite sua senha...", password=True)#input para senha



    page.add( #adicionando os elementos na tela
        txt_granted,
        txt_erro,
        txt_title,#adicionando o nome do app
        txt_name,#adicionando o texto nome
        input_name, #adicionando o input nome completo
        txt_user, #variavel de texto
        input_user, #adicionando o input a janela
        txt_password, #adicionando o texto do password 
        input_password,#adicionando o input do password
        
        ft.Text( # essas linhas de codigo definem para o texto nomel, e o hipertexto, que possui um link nele
            disabled=False,
            spans=[
                ft.TextSpan("Caso já possua login, clique "),
                ft.TextSpan(
                    "Aqui",
                    ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE),
                    url="https://google.com",
                    on_enter=highlight_link,
                    on_exit=unhighlight_link,
                ),
            ],
        ),
    
        btn_user, #adicionando botao a janela
    )

    for p in session.query(Users).all():
        list_users.controls.append(
            ft.Container(
                ft.Text(p.name),
                bgcolor=ft.colors.BLACK12,
                alignment=ft.alignment.center,

                )
        )

    page.add(
        list_users,
    )


ft.app(target=main) #interface chamada main