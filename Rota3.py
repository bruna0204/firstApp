import flet as ft
from flet.core import page
from flet.core.app_bar import AppBar
from flet.core.colors import Colors
from flet.core.elevated_button import ElevatedButton
from flet.core.text import Text
from flet.core.view import View


def main(page: ft.Page):

    # Configuração da pagina
    page.title = "Exemplo de Rotas"
    page.theme_mode = ft.ThemeMode.LIGHT # ou ft.ThemeModo.DARK
    page.window.width = 375
    page.window.height = 667


    #função para gerenciar as telas
    def gerenciar_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Cadastro de livros"), bgcolor=Colors.PRIMARY_CONTAINER),
                    input_titulo,
                    input_descricao,
                    input_categoria,
                    input_autor,
                    ElevatedButton(text="enviar", on_click=lambda _: page.go("/segunda")),
                ],
            )
        )
        if page.route == "/segunda":
            page.views.append(
                View(
                    "/segunda",
                    [
                        AppBar(title=Text("Segunda tela"), bgcolor=Colors.PRIMARY_CONTAINER),
                        Text(value= f"Titulo: {input_titulo.value}"),
                        Text(value= f"Descrição:  {input_descricao.value}"),
                        Text(value= f"Categoria: {input_categoria.value}"),
                        Text(value= f"Autor: {input_autor.value}")

                    ],
                )
            )


        page.update()

    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    input_titulo = ft.TextField(label="titulo", hint_text="Digite o titulo")
    input_descricao = ft.TextField(label="descricao", hint_text="Digite a descricao")
    input_categoria = ft.TextField(label="categoria", hint_text="Digite a categoria")
    input_autor = ft.TextField(label="autor", hint_text="Digite o autor")
    txt_resultado = ft.Text(value="")

    page.on_route_change = gerenciar_rotas
    page.on_view_pop = voltar
    page.go(page.route)

ft.app(main)
