import flet as ft

def main(page: ft.Page):
    page.title = "Formulário de Contato"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

   
    nome = ft.TextField(label="Nome", width=300)
    email = ft.TextField(label="E-mail", width=300)
    mensagem = ft.TextField(label="Mensagem", multiline=True, width=300, height=100)

    
    confirmacao = ft.Text("", color="green", weight=ft.FontWeight.BOLD)

   
    def enviar_formulario(e):
        if not nome.value or not email.value or not mensagem.value:
            confirmacao.value = "Por favor, preencha todos os campos."
            confirmacao.color = "red"
        else:
            confirmacao.value = f"Obrigado, {nome.value}! Seu formulário foi enviado com sucesso."
            confirmacao.color = "green"
           
            nome.value = ""
            email.value = ""
            mensagem.value = ""
        page.update()

  
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_formulario)

   
    page.add(
        ft.Text(" Formulário de Contato", size=24, weight=ft.FontWeight.BOLD),
        nome,
        email,
        mensagem,
        botao_enviar,
        confirmacao
    )


ft.app(target=main)
