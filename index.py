import json

salle_list = []
def creation():
    salle_info = []
    name = input("saisir l'identificateur de la salle :")
    type = input("saisir le type :")
    capacite = input("saisir la capacite :")

    salle_info.append(name)
    salle_info.append(type)
    salle_info.append(capacite)
    salle_list.append(salle_info)
    print(salle_list)
def list():
    print('Id','Type', 'capacite')
    for i in salle_list:
        for j in range(0,3):
            print(i[j], end=' ')
        print()
def save():
    file_path = "data.json"
    with open(file_path, 'w') as json_file:
        json.dump(salle_list,json_file)
        print('enregistree avec succee')
def quit():
    exit()
def index():
    n = 0
    while n < 10:
        print('1- nouvelle salle')
        print('2- afficher la list des salles')
        print('3- enregister dans un fichier')
        print('4- quiter')
        print('_________________________')
        number = int(input('taper votre choix : '))
        n += 1
        if number == 1:
            creation()
        elif number == 2:
            list()
        elif number == 3:
            save()
        elif number==4:
            quit()


index()




