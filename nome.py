
vendas_vendedores = [
    {"nome": "Ana", "vendas": 12000},
    {"nome": "Bruno", "vendas": 8500},
    {"nome": "Carla", "vendas": 15000},
    {"nome": "Diego", "vendas": 5000}
]

print("=== CALCULADORA DE BÔNUS ===")

for vendedor in vendas_vendedores:
    nome = vendedor["nome"]
    vendas = vendedor["vendas"]

if vendas >= 10000:
    # Se vendeu 10.000 ou mais, ganha 10% (multiplica por 0.10)
    bonus = vendas * 0.10
else:
    # Senão (vendeu menos que 10.000), ganha 2% (multiplica por 0.02)
    bonus = vendas * 0.02
print(nome,bonus)