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

    def exibir_dados(e):
        lv.controls.clear()
        for user in lista:
            lv.controls.append(
                ft.Text(value= f"Titulo: {user.titulo}\n"
                               f"Descrisao: {user.descrisao}\n"
                               f"Categoria: {user.categoria}\n"
                               f"Autor: {user.autor}\n")
            )
        page.update()

    def vizualiza_dados(e):
        lv.controls.clear()
        for user in lista:
            lv.controls.append(
                ft.ListTile(
                    leading=ft.Icon(ft.Icons.PERSON),
                    title=ft.Text(f"Titulo: {user.titulo}"),
                    trailing=ft.PopupMenuButton(
                        icon=ft.Icons.MORE_VERT,
                        items=[
                            ft.PopupMenuItem(text=f"detalhes", on_click=lambda _: page.go("/terceira")),
                        ]
                    )
                )
            )



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
            vizualiza_dados(e)
            page.views.append(
                View(
                    "/segunda",
                    [
                        AppBar(title=Text("Segunda tela"), bgcolor=Colors.SECONDARY_CONTAINER),
                        lv

                    ],
                )
            )
        if page.route == "/terceira":
            exibir_dados(e)
            page.views.append(
                View(
                    "/terceira",
                    [
                        AppBar(title=Text("detalhes"), bgcolor=Colors.SECONDARY_CONTAINER),
                        lv
                    ],
                )
            )
        page.update()

    page.on_route_changed = gerencia_rotas
    page.go(page.route)

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
    lv = ft.ListView(
        height=500
    )



    # Eventos
    page.on_route_change = gerencia_rotas
    page.on_view_pop = voltar

    page.go(page.route)

# Comando que executa o aplicativo
# Deve estar sempre colado na linha
ft.app(main)
