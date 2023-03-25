from time import sleep

first_l = [
    "Brás",
    "Tatuapé",
    "Engº Goulart",
    "USP Leste",
    "Comendador Ermelino",
    "São Miguel Paulista",
    "Jardim Helena - Vila Mara",
    "Itaim Paulista",
    "Jardim Romano",
    "Engº Manoel Feio",
    "Itaquaquecetuba",
    "Aracaré",
    "Calmon Viana"
]

second_l = [
    "Luz",
    "Brás",
    "Tatuapé",
    "Corinthias - Itaquera",
    "Dom Bosco",
    "José Bonifácio",
    "Guaianases",
    "Antonio Gianetti Neto",
    "Ferraz de Vasconcelos",
    "Poá",
    "Calmon Viana",
    "Suzano",
    "Jundiapeba",
    "Braz Cubas",
    "Mogi das Cruzes",
    "Estudantes"
]

transfer = [
    "Brás",
    "Tatuapé",
    "Calon Viana"
]

lines = [
    first_l,
    second_l
]

i=0
max=len(first_l)-1

current_line = first_l

def start_end():
    global start, end
    if current_line[i] == current_line[0]:
        start = current_line[0]
        end = current_line[max]
    elif current_line[i] == current_line[max]:
        start = current_line[max]
        end = current_line[0]
    return start,end


def final():
    if current_station == current_line[max] or current_station == current_line[0]:
        print(f"ESTAÇÃO FINAL\n")
    else:
        print(f"DESTINO : {end}\n")


def goto_next():
    global i, next_station
    if start == current_line[0]:
        i += 1
    elif start == current_line[max]:
        i -= 1
    next_station = current_line[i]
    print(f"PRÓXIMA ESTAÇÃO : {next_station}")
    return i, next_station


def change_line():
    global current_line
    if current_station in transfer:
        ask = input(f"Transferencia para Linha 2?\n").lower()
        if ask == 'y':
            current_line = second_l
        else:
            print("Prosseguindo")


while True:
    current_station = current_line[i]
    print(f"VOCÊ ESTÁ EM : {current_station}")

    start_end()

    if current_line != second_l:
        change_line()

    goto_next()

    final()

    sleep(3)
