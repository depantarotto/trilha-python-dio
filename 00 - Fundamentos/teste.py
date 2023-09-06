valor = float(input())

if valor > 0:
    # TODO: Imprimir a mensagem de sucesso, formatando o saldo atual (vide Exemplos).
    print("Deposito realizado com sucesso!")
    print(f"Saldo atual: R$ {valor:.2f}")
elif valor == 0:
    # TODO: Imprimir a mensagem de valor inválido.
    print("Encerrando o programa...")
else:
    # TODO: Imprimir a mensagem de encerrar o programa.
    print("Valor invalido! Digite um valor maior que zero.")


# ----------------------------

# valor_inicial = float(input())
# taxa_juros = float(input())
# periodo = int(input())

# valor_final = valor_inicial

# # TODO: Iterar, baseado no período em anos, para calculo do valorFinal com os juros.
# for ano in range(periodo):
#     valor_final += valor_final * taxa_juros

# print(f"Valor final do investimento: R$ {valor_final:.2f}")


#-----------------------------

# # Entrada de dados
# saldo_total = int(input())
# valor_saque = int(input())

# # TODO: Criar as condições necessárias para impressão da saída, vide tabela de exemplos.
# saldo_atualizado = saldo_total - valor_saque
# if saldo_atualizado >= 0:
#   print(f"Saque realizado com sucesso! Novo saldo: {saldo_atualizado}")
# else:
#   print("Saldo insuficiente. Saque nao realizado!")



#------------------------



# saldo_atual = float(input())
# valor_deposito = float(input())
# valor_retirada = float(input())

# #TODO: Calcular o saldo atualizado de acordo com a descrição deste desafio.
# saldo_atual += (valor_deposito - valor_retirada)

# #TODO: Imprimir o a saída de conforme a tabela de exemplos (uma casa decimal).
# print(f"{saldo_atual:.1f}")

# --------------------------

# ativos = []

# # Entrada da quantidade de ativos
# quantidadeAtivos = int(input())

# # Entrada dos códigos dos ativos
# for _ in range(quantidadeAtivos):
#     codigoAtivo = input()
#     ativos.append(codigoAtivo)

# # TODO: Ordenar os ativos em ordem alfabética.
# ativos.sort()

# # TODO: Imprimir a lista de ativos ordenada, conforme a tabela de exemplos.
# for ativo in ativos:
#     print(ativo)