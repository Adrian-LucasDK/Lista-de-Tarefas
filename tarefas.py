
import tkinter as tk
from tkinter import messagebox


# Lista que armazenará as tarefas
tarefas = []


# Função para atualizar a lista na interface
def atualizar_lista():

    lista_tarefas.delete(0, tk.END)

    for indice, tarefa in enumerate(tarefas):

        if tarefa["concluida"]:
            status = "[CONCLUÍDA]"
        else:
            status = "[PENDENTE]"

        texto = f"{indice + 1}. {tarefa['descricao']} - {status}"

        lista_tarefas.insert(tk.END, texto)


# Função para adicionar uma tarefa
def adicionar_tarefa():

    descricao = campo_tarefa.get().strip()

    if not descricao:
        messagebox.showwarning(
            "Atenção",
            "Digite uma descrição para a tarefa."
        )
        return

    tarefa = {
        "descricao": descricao,
        "concluida": False
    }

    tarefas.append(tarefa)

    atualizar_lista()

    campo_tarefa.delete(0, tk.END)

    texto_status.config(
        text="Tarefa adicionada com sucesso!",
        fg="#65E6A5"
    )


# Função para concluir uma tarefa
def concluir_tarefa():

    selecao = lista_tarefas.curselection()

    if not selecao:
        messagebox.showwarning(
            "Atenção",
            "Selecione uma tarefa para concluir."
        )
        return

    indice = selecao[0]

    if tarefas[indice]["concluida"]:
        messagebox.showinfo(
            "Informação",
            "Esta tarefa já foi concluída."
        )
        return

    tarefas[indice]["concluida"] = True

    atualizar_lista()

    lista_tarefas.selection_set(indice)

    texto_status.config(
        text="Tarefa concluída com sucesso!",
        fg="#65E6A5"
    )


# Função para excluir uma tarefa
def excluir_tarefa():

    selecao = lista_tarefas.curselection()

    if not selecao:
        messagebox.showwarning(
            "Atenção",
            "Selecione uma tarefa para excluir."
        )
        return

    indice = selecao[0]

    descricao = tarefas[indice]["descricao"]

    confirmacao = messagebox.askyesno(
        "Confirmar exclusão",
        f"Deseja excluir a tarefa:\n\n{descricao}?"
    )

    if confirmacao:

        tarefas.pop(indice)

        atualizar_lista()

        texto_status.config(
            text="Tarefa excluída com sucesso!",
            fg="#65E6A5"
        )


# Função para limpar o campo de texto
def limpar_campo():

    campo_tarefa.delete(0, tk.END)

    texto_status.config(
        text="Campo de texto limpo.",
        fg="#B0B0B0"
    )


# Configuração da janela principal
janela = tk.Tk()
janela.title("Gerenciador de Tarefas")
janela.geometry("550x620")
janela.resizable(False, False)
janela.configure(bg="#20232A")


# Título
titulo = tk.Label(
    janela,
    text="GERENCIADOR DE TAREFAS",
    font=("Arial", 20, "bold"),
    bg="#20232A",
    fg="white"
)
titulo.pack(pady=(25, 5))


# Subtítulo
subtitulo = tk.Label(
    janela,
    text="Organize suas atividades de maneira simples",
    font=("Arial", 10),
    bg="#20232A",
    fg="#B0B0B0"
)
subtitulo.pack(pady=(0, 25))


# Área de cadastro
frame_cadastro = tk.Frame(
    janela,
    bg="#2D323C",
    padx=20,
    pady=20
)
frame_cadastro.pack(padx=30, fill="x")


tk.Label(
    frame_cadastro,
    text="Digite uma nova tarefa:",
    font=("Arial", 11, "bold"),
    bg="#2D323C",
    fg="white"
).pack(anchor="w", pady=(0, 10))


# Campo de entrada
campo_tarefa = tk.Entry(
    frame_cadastro,
    font=("Arial", 12),
    bg="#20232A",
    fg="white",
    insertbackground="white",
    relief="flat"
)
campo_tarefa.pack(fill="x", ipady=10)


# Botão adicionar
botao_adicionar = tk.Button(
    frame_cadastro,
    text="ADICIONAR TAREFA",
    font=("Arial", 10, "bold"),
    bg="#6C45D9",
    fg="white",
    activebackground="#5433B5",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=adicionar_tarefa
)
botao_adicionar.pack(fill="x", pady=(15, 0), ipady=9)


# Título da lista
tk.Label(
    janela,
    text="MINHAS TAREFAS",
    font=("Arial", 12, "bold"),
    bg="#20232A",
    fg="white"
).pack(pady=(25, 10))


# Área da lista com barra de rolagem
frame_lista = tk.Frame(
    janela,
    bg="#2D323C"
)
frame_lista.pack(padx=30, fill="both", expand=True)


lista_tarefas = tk.Listbox(
    frame_lista,
    font=("Arial", 11),
    bg="#2D323C",
    fg="white",
    selectbackground="#6C45D9",
    selectforeground="white",
    relief="flat",
    activestyle="none",
    height=8
)
lista_tarefas.pack(
    side="left",
    fill="both",
    expand=True,
    padx=10,
    pady=10
)


# Barra de rolagem
barra_rolagem = tk.Scrollbar(
    frame_lista,
    command=lista_tarefas.yview
)
barra_rolagem.pack(side="right", fill="y")

lista_tarefas.config(
    yscrollcommand=barra_rolagem.set
)


# Área dos botões de gerenciamento
frame_botoes = tk.Frame(
    janela,
    bg="#20232A"
)
frame_botoes.pack(padx=30, fill="x", pady=20)


# Botão concluir
botao_concluir = tk.Button(
    frame_botoes,
    text="CONCLUIR",
    font=("Arial", 9, "bold"),
    bg="#238B57",
    fg="white",
    activebackground="#176B40",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=concluir_tarefa
)
botao_concluir.pack(
    side="left",
    expand=True,
    fill="x",
    padx=5,
    ipady=10
)


# Botão excluir
botao_excluir = tk.Button(
    frame_botoes,
    text="EXCLUIR",
    font=("Arial", 9, "bold"),
    bg="#C74343",
    fg="white",
    activebackground="#A52E2E",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=excluir_tarefa
)
botao_excluir.pack(
    side="left",
    expand=True,
    fill="x",
    padx=5,
    ipady=10
)


# Botão limpar campo
botao_limpar = tk.Button(
    frame_botoes,
    text="LIMPAR CAMPO",
    font=("Arial", 9, "bold"),
    bg="#343A46",
    fg="white",
    activebackground="#454D5B",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=limpar_campo
)
botao_limpar.pack(
    side="left",
    expand=True,
    fill="x",
    padx=5,
    ipady=10
)


# Status do programa
texto_status = tk.Label(
    janela,
    text="Pronto para cadastrar tarefas.",
    font=("Arial", 9),
    bg="#20232A",
    fg="#B0B0B0"
)
texto_status.pack(pady=(0, 10))


# Rodapé
tk.Label(
    janela,
    text="Desenvolvido em Python com Tkinter",
    font=("Arial", 8),
    bg="#20232A",
    fg="#888888"
).pack(side="bottom", pady=10)


# Inicia a aplicação
janela.mainloop()
