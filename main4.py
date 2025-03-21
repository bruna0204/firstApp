import flet as ft
from flet.core import page


def main(page: ft.Page):

    # Configuração da pagina
    page.title = "Minha aplicação Flet"
    page.theme_mode = ft.ThemeMode.LIGHT # ou ft.ThemeModo.DARK
    page.window.width = 375
    page.window.height = 667

    # Definição de funçõe

    def soma(e):
        resultado = int(num1_input.value) + int(num2_input.value)
        txt_resultado.value = f'{resultado}'
        page.update()

    def subtracao(e):
        resultado = int(num1_input.value) - int(num2_input.value)
        txt_resultado.value = f'{resultado}'
        page.update()

    def multiplicacao(e):
        resultado = int(num1_input.value) * int(num2_input.value)
        txt_resultado.value = f'{resultado}'
        page.update()

    def divisao(e):
        resultado = int(num1_input.value) / int(num2_input.value)
        txt_resultado.value = f'{resultado}'
        page.update()



    # Criação de componentes
    num1_input = ft.TextField(label="numero1", hint_text="Digite um numero")
    num2_input = ft.TextField(label="numero2", hint_text="Digite um numero")
    btm_mais = ft.FilledButton(text="somar", width= page.window.width, on_click= soma)
    btm_menos = ft.FilledButton(text="subtrair", width= page.window.width, on_click= subtracao)
    btm_divisao = ft.FilledButton(text="divisao", width= page.window.width, on_click= divisao)
    btm_multiplicacao = ft.FilledButton(text="multiplicacao", width= page.window.width, on_click= multiplicacao)
    txt_resultado =ft.Text(value="")

    # Construir o layoute

    page.add(
        ft.Column(
            [
                num1_input,
                num2_input,
                btm_mais,
                btm_menos,
                btm_divisao,
                btm_multiplicacao,
                txt_resultado,
            ]
        )
    )

ft.app(main)

