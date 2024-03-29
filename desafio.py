def adicionar_contato(contatos):
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite o email: ")
    is_favorite = int(input("é um contato favorito? digite 1 - sim e 2 - não: "))

    contatos.append({
        "nome": nome, 
        "telefone": telefone, 
        "email": email, 
        "is_favorite": True if is_favorite == 1 else False 
    })

def visualizar_contatos(contatos):
    print("\nLista de contatos")
    for index, contato in enumerate(contatos, start = 1):
        star_favorited = "🌟" if contato["is_favorite"] else " "
        print(f"{index}. {contato['nome']}, {contato['email']}, {contato['telefone']} {star_favorited}")

def editar_contato(contatos):
    index_editar = int(input("Digite o numero do contato que deseja editar: "))
    novo_nome = input("Digite o novo nome: ")
    novo_email = input("Digite o novo email: ")
    novo_telefone = input("Digite o novo telefone: ")

    contatos[index_editar - 1]["nome"] = novo_nome
    contatos[index_editar - 1]["email"] = novo_email
    contatos[index_editar - 1]["telefone"] = novo_telefone

def tougle_favorite(contatos):
    index_favorito = int(input("digite o numero do contato que deseja favoritar/tirar do favorito: ")) - 1
    contatos[index_favorito]["is_favorite"] = False if contatos[index_favorito]["is_favorite"] == True else True

def visualizar_favoritos(contatos):
    print("\n🌟 Sua lista de favoritos 🌟")
    for contato in contatos:
        if contato['is_favorite']:  print(f"{contato['nome']}, {contato['email']}, {contato['telefone']}")

def remover_contato(contatos):
    index_remove = int(input("digite o numero do contato que deseja remover da lista: ")) - 1
    contatos.remove(contatos[index_remove])

contatos = []
while True:
    print("\nMenu")
    print("1. Adicionar um contato")
    print("2. Vizualizar contatos")
    print("3. Editar contato")
    print("4. Marcar contato como favorito")
    print("5. Ver lista de favoritos")
    print("6. Apagar contato")
    print("7. Sair")

    escolha = input("Digite a sua escolha: ")

    if(escolha == "1"):
        adicionar_contato(contatos)
    if(escolha == "2"):
        visualizar_contatos(contatos)
    if(escolha == "3"):
        visualizar_contatos(contatos)
        editar_contato(contatos)
    if(escolha == "4"):
        visualizar_contatos(contatos)
        tougle_favorite(contatos)
    if(escolha == "5"):
        visualizar_favoritos(contatos)
    if(escolha == "6"):
        visualizar_contatos(contatos)
        remover_contato(contatos)
    if(escolha == "7"):
        break