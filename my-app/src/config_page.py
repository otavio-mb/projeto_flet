import flet as ft
import time
import os

def main(page: ft.Page): # função principal
    # Configuração de Janela

    page.title = 'Configuração da Página' # título da página
    page.theme_mode = ft.ThemeMode.DARK 

    page.window.width = 300
    page.window.height = 600
    page.window.center()
    # Check if font file exists
    if os.path.exists('src/assets/fonts/guns.ttf'):
        print("Font file found.")
    else:
        print("Font file not found.")
    
    page.fonts = {'Guns': 'src/assets/fonts/guns.ttf'}
    
    def janela_evento(e):
        match e.data:
            case 'moved':
                print('Janela movida')
            case 'resized':
                print('Janela redimensionada')
            case 'minimize':
                print('Janela minimizada')
            case _:
                print('Outra ação')

    page.window.on_event = janela_evento

    #page.window.always_on_top = True

    # Alinhamento
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    #page.padding = ft.padding.all(10)
    #page.padding = ft.padding.only(left=10, right=10, top=10, bottom=10)
    #page.spacing = 100

    var = 0.5

    while True:
        time.sleep(0.01)
        var += 0.5
        page.window.width += var
        page.update()
        if page.window.width >= 900:
            break
    #page.window.resizable = False

    def alterar_tema(e):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
            btn_tema.icon = ft.icons.SIGNAL_WIFI_0_BAR_OUTLINED
            btn_tema.tooltip = 'Alterar Tema para escuro'
            page.bgcolor = ft.Colors.WHITE
        else:
            page.theme_mode = ft.ThemeMode.DARK
            btn_tema.icon = ft.icons.SIGNAL_WIFI_4_BAR_OUTLINED
            btn_tema.tooltip = 'Alterar Tema para claro'
            page.bgcolor = ft.Colors.BLACK
        page.update()
        
    btn_tema = ft.IconButton(icon=ft.icons.SIGNAL_WIFI_4_BAR_OUTLINED, tooltip='Alterar Tema', on_click=alterar_tema) # cria um botão que executa a função alterar_tema

    t = ft.Text('hello world',
                size=50,
                font_family='Guns',
                color='blue',
                italic=False,
                ) # cria um texto

    elementos = [ # lista de elementos
        ft.Text(
            value='Texto 1',
            size=20,
            color=ft.Colors.RED_300,
            bgcolor=ft.Colors.AMBER_100,
            font_family='Guns'),
        ft.Text(
            value='Texto 2',
            size=20,
            color=ft.Colors.RED_300,
            bgcolor=ft.Colors.AMBER_100,
            font_family='Guns'),
        ft.Text(
            value='Texto 3',
            size=20,
            color=ft.Colors.RED_300,
            bgcolor=ft.Colors.AMBER_100,
            font_family='Guns'),
    ]

    page.add(t, btn_tema, *elementos) # adiciona um widget/elemento

ft.app(main, assets_dir="assets") # inicia a aplicação