import flet as ft

def main(page: ft.Page):
    page.title = 'Primeiro app flet'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    num1 = ft.TextField(value = '0', text_align=ft.TextAlign.CENTER)

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

    def menos(e):
        num1.value = str(int(num1.value) - 1)
        page.update()

    def mais(e):
        num1.value = str(int(num1.value) + 1)
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.ADD, on_click=mais),
                num1,
                ft.IconButton(ft.icons.REMOVE, on_click=menos),
                btn_tema
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

ft.app(main)