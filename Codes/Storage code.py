estoque = {}

while True:

    print("\n1 - Visualizar Estoque Atual")
    print("2 - Registrar Entrada de Produto")
    print("3 - Registrar Saída de Produto")
    print("4 - Sair do Sistema")

    choice = input("\nEscolha:")

    if choice == "2":

        name = input("\nProduto:").capitalize()
        quantidade = int(input("Quantidade:"))

        if not name in estoque:
            yesorno = input("\ndeseja adicionar no estoque?s/n")

            if yesorno == "s":
                price = float(input("Qual o valor:"))
                estoque[name] = quantidade
                estoque[name] = price

            elif yesorno == "n":
                print("\nVoltando ao Menu....")
                continue

            else:
                print("\nInválido")
                continue

            estoque[name] = {
                "quantidade": quantidade,
                "preço": price
            }

        else:
            estoque[name]["quantidade"] += quantidade


    elif choice == "3":

        name = input("\nProduto:").capitalize()
        minus = int(input("Quantidade:"))

        if name in estoque:
            if minus > estoque[name]["quantidade"]:
                print("\nEstoque insuficiente")

            elif minus == estoque[name]["quantidade"]:
                decision = input("Deseja remove-lo do estoque?s/n")
                estoque[name]["quantidade"] -= minus

                if decision == "s":
                    del estoque[name]
                    print(f"{name} removido com sucesso")
                    print("\nEstoque atualizado")

                elif decision == "n":
                    print(f"\nProduto {name} ficará classificado como 'fora de estoque'")

                else:
                    continue


            else:
                estoque[name]["quantidade"] -= minus
                print("\nEstoque atualizado")

        else:
            print("\nproduto indisponivel")



    elif choice == "1":
        print("\n=====Verificando Estoque=====")

        if not estoque:
            print("\nEstoque Vazio")

        else:
            for name, info in estoque.items():

                if estoque[name]["quantidade"] == 0:
                    print(f"\nProduto:{name} - FORA DE ESTOQUE")
                    print(f"    Quantidade: {info['quantidade']}")
                    print(f"    Preço: R${info['preço']:.2f}")

                else:
                    print(f"\nProduto:{name}")
                    print(f"    Quantidade: {info['quantidade']}")
                    print(f"    Preço: R${info['preço']:.2f}")

    elif choice == "4":
        print("\nSaindo do sistema...")
        break

    else:
        print("\nEscolha um número entre 1 e 4")