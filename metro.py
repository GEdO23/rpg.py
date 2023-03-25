from time import sleep
stations = [
    "Tucuruvi",
    "Parada Inglesa",
    "Jardim São Paulo - Ayrton Senna",
    "Santana",
    "Carandiru",
    "Portuguesa - Tietê",
    "Armênia",
    "Tiradentes",
    "Luz",
    "São Bento",
    "Sé",
    "Japão - Liberdade",
    "São Joaquim",
    "Vergueiro",
    "Paraíso",
    "Ana Rosa",
    "Vila Mariana",
    "Santa Cruz",
    "Praça da Árvore",
    "Saúde",
    "São Judas",
    "Conceição",
    "Jabaquara"
]

i = 0

start = True
end = False
goal = stations[len(stations) - 1]

def goto():
    global i
    global start, end
    global goal

    if start == True and stations[i] != stations[len(stations) - 1]:
        i += 1
        goal = stations[len(stations) - 1]

    elif end == True and stations[i] != stations[0]:
        i -= 1
        goal = stations[0]
    
    elif stations[i] == stations[len(stations) - 1]:
        start = False
        end = True

    elif stations[i] == stations[0]:
        start = True
        end = False

    else:
        print("I didnt quite undestand that")
        sleep(1)
        goto()

while True:
    if stations[i] != stations[0]:
        print(f"\nPREVIOUS STATION : {stations[i-1]} : {i-1}")
    else: 
        print("\nFIRST STATION")
    print(f"CURRENT STATION : {stations[i]} : {i}")
    if stations[i] != stations[len(stations) - 1]:
        print(f"NEXT STATION : {stations[i+1]} : {i+1}\n")
    else:
        print("LAST STATION\n")
    
    print(f"STATION GOAL : {goal}")
    
    sleep(1)
    goto()
