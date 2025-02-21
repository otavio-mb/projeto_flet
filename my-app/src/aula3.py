import config
import flet as ft
def main(page: ft.Page):

    config.configuracao(page)

    page.title = 'Minha Página'
    def adicionar(e):
        if not nova_tarefa.value:
            nova_tarefa.error_text = "Por favor, digite"
            nova_tarefa.update()
        else:
            nova_tarefa.error_text = None

            tarefa = ft.Row([])
            checkbox = ft.Checkbox(label=nova_tarefa.value)

            btn_editar = ft.IconButton(
                icon=ft.icons.EDIT,
                tooltip='Editar Tarefa'
            )

            botao_remover = ft.IconButton(icon=ft.icons.DELETE_OUTLINED,
                                          tooltip='Remover tarefa',
                                          on_click= lambda e: remover_tarefa(tarefa)
                                          )
            tarefa.controls.extend([checkbox, botao_remover, btn_editar])
            page.add(tarefa)
            nova_tarefa.value = ''
            nova_tarefa.focus()
            nova_tarefa.update()        
    

    def remover_tarefa(tarefa):
        page.controls.remove(tarefa)
        page.update()

    def saudacao(e):
        if not txt_nome.value:
            txt_nome.error_text = "Por favor, digite"
            page.update()
        else:
            nome = txt_nome.value
            page.clean()
            page.add(ft.Text(f"Olá {nome}!"))

    txt_nome = ft.TextField(label="Seu nome?")
    nova_tarefa=ft.TextField(hint_text="O que você deseja adicionar?", width=300)

    def clicar(e):
        saida_texto.value = f'Valor Dropdown is: {color_dropdown.value}'
        page.update()

    
    saida_texto = ft.Text()
    submit_btn = ft.ElevatedButton(text='Submit', on_click=clicar)
    color_dropdown = ft.Dropdown(
        width=200,
        options=[
            ft.dropdown.Option("Red"),
            ft.dropdown.Option("Green"),
            ft.dropdown.Option("Blue"),
            ft.dropdown.Option("Minha Opção"),
        ],
    )
    page.add(color_dropdown, submit_btn, saida_texto)


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

    page.add(ft.Row(
        [
            nova_tarefa,
            ft.ElevatedButton('Adicionar', on_click=adicionar),
            btn_tema,
        ]
    ))
    
    txt_nome = ft.TextField(label='Qual seu nome?')
    page.add(txt_nome, ft.ElevatedButton('Diga ola!', on_click=saudacao))

ft.app(main)