import flet as ft
from flet.core import page


def main(page: ft.Page):

    # Configuração da pagina
    page.title = "Minha aplicação Flet"
    page.theme_mode = ft.ThemeMode.LIGHT # ou ft.ThemeModo.DARK
    page.window.width = 375
    page.window.height = 667

    # Definição de funçõe

    def mostrar_valor(e):
        num1_input.value = int(num1_input.value)
        verificar = num1_input.value % 2
        if verificar == 0:
            txt_resultado.value = 'Esse numero é par'
            page.update()

        else:
            txt_resultado.value = 'Esse numero é impar'
            page.update()


    # Criação de componentes
    num1_input = ft.TextField(label="numero", hint_text="Digite um numero")
    btm_enviar = ft.FilledButton(text="Enviar", width= page.window.width, on_click=mostrar_valor)
    txt_resultado =ft.Text(value="")

    # Construir o layoute

    page.add(
        ft.Column(
            [
                num1_input,
                btm_enviar,
                txt_resultado,
            ]
        )
    )

ft.app(main)

