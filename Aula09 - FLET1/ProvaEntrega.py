import flet as ft

def main(page: ft.Page):
    page.title = "Lista de Tarefas"
    campo_tarefa = ft.TextField(label="Digite uma tarefa", width=300)
    lista_tarefas = ft.Column()

    def adicionar_tarefa(e):
        if campo_tarefa.value.strip():
            lista_tarefas.controls.append(ft.Text(f"• {campo_tarefa.value}"))
            campo_tarefa.value = ""
            page.update()

    page.add(
        ft.Text("Lista de Tarefas", size=24, weight=ft.FontWeight.BOLD),
        campo_tarefa,
        ft.ElevatedButton("Adicionar", on_click=adicionar_tarefa),
        ft.Divider(),
        lista_tarefas
    )

ft.app(target=main)

