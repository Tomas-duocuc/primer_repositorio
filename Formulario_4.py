turistas = {"001": ["John Doe", "Estados Unidos", "12-01-2024"],
            "002": ["Emily Smith", "Estados Unidos", "23-03-2024"],
            "012": ["Julian Martinez", "Argentina", "19-09-2023"],
            "014": ["Agustin Morales", "Argentina", "28-03-2024"],
            "005": ["Carlos Garcia", "Mexico", "10-05-2024"],
            "006": ["Maria Lopez", "Mexico", "08-12-2023"],
            "007": ["Joao Silva", "Brasil", "20-06-2024"],
	        "003": ["Michael Brown", "Estados Unidos", "05-07-2023"],
	        "004": ["Jessica Davis", "Estados Unidos", "15-11-2024"],
            "008": ["Ana Santos", "Brasil", "03-10-2023"],
            "010": ["Martin Fernandez", "Argentina", "13-02-2023"],
            "011": ["Sofia Gomez", "Argentina", "07-04-2024"],
    }
def turistas_del_pais(pais):
        for i in turistas:
            paises=(turistas[i][1])
            if paises==pais:
                print(turistas[i][0])

def turistas_por_mes():
    
opcion=0
while opcion!=4:
    print("*** MENU PRINCIPAL ***")
    print("1.- Turistas por país.")
    print("2.- Turista por mes.")
    print("3.- Eliminar turista.")
    print("4.- Salir")
    opcion=int(input("Ingrese la opcion que desea: "))
    match opcion:
        case 1:
            print("Seleccione el pais que desea: ")
            print("1.- Estados Unidos")
            print("2.- Argentina")
            print("3.- Mexico")
            print("4.- Brasil")
            print("5.- Salir")
            pais=int(input(""))
            match pais:
                case 1:
                    pais="Estados Unidos"
                case 2:
                    pais="Argentina"
                case 3:
                    pais="Mexico"
                case 4:
                    pais="Brasil"
                case 5:
                    break
                case _:
                    print("Eliga una de las opciones mencionadas")
            turistas_del_pais(pais)
        case 2:
            


