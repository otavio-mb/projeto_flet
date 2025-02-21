import flet as ft


def configuracao(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER #Alinhamento Vertical
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER #Alinhamento Horizontal
    page.window.width = 800 #Largura
    page.window.height = 400 #Altura
    #page.window.resizable = False Redimensionavel
    page.theme_mode = ft.ThemeMode.DARK
    #page.add() #Adicionar widget
    #page.update() Atualizas página