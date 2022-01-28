from utilidadescev import moedas, dados

p = dados.leiaDinheiro('Insira um valor R$')
print()
moedas.resumo(p, 13, 10)