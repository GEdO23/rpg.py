from time import sleep

sapph_l = [
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

i=0
max=len(sapph_l)-1


def start_end():
    global start, end
    if sapph_l[i] == sapph_l[0]:
        start = sapph_l[0]
        end = sapph_l[max]
    elif sapph_l[i] == sapph_l[max]:
        start = sapph_l[max]
        end = sapph_l[0]
    return start,end

def final():
    if current == sapph_l[max] or current == sapph_l[0]:
        print(f"ESTAÇÃO FINAL\n")
        sleep(1)
    else:
        print(f"DESTINO : {end}\n")


def goto_next():
    global i
    if start == sapph_l[0]:
        i += 1
    elif start == sapph_l[max]:
        i -= 1
    print(f"PROXIMA ESTAÇÃO : {sapph_l[i]}")
    return i

while True:
    current = sapph_l[i]
    print(f"VOCÊ ESTÁ EM : {current}")

    start_end()

    goto_next()

    final()

    sleep(3)
