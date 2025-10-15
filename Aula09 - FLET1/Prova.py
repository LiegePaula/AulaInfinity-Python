import flet as ft

def main(page: ft.Page):
    page.title = "Lista de Tarefas"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    
    campo_tarefa = ft.TextField(
        label="Digite uma tarefa",
        width=300,
        autofocus=True
    )

   
    lista_tarefas = ft.Column()

    
    def adicionar_tarefa(e):
        if campo_tarefa.value.strip() != "":
            
            nova_tarefa = ft.Text(f"• {campo_tarefa.value}")
            lista_tarefas.controls.append(nova_tarefa)
            
            campo_tarefa.value = ""
            
            page.update()

    
    botao_adicionar = ft.ElevatedButton(
        "Adicionar",
        on_click=adicionar_tarefa
    )

    
    page.add(
        ft.Text("Lista de Tarefas", size=24, weight=ft.FontWeight.BOLD),
        campo_tarefa,
        botao_adicionar,
        ft.Divider(),
        lista_tarefas
    )


ft.app(target=main)
