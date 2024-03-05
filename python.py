def add_definition(definitions, key, definition):
    definitions[key] = definition
    print("Definicja dodana pomyślnie")
 
def find_definition(definitions, key):
    if key in definitions:
        print(definitions[key])
    else:
        print("Nie znaleziono definicji dla", key)
 
def delete_definition(definitions, key):
    if key in definitions:
        del definitions[key]
        print("Usunięto definicję dla:", key)
    else:
        print("Nie znaleziono definicji dla", key)
 
definitions = {}
 
while True:
    print("1: Dodaj definicję")
    print("2: Znajdź definicję")
    print("3: Usuń definicję")
    print("4: Wyjście")
 
    choice = input("Co chcesz zrobić? ")
 
    if choice == "1":
        key = input("Wprowadź klucz (słowo) do zdefiniowania: ")
        definition = input("Wprowadź definicję: ")
        add_definition(definitions, key, definition)
    elif choice == "2":
        key = input("Czego szukasz? ")
        find_definition(definitions, key)
    elif choice == "3":
        key = input("Którą definicję chcesz usunąć? ")
        delete_definition(definitions, key)
    elif choice == "4":
        print("Do widzenia!")
        break
    else:
        print("Wprowadziłeś coś poza zakresem")