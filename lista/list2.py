import flet as ft
from flet import AppBar, Text, View
from flet.core.colors import Colors

class User():
    def __init__(self, titulo, descrisao, categoria, autor):
        self.titulo = titulo
        self.descrisao = descrisao
        self.categoria = categoria
        self.autor = autor

def main(page: ft.Page):
    # Configurações
    page.title = "Exemplos de listas"
    page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    # Funções
    lista = []
    def salvar_dados(e):
        if input_titulo.value == "" or input_autor.value == "" or input_descricao.value == "" or input_categoria.value == "":
            page.overlay.append(msg_erro)
            msg_erro.open = True
            page.update()

        else:
            obj_user = User(
                titulo = input_titulo.value,
                descrisao = input_descricao.value,
                categoria = input_categoria.value,
                autor = input_autor.value,
            )
            lista.append(obj_user)
            input_titulo.value = ""
            input_descricao.value = ""
            input_categoria.value = ""
            input_autor.value = ""
            page.overlay.append(msg_sucesso)
            msg_sucesso.open = True
            page.update()

    def exibir_lista(e):
        lv_dados.controls.clear()
        for user in lista:
            lv_dados.controls.append(
                ft.Text(value= f"{user.titulo} - {user.descrisao} - {user.categoria} - {user.autor}")
            )
        page.update()
    def gerencia_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Home"), bgcolor=Colors.PRIMARY_CONTAINER),
                    input_titulo,
                    input_descricao,
                    input_categoria,
                    input_autor,
                    ft.Button(
                        text='salvar',
                        on_click=lambda _: salvar_dados(e)
                    ),
                    ft.Button(
                        text='exibir lista',
                        on_click= lambda _: page.go("/segunda"),
                    )
                ],
            )
        )
        if page.route == "/segunda":
            exibir_lista(e)
            page.views.append(
                View(
                    "/segunda",
                    [
                        AppBar(title=Text("Segunda tela"), bgcolor=Colors.SECONDARY_CONTAINER),
                        lv_dados,

                    ],
                )
            )
        page.update()

    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)


    # Componentes
    msg_sucesso = ft.SnackBar(
        content= ft.Text("Nome salvo com sucesso"),
        bgcolor=Colors.GREEN
                              )

    msg_erro = ft.SnackBar(
        content=ft.Text("ERRO"),
        bgcolor=Colors.RED
    )

    input_titulo = ft.TextField(label="titulo", hint_text="Digite o titulo")
    input_descricao = ft.TextField(label="descricao", hint_text="Digite a descricao")
    input_categoria = ft.TextField(label="categoria", hint_text="Digite a categoria")
    input_autor = ft.TextField(label="autor", hint_text="Digite o autor")
    btn_salvar = ft.Button(text="Salvar")
    lv_dados = ft.ListView(
        height=500
    )



    # Eventos
    page.on_route_change = gerencia_rotas
    page.on_view_pop = voltar

    page.go(page.route)

# Comando que executa o aplicativo
# Deve estar sempre colado na linha
ft.app(main)
