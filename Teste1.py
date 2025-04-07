nome = "Hatila"
idade = 28
print(f"olá, meu nome é {nome} e tenho {idade} anos!")
nome2 = "priscila"
idade = 29
salario = 3000.50
ativo = True
numero = 73
print("-" * 40)
print(f"{'DADO':<15} | {'VALOR':>20}")
print("-" * 40)
print(f"{'Nome':<15} | {nome2:>20}")
print(f"{'Idade':<15} | {idade:20d}")
print(f"{'Salário':<15} | {f'R${salario:.2f}':>20}")
print(f"{'Ativo':<15} | {str(ativo):>20}")
print(f"{'Número':<15} | {numero:>020d}")
print("-" * 40)
