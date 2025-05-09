import flet as ft
from flet.core.app_bar import AppBar
from flet.core.border_radius import horizontal
from flet.core.colors import Colors
from flet.core.dropdown import Option
from flet.core.elevated_button import ElevatedButton
from flet.core.text import Text
from flet.core.types import CrossAxisAlignment, MainAxisAlignment
from flet.core.view import View
import datetime
from datetime import datetime


def main(page: ft.Page):
    # Configuração da pagina
    page.title = "Exemplo de Rotas"
    page.theme_mode = ft.ThemeMode.LIGHT  # ou ft.ThemeModo.DARK
    page.window.width = 375
    page.window.height = 667

    # função para gerenciar as telas
    def gerenciar_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(
                        title=Text("Pagina inicial"), bgcolor=Colors.PRIMARY_CONTAINER),
                    ft.Container(
                        ft.Image(src="../INSS_app/images-removebg-preview.png"),
                        margin=50,
                    ),
                    ft.Container(
                        ft.Column(
                            [
                                ElevatedButton(text="Simular", width=300, on_click=lambda _: page.go("/simular")),
                                ElevatedButton(text="regras", width=300, on_click=lambda _: page.go("/regras")),
                            ],

                        ),


                    ),

                ],
                bgcolor=Colors.INDIGO_900,
                horizontal_alignment = CrossAxisAlignment.CENTER,
            ),
        )
        if page.route == "/regras":
            page.views.append(
                View(
                    "/regras",
                    [
                        AppBar(title=Text("Regras"), bgcolor=Colors.PRIMARY_CONTAINER),
                        Text(theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM, value=f"Regras Básicas de Aposentadoria: "),
                        Text(theme_style=ft.TextThemeStyle.TITLE_LARGE,value=f"Aposentadoria por Idade"),
                        Text(theme_style=ft.TextThemeStyle.BODY_LARGE,value=f"Homens: 65 anos de idade e pelo menos 15 anos de contribuição.\n"
                                   f"Mulheres: 62 anos de idade e pelo menos 15 anos de contribuição.\n  "),
                        Text(theme_style=ft.TextThemeStyle.TITLE_LARGE,value=f"Aposentadoria por Tempo de Contribuição"),
                        Text(theme_style=ft.TextThemeStyle.BODY_LARGE,value=f"Homens: 35 anos de contribuição.\n"
                                   f"Mulheres: 30 anos de contribuição. "),
                        Text(theme_style=ft.TextThemeStyle.TITLE_MEDIUM,value=f"Valor Estimado do Benefício: O valor da aposentadoria será uma média de 60%\n"
                                   f" da média salarial informada, acrescido de 2% por ano que exceder o tempo mínimo\n"
                                   f" de contribuição "),
                    ],
                    bgcolor=Colors.BLUE_100
                ),
            )


        elif page.route == "/simular":
            page.views.append(
                View(
                    "/simular",
                    [
                        AppBar(title=Text("Entradas do usuario"), bgcolor=Colors.PRIMARY_CONTAINER),
                        ft.Container(

                            margin=20,
                            padding=10,
                            alignment=ft.alignment.center,
                            bgcolor=ft.Colors.WHITE,
                            width=400,
                            height=490,
                            content= ft.Column(

                                [
                                    input_idade,
                                    input_gen,
                                    input_tempo,
                                    input_media_salarial,
                                    input_categori,
                                    ElevatedButton(text="enviar", bgcolor= Colors.BLACK, color= ft.Colors.WHITE, width= 400, on_click=lambda _: page.go("/contas")),

                                ],



                            ),




                        ),


                    ],
                    bgcolor=Colors.BLUE

                )

            )
        elif page.route == "/contas":

            idade = int(input_idade.value)
            tempo = int(input_tempo.value)
            media_salarial = int(input_media_salarial.value)
            salario = media_salarial * 60
            resultado = salario / 100

            anos = datetime.now().year
            print(anos)

            if not idade:
                idade.error = True
                idade.error_text = "PREENCHA ESSE CAMPO"
                page.update()

            if not tempo:
                tempo.error = True
                tempo.error_text = "PREENCHA ESSE CAMPO"
                page.update()

            if not media_salarial   :
                media_salarial.error = True
                media_salarial.error_text = "PREENCHA ESSE CAMPO"
                page.update()


            if input_categori.value == "idade":
                if input_gen.value == "feminino":
                    if idade >= 62 and tempo >= 15:
                        txt_resultad.value = "Voce pode se aposentar"
                        if tempo > 15:
                            conta = tempo - 15
                            porcentagem = media_salarial * 2
                            final = porcentagem / 100
                            ultima = final * conta
                            resultado_final = resultado + ultima
                            salaro_resultad.value = f"seu beneficio é {resultado_final}"
                        elif tempo == 15:
                            salaro_resultad.value = f"seu beneficio é {resultado}"

                    elif idade >= 62 and tempo < 15:
                        txt_resultad.value = "voce nao pode se aposentar pela idade por conta do tempo de contribuição"
                        conta = 15 - tempo
                        final = conta + anos
                        tempo_resultad.value = f"Voce vai atingir o tempo minimo de contribuição  em {final}"

                    elif idade < 62 and tempo >= 15:
                        txt_resultad.value = "voce nao pode se aposentar por conta da idade"
                        conta = 62 - idade
                        final = conta + anos
                        anos_resultad.value = f"Voce vai se aposentar em {final}"

                    else:
                        txt_resultad.value = "Voce não consegue se aposentar, pois vc não tem idade o suficiente e tempo de contribuiçao não suficiente"
                        conta = 15 - tempo
                        final = conta + anos
                        tempo_resultad.value = f"Voce vai atingir o tempo minimo de contribuição  em {final}"

                        conta = 62 - idade
                        final_idade = conta + anos
                        anos_resultad.value = f"Voce vai se aposentar em {final_idade}"
                else:
                    if idade >= 65 and tempo >= 15:
                        txt_resultad.value = "Voce pode se aposentar"
                        if tempo > 15:
                            conta = tempo - 15
                            porcentagem = media_salarial * 2
                            final = porcentagem / 100
                            ultima = final * conta
                            resultado_final = resultado + ultima
                            salaro_resultad.value = f"seu beneficio é {resultado_final}"
                        elif tempo == 15:
                            salaro_resultad.value = f"seu beneficio é {resultado}"

                    elif idade >= 65 and tempo < 15:
                        txt_resultad.value = "voce nao pode se aposentar pela idade por conta do tempo de contribuição"
                        conta = 15 - tempo
                        final = conta + anos
                        tempo_resultad.value = f"Voce vai atingir o tempo minimo de contribuição  em {final}"

                    elif idade <= 65 and tempo >= 15:
                        txt_resultad.value = "voce nao pode se aposentar por conta da idade"
                        conta = 65 - idade
                        final = conta + anos
                        anos_resultad.value = f"Voce vai se aposentar em {final}"

                    else:
                        txt_resultad.value = "Voce não consegue se aposentar, pois vc não tem idede o suficiente e tempo de contribuiçao não suficiente"
                        conta = 15 - tempo
                        final = conta + anos
                        tempo_resultad.value = f"Voce vai atingir o tempo minimo de contribuição  em {final}"

                        conta = 65 - idade
                        final_idade = conta + anos
                        anos_resultad.value = f"Voce vai se aposentar em {final_idade}"

            else:
                if input_gen.value == "feminino":
                    if tempo >= 30:
                        txt_resultad.value = "Voce pode se aposentar"
                        if tempo == 30:
                            conta = 30 - 15
                            porcentagem = media_salarial * 2
                            final = porcentagem / 100
                            ultima = final * conta
                            resultado_final = resultado + ultima
                            salaro_resultad.value = f"seu beneficio é {resultado_final}"

                        elif tempo > 30:

                            conta = tempo - 15
                            porcentagem = media_salarial * 2
                            final = porcentagem / 100
                            ultima = final * conta
                            resultado_final = resultado + ultima
                            salaro_resultad.value = f"seu beneficio é {resultado_final}"

                    else:
                        txt_resultad.value = "voce não tem tempo de contribuição o suficiente, portanto não pode se aposentar por contribuição"
                        conta = tempo - 15
                        final = conta + anos
                        tempo_resultad.value = f"Voce vai atingir o tempo minimo de contribuição  em {final}"
                else:
                    if tempo > 35:
                        txt_resultad.value = "Voce pode se aposentar"
                        if tempo == 35:
                            conta = 35 - 15
                            porcentagem = media_salarial * 2
                            final = porcentagem / 100
                            ultima = final * conta
                            resultado_final = resultado + ultima
                            salaro_resultad.value = f"seu beneficio é {resultado_final}"
                        elif tempo > 35:
                            conta = tempo - 15
                            porcentagem = media_salarial * 2
                            final = porcentagem / 100
                            ultima = final * conta
                            resultado_final = resultado + ultima
                            salaro_resultad.value = f"seu beneficio é {resultado_final}"

                    else:
                        txt_resultad.value = "voce não tem tempo de contribuição o suficiente, portanto não pode se aposentar"
                        conta = tempo - 35
                        final = conta + anos
                        tempo_resultad.value = f"Voce vai atingir o tempo minimo de contribuição  em {final}"

            page.views.append(
                View(
                    "/contas",
                    [
                        AppBar(title=Text("rewsultado"), bgcolor=Colors.PRIMARY_CONTAINER),
                        Text(theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM, color= ft.Colors.WHITE, value=f"Resultado final:"),
                        ft.Container(
                            margin=20,
                            padding=10,
                            alignment=ft.alignment.center,
                            bgcolor=ft.Colors.WHITE,
                            width=400,
                            height=350,
                            content=ft.Column(
                                [

                                    txt_resultad,
                                    salaro_resultad,
                                    anos_resultad,
                                    tempo_resultad,
                                ]
                            )

                        )

                    ],
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    bgcolor= ft.Colors.BLUE_ACCENT_200,
                )
            )
        page.update()

    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    txt_resultad = ft.Text(value="")
    salaro_resultad = ft.Text(value="")
    anos_resultad = ft.Text(value="")
    tempo_resultad = ft.Text(value="")

    input_idade = ft.TextField(label="Idade", width= 400, hint_text="informe sua idade")
    input_tempo = ft.TextField(label="Tempo de contribuição", width= 400, hint_text="informe o tempo de contribuição")
    input_media_salarial = ft.TextField(label="Média salarial", width= 400,
                                        hint_text="media salarial(pelo menos dos ultimos 5 anos de contribuição)")

    input_categori = ft.Dropdown(label="Categoria da aposentadoria", width= 400, options=[Option(key="idade", text="Idade"),
                                                                              Option(key="tempo",
                                                                                     text="Tempo de contribuicão") ])
    input_gen = ft.Dropdown(label="Genero", width= 400,
                            options=[Option(key="masculino", text="Homem"), Option(key="feminino", text="Mulher"), ])

    page.on_route_change = gerenciar_rotas
    page.on_view_pop = voltar

    page.go(page.route)


ft.app(main)
