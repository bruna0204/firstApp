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
                    AppBar(title=Text("home"), bgcolor=Colors.PRIMARY_CONTAINER),
                    ElevatedButton(text="Navegar", on_click=lambda _: page.go("/segunda")),
                ],
            )
        )
        if page.route == "/segunda":
            page.views.append(
                View(
                    "/segunda",
                    [
                        AppBar(title=Text("Segunda tela"), bgcolor=Colors.PRIMARY_CONTAINER),

                    ],
                )
            )
        page.update()

    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = gerenciar_rotas
    page.on_view_pop = voltar
    page.go(page.route)

ft.app(main)
