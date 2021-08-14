#/*******************************************************************************
#Autor: Gabriel Santos Cruz
#Componente Curricular: Algoritmos I
#Concluido em: xx/xx/2021
#Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
#trecho de código de outro colega ou de outro autor, tais como provindos de livros e
#apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
#de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
#do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
#******************************************************************************************/

# Entrada de dados:
print("Sistema UEFS pelos atletas\n")

rep = 's'

# espaço para as listas ficarem predefinidamente salvas

age = []
gender = []
fever = []
syptom = []
kit = []
medal = []
quant = 0
# Se eu digitar um numero em vez de uma string e dar erro?

while rep.lower() == 's':
    quant += 1
    age.append(int(input("Digite sua idade: ")))
    gender.append(input("Digite seu sexo (M/F): "))
    fever = input("Teve febre (S/N): ")

    if fever.lower() == 's':
        temperatura = []
        temperatura.append(float(input("Qual foi a maior temperatura detectada: ")))

    else:
        symptom = []
        symptom.append(input("Teve algum sintoma (S/N): "))

    kit.append(input("Tomou o kit Covid ao retornar ao Brasil (S/N): "))

    medal = input("Ganhou alguma medalha? (S/N): ")
    
# Calcular a quantidade de medalhas e qual o seu tipo (Ouro, Prata, Bronze)

    if medal.lower() == 's':
        gold = []
        silver = []
        bronze = []
        gold.append(int(input("Quantas medalhas de ouro?: ")))
        silver.append(int(input("Quantas medalhas de prata?: ")))
        bronze.append(int(input("Quantas medalhas de bronze?: ")))
    
    rep = input("Deseja cadastrar um novo atleta?(S/N): ")

    if rep.lower() == 'n':

        print("O cadastramento foi encerrado!!!")

print(f"A quantidade de atletas cadastrados é de: {quant}")

# Processamento de dados: