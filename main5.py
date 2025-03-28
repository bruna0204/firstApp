import flet as ft
import datetime
from flet.core import page
from oauthlib.common import add_params_to_uri


def main(page: ft.Page):
    # Configuração da pagina
    page.title = "Minha aplicação Flet"
    page.theme_mode = ft.ThemeMode.LIGHT # ou ft.ThemeModo.DARK
    page.window.width = 375
    page.window.height = 667

    # Definição de funçõe

    def calcular_idade(e):
        tempo_atual = datetime.datetime.now()
        data_informada = datetime.datetime.strptime(data.value, '%d-%m-%Y')
        idade_atual = tempo_atual.year - data_informada.year
        if idade_atual < 18:
            txt_resultado.value = f' você é menor de idade'
            page.update()
        elif idade_atual > 110:
            txt_resultado.value = f'Essa pessoa não existe'

        else:
            txt_resultado.value = f' você é maior de idade'
            page.update()






    # Criação de componentes
    data = ft.TextField(label="data", hint_text="Digite a data do seu nascimento")
    enviar = ft.FilledButton(text="enviar", width= page.window.width, on_click= calcular_idade)
    txt_resultado =ft.Text(value="")

    # Construir o layoute

    page.add(
        ft.Column(
            [
                data,
                enviar,
                txt_resultado,
            ]
        )
    )

ft.app(main)

