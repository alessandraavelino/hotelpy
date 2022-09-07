hospedes = dict()

def create():
    nome = input("Nome do hospede: ")
    telefone = input("Telefone: ")
    numQuarto = input("Número do quarto: ")
    checkin = input("Data de chegada: ")
    checkout = input("Data de saída: ")
    hospedes[nome] = {"nome": nome, "telefone": telefone, "checkin": checkin, "checkout": checkout }
    

def read():
    print(hospedes)

def update():
    pass

def delete():
    nome = input("insira o nome do hospede pra deletar: ")
    hospedes.remove(nome)

def menu():
    
    while True:
        print("** HOTEL PY **")
        print("1 - INSERIR HÓSPEDE")
        print("2 - LISTAR HÓSPEDES")
        print("3 - ATUALIZAR HÓSPEDE")
        print("4 - DELETAR HÓSPEDE")
        
        opt = int(input("-> "))

        if opt == 1:
            create()
        elif opt == 2:
            read()
        elif opt == 3:
            update()
        elif opt == 4:
            delete()
        else:
            print("opc inválida")

menu()


    
