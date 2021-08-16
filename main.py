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


while rep.lower() == 's':
    quant += 1
    while True:
        try:
            age.append(int(input("Digite sua idade: ")))
            break
        except ValueError:
            print("Erro! Digite a idade em números! ")
            continue

<<<<<<< HEAD
    age = int(input("Digite sua idade: "))
    while True:
        try:
            age = int(input("Digite sua idade: "))
            break
        except ValueError:
            print("Erro! Digite a idade em números! ")
            continue

    gender = input("Digite seu sexo (M/F): ")
=======
    gender.append(input("Digite seu sexo (M/F): "))
>>>>>>> 03e4d0a422631ee0a58cb0d7aa75c73b2fcae02a
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
        while True:
            try:
                gold.append(int(input("Quantas medalhas de ouro?: ")))
                break
            except ValueError:
                print("Erro! Digite um número! ")
                continue
        
        while True:
            try:
                silver.append(int(input("Quantas medalhas de prata?: ")))
                break
            except ValueError:
                print("Erro! Digite um número!")
                continue       
        
        while True:
            try:
                bronze.append(int(input("Quantas medalhas de bronze?: ")))
                break
            except ValueError:
                print("Erro! Digite um número!")
                continue
        
    rep = input("Deseja cadastrar um novo atleta?(S/N): ")

    if rep.lower() == 'n':

        print("O cadastramento foi encerrado!!!")

# Processamento de dados:

    # A quantidade e a porcentagem de atletas que apresentaram sintomas;
athletes_symptoms = symptom.count('s') 
athletes_porcent = (athletes_symptoms * 100) / quant    

    # Idade média de todos os atletas, dos atletas sem sintomas, e dos atletas sintomáticos;

middle_ages = sum(age) / len(age)

# Saida de dados

print(f"A quantidade de atletas cadastrados é de: {quant}")
print(f"A quantidade de atletas que tiveram sintomas e de {athletes_symptoms}.\nO que equivale a {athletes_porcent}% do total")
