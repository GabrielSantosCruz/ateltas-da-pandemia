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
quant = 0
age = 0
symptom_age = 0
symp_quant = 0
assymptom_age = 0
assymptom_quant = 0

while rep.lower() == 's':
    quant += 1

    while True:
        try:
            age = int(input("Digite sua idade: "))
            total_age += age
            break
        except ValueError:
            print("Erro! Digite a idade em números! ")
            continue

    gender = input("Digite seu sexo (M/F): ")
    fever = input("Teve febre (S/N): ")

    if fever.lower() == 's':
        while True:
            try:
                temperatura = float(input("Qual foi a maior temperatura detectada: "))
                break
            except ValueError:
                print("Digite a temperatura me números! ")
                continue

    else:
        symptom = input("Teve algum sintoma (S/N): ")
        if symptom.lower() == 's':
            # tá adicionando a primeira idade digitada mais uma vez ao total
            # se já foi cadastrada alguma idade antes, ela é somada ao cadastrar alguém sintomático
            symp_quant += 1
            symptom_age += age
        else:
            assymptom_age = age 
            assymptom_quant  += 1

    kit = input("Tomou o kit Covid ao retornar ao Brasil (S/N): ")

    medal = input("Ganhou alguma medalha? (S/N): ")
    
# Calcular a quantidade de medalhas e qual o seu tipo (Ouro, Prata, Bronze)

    if medal.lower() == 's':

        while True:
            try:
                gold = int(input("Quantas medalhas de ouro?: "))
                break
            except ValueError:
                print("Digite a quantidade de medalhas em números! ")
                continue
        
        while True:
            try:
                silver = int(input("Quantas medalhas de prata?: "))
                break
            except ValueError:
                 print("Digite a quantidade de medalhas em números! ")
                 continue
        
        while True:
            try:
                bronze = int(input("Quantas medalhas de bronze?: "))
                break
            except ValueError:
                print("Digite a quantidade de medalhas em números! ")
                continue
    
    rep = input("Deseja cadastrar um novo atleta?(S/N): ")

    if rep.lower() == 'n':

        print("O cadastramento foi encerrado!!!")

# Processamento de dados:
percent_symp = float((100 * symp_quant) / quant) # procentagem dos sintomáticos
middle_age = float(total_age / quant) # Idade média dos atletas
symp_age_middle = float(symptom_age / symp_quant)

# Saída de dados:
   
    # Quantidade de atletas monitorados;
print(f"A quantidade de atletas monitorados é de {quant}!")

    # A quantidade e a porcentagem de atletas que apresentaram sintomas;

print(f"A quantidade de atletas que apresentam sintomas é de {symp_quant}.\nO que equivale a {round(percent_symp, 2)}% do total!" )

    # Idade média de todos os atletas, dos atletas sem sintomas, e dos atletas sintomáticos;
print(f"A idade média dos atletas cadastrados é {round(middle_age, 2)}!\nSendo {round(symp_age_middle, 2)} a media dos simtomáticos")
print(symptom_age, symp_quant)