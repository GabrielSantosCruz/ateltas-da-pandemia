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
total_age = 0
temperature = 0
temperature1 = 0
symp_age_middle = 0
assymptom_age_middle = 0
max_age = 0
min_age = 1000
kit_covid = 0
masculine = 0
feminine = 0
masc_kit = 0
fem_kit = 0
masc_symp = 0
fem_symp = 0
masc_assymp = 0
fem_assymp = 0

while rep.lower() == 's':
    quant += 1

    try:
        age = int(input("Digite sua idade: "))
    except:
        age = int(input("Erro! Digite uma idade válida: "))
    while (age < 10) or (age > 100): #or Exception():
        age = int(input("Erro! Digite uma idade válida: "))
    total_age += age


    gender = str(input("Digite seu sexo (M/F): ")).lower()
    while gender not in 'mf':
        gender = str(input("Erro! Digite M ou F: "))
    fever = str(input("Teve febre (S/N): ")).lower()
    while fever not in 'sn':
        fever = str(input("Erro! Digite S ou N: "))
        if gender == 'm':
            masculine += 1
        if gender == 'f':
            feminine += 1

    if fever.lower() == 's':
        while True:
            try:
                temperature = float(input("Qual foi a maior temperatura detectada: "))
                break
            except ValueError:
                print("Digite a temperatura me números! ")
                continue

    else:
        symptom = str(input("Teve algum sintoma (S/N): ")).lower()
        while symptom not in 'sn':
            symptom = str(input("Erro! Digite S ou N: "))
        if symptom == 's':
            symp_quant += 1
            symptom_age += age
            if gender == 'm':
                masc_symp += 1
            if gender == 'f':
                fem_symp += 1

        else:
            assymptom_quant  += 1
            assymptom_age += age 
            if gender == 'm':
                masc_assymp += 1
            if gender == 'f':
                fem_assymp += 1

    if symptom == 's':   
        if min_age > age: # sempre dando a maior
            min_age = age
        elif age > max_age: # sempre 0 
            max_age = age

    kit = str(input("Tomou o kit Covid ao retornar ao Brasil (S/N): ")).lower()
    while kit not in 'sn':
        kit = str(input("Erro! Digite S ou N: "))
    if kit == 's':
        kit_covid += 1
        if gender == 'm':
            masc_kit += 1
        if gender == 'f':
            fem_kit += 1

    medal = input("Ganhou alguma medalha? (S/N): ")
    while medal not in 'sn':
        medal = str(input("Erro! Digite S ou N: "))
    
# Calcular a quantidade de medalhas e qual o seu tipo (Ouro, Prata, Bronze)

    if medal.lower() == 's':

        try:
            gold = int(input("Quantas medalhas de ouro?: "))
        except:
            gold = int(input("Erro! Quantas medalhas de ouro?: "))
        while gold <= 0:
            gold = int(input("Erro! Quantas medalhas de ouro?: "))

        try:
            silver = int(input("Quantas medalhas de prata?: "))
        except:
            silver = int(input("Erro! Quantas medalhas de prata?: "))
        while silver <= 0:
            silver = int(input("Erro! Quantas medalhas de prata?: "))
                   
        try:
            bronze = int(input("Quantas medalhas de bronze?: "))
        except:
            bronze = int(input("Erro! Quantas medalhas de bronze?: "))
        while bronze <=0:
            bronze = int(input("Erro! Quantas medalhas de bronze?: "))
    
    rep = str(input("Deseja cadastrar um novo atleta?(S/N): ")).lower()
    while rep not in 'sn':
        rep = str(input("Erro! Digite S ou N: "))
    if rep.lower() == 'n':

        print("O cadastramento foi encerrado!!!")

# Processamento de dados:

    # procentagem dos sintomáticos
middle_age = float(total_age / quant) # Idade média dos atletas

    # se o atleta tiver febre e não forem preenchidos estes dados da erro de ZerodivisionError
if (fever == 'n') and (symp_quant > 0) and (symptom == 's'):
    symp_age_middle = float(symptom_age / symp_quant) # Idade média dos sintomáticos

if symptom == 'n':    
    assymptom_age_middle = float(assymptom_age / assymptom_quant) # Idade média dos assintomáticos

if temperature > temperature1: # temperatura máxima
    temperature1 = temperature

percent_symp = float((100 * symp_quant) / quant) # procentagem dos sintomáticos

# Saída de dados:
   
    # Quantidade de atletas monitorados;
print(f"A quantidade de atletas monitorados é de {quant}!")

    # A quantidade e a porcentagem de atletas que apresentaram sintomas;

print(f"A quantidade de atletas que apresentam sintomas é de {symp_quant}.\nO que equivale a {round(percent_symp, 2)}% do total!" )

    # Idade média de todos os atletas, dos atletas sem sintomas, e dos atletas sintomáticos;
print(f"A idade média dos atletas cadastrados é {round(middle_age, 2)}!\nSendo {round(symp_age_middle, 2)} a media dos sintomáticos\nE {assymptom_age_middle} a dos assintomáticos")

    # A temperatura corporal mais alta relatada;
if temperature > 0:
    print(f"A maior temperatura registrada foi de {temperature1}!")
elif temperature == 0:
    print("Não houveram atletas com febre!")

    # Dentre os que apresentaram sintomas, a idade do atleta mais novo e do atleta mais velho;
if symptom == 's':
    print(f"Dentre os sintomáticos, a idade do atleta mais novo foi de {min_age} e do atleta mais velho {max_age}!")
else:
    print("Não houveram atletas com sintomas!")
    
    '''Um recorte por gênero dos atletas que tomaram o “kit COVID”, indicando ainda, dentre estes, a  
    quantidade de homens e mulheres que tiveram ou não sintomas;'''
    # quantos homens e mulheres tomaram o kit covid;
    # destes, quantos homens e mulheres tiveram sintomas. E quantos não tiveram;
if kit_covid > 0:
    print(f"A quantidade de homens que tomaram o Kit Covid foi de {masc_kit} e a de mulheres {fem_kit}! ")
    if symp_quant > 0:
        print(f"Dentre estes, {masc_symp} homens e {fem_symp} mulheres tiveram sintomas!")
    if assymptom_quant > 0:    
        print(f"Dentre estes, {masc_assymp} homens e {fem_assymp} não tiveram sintomas!")
else: 
    print("Nenhum atleta tomou o kit covid! ")