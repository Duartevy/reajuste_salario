# Função: Calcular o novo salário com base no código do cargo
# Autor: Milene Duarte
# Data: 14/08/2024

# Seção de Declarações
salario_atual = 0.0
salario_novo = 0.0
cod_cargo = 0

# Entrada de Dados
cod_cargo = int(input("Informe o código do cargo: "))
salario_atual = float(input("Informe o salário atual: "))

# Processamento de Dados
if cod_cargo == 101:
    salario_novo = salario_atual * 1.1  # Acrescenta 10%
elif cod_cargo == 102:
    salario_novo = salario_atual * 1.2  # Acrescenta 20%
elif cod_cargo == 103:
    salario_novo = salario_atual * 1.3  # Acrescenta 30%
elif cod_cargo == 104:
    salario_novo = salario_atual * 1.4  # Acrescenta 40%
elif cod_cargo == 105:
    salario_novo = salario_atual * 1.5  # Acrescenta 50%
else:
    print("Código de cargo inválido.")
    exit()

# Saída de Dados
print(f"O salário novo é: R$ {salario_novo:.2f}")
print(f"A diferença é: R$ {salario_novo - salario_atual:.2f}")
