while True:

    print("\n")
    print("\n  GESTÃO  ")
    print("    Sistema de Gestão Agropecuário")
    print("  [1]    Gestão Financeira")
    print("  [2]    Pesagem e Nutrição")
    print("  [3]    Sair do Sistema")


    opcao = input("  Escolha uma opção: ")

    if opcao == "1":

        print("\n       GESTÃO FINANCEIRA")

        custos = float(input("  Custos totais (R$): "))
        receita = float(input(" Ganhos esperados (R$): "))

        lucro = receita - custos

        print("\n  ──────────────────────────────────")
        print(f"  Ganhos:   R$ {receita:.2f}")
        print(f"  Custos:   R$ {custos:.2f}")
        print(f"  Lucro:    R$ {lucro:.2f}")
        print("  ──────────────────────────────────")

        if lucro > 0:
            print("    Status: OPERAÇÃO SAUDÁVEL")
        else:
            print("    Status: ALERTA DE PREJUÍZO")


    elif opcao == "2":

        print("     PESAGEM E NUTRIÇÃO ")

        peso_ideal = float(input("    Peso Ideal / Meta (KG): "))
        peso_atual = float(input("    Peso Atual na Balança (KG): "))

        print("\n ")
        print(f"  Peso Ideal:  {peso_ideal:.2f} kg")
        print(f"  Peso Atual:  {peso_atual:.2f} kg")
        print("\n ")

        if peso_atual >= peso_ideal:
            print("    Peso certificado!")
            print("    Animal dentro dos padrões para venda.")

        else:
            diferenca = peso_ideal - peso_atual
            print(f"    Animal abaixo do peso em {diferenca:.2f} kg.")
            print("\n   NUTRIÇÃO ACIONADO ")
            preco_racao = float(input("   Preço do KG de ração (R$): "))
            conversao_alimentar = 7.0 
            kg_racao_necessario = diferenca * conversao_alimentar
            custo_nutricao = kg_racao_necessario * preco_racao
            print("\n")
            
            print("         PLANO ALIMENTAR ESTIMADO         ")
            print(f"  KG de ração total: {kg_racao_necessario:.2f} kg")
            print(f"  Custo total da nutrição.: R$ {custo_nutricao:.2f}")
            print("  Pesar novamente em 30 dias.")


    elif opcao == "3":

        print("   Encerrando o sistema")
        break

    else:
        print("\n  Opção inválida! Digite 1, 2 ou 3.")
