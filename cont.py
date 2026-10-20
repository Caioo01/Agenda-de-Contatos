def adicionar_contatos (nome , telefone , email , favorito):
    contato = {'Nome' : nome, 'Telefone' : telefone, 'Email' : email, 'Favorito' : favorito}
    contatos.append(contato)
    print(f"Contato {nome} adicionado com sucesso!\n")
    return


def visualizar_contatos ():
     print(f"Lista de contatos: {contatos}\n")
     return


def favoritar_contato(resposta_favorita):
    for contato in contatos:
        if contato['Nome'] == resposta_favorita:
           contato['Favorito'] = True
           print(f"O contato {resposta_favorita} foi favoritado!\n")
        else:
            print("Esse contato não existe , digite novamente!")   


def editar_contato(contato_alterar):
    for contato in contatos:
        if contato['Nome'] == contato_alterar:
           dado_alterar = input("\nEscolha a opção de qual chave alterar 1-Nome / 2-Telefone / 3-Email / 4-Favorito: ")
           if dado_alterar == "1":
               nome_novo = input("Digite o novo nome: ")
               contato['Nome'] = nome_novo
               print("Nome de contato alterado!")
           elif dado_alterar == "2":
               telefone_novo = input("Digite o novo numero: ")
               contato['Telefone'] = telefone_novo
               print("Numero de telefone alterado!")
           elif dado_alterar == "3":
               email_novo = input("Digite o novo email: ")
               contato['Email'] = email_novo
               print("Novo email alterado!")
           elif dado_alterar == "4":
               while True: 
                favorito_novo = input("Digite Y-pra favoritar e N-pra tirar de favorito: ")   
                if favorito_novo == 'Y':
                   contato['Favorito'] = True
                   print("Contato favoritado!")
                   break
                elif favorito_novo == 'N':
                    contato['Favorito'] = False
                    print("Contato removido dos favoritos!")
                    break
                else:
                    print("Opção invalida!")    
        else: 
               print("Contato invalido!")              


def deletar_contato(contato_deletar):
    for contato in contatos:
      if contato['Nome'] == contato_deletar:
       contatos.remove(contato)
       print(f"Contato {contato_deletar} deletado!\n")
       break
      else:
        print("Contato não encontrado!")


def lista_favoritos():
    for contato in contatos:
     if contato['Favorito'] == True:
        print(contato)
     else:
         print("Sem contatos favoritados!")
      

contatos = []


while True:

    print("--------AGENDA--------")
    print("\n 1-Adicionar um Contato")
    print("\n 2-Visualizar contatos cadastrados")
    print("\n 3-Editar contato existente")
    print("\n 4-Favoritar contato")
    print("\n 5-Deletar contato")
    print("\n 6-Lista contatos favoritos")
    print("\n 7-Sair")

    opcao_escolhida = input("\nEscolha uma das opções: ")

    if opcao_escolhida == "1":
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o telefone: ")
            email = input("Digite o email: ")
            while True:
             resposta = input("Favoritar contato Y/N : ")

             if resposta == 'Y':
                 favorito = True
                 break
             elif resposta == 'N':
                 favorito = False
                 break
             else:
                  print("Digite novamente Y/N!")
            adicionar_contatos(nome, telefone, email, favorito) 


    if opcao_escolhida == "2":
         visualizar_contatos()      


    if opcao_escolhida == "3":
        print(contatos)
        contato_alterar = input("Digite qual contato alterar: ")
        editar_contato(contato_alterar)
     

    if opcao_escolhida == "4":
       print(contatos)
       resposta_favorita = input("Digite qual contato favoritar: ")
       favoritar_contato(resposta_favorita)


    if opcao_escolhida == "5":
       print(contatos)
       contato_deletar = input("Digite qual contato deletar: ")
       deletar_contato(contato_deletar)


    if opcao_escolhida == "6":
       lista_favoritos()


    if opcao_escolhida == "7":
        break