import random

# Állat adatbázis bővebb tulajdonságokkal
animals = [
    {
        "name": "elefánt",
        "attributes": ["nagy testű", "szürke színű", "hosszú ormánya van", "emlős", "Afrikában él vagy Ázsiában él"]
    },
    {
        "name": "oroszlán",
        "attributes": ["nagy testű", "ragadozó", "sörénye van", "emlős", "Afrikában él"]
    },
    {
        "name": "pingvin",
        "attributes": ["madár", "nem tud repülni", "hideg területeken él", "fekete-fehér színű", "vízben úszik"]
    },
    {
        "name": "kígyó",
        "attributes": ["nincs lába", "hosszú testű", "mérges lehet", "hüllő", "különböző színek"]
    },
    {
        "name": "kenguru",
        "attributes": ["nagy testű", "ugrál", "Ausztráliában él", "emlős", "zsebes"]
    },
    {
        "name": "teknős",
        "attributes": ["hosszú életű", "van páncélja", "lassan mozog", "hüllő", "vízben és szárazföldön is él"]
    },
    {
        "name": "bálna",
        "attributes": ["nagy testű", "vízben él", "emlős", "tengerben él", "szűri a táplálékát"]
    },
    {
        "name": "páva",
        "attributes": ["madár", "színes tolla van", "nagy farok tollai vannak", "Indiában él", "tollait kiterjeszti"]
    }
]

def ask_yes_no_question(question):
    while True:
        answer = input(f"{question} (igen/nem): ").strip().lower()
        if answer in ["igen", "nem"]:
            return answer == "igen"
        else:
            print("Kérlek, válaszolj igennel vagy nemmel.")

def main():
    print("Üdvözöllek az Állatos Kitalálós Játékban!")
    print("Gondolj egy állatra, majd válaszolj a kérdésekre igennel vagy nemmel, hogy kitaláljam, melyik állatra gondoltál.")
    
    while True:
        animal = random.choice(animals)
        print("\nGondoltál egy állatra. Kezdjük!")

        correct_answers = 0
        for attribute in animal["attributes"]:
            if ask_yes_no_question(attribute):
                correct_answers += 1
        
        print(f"Az állat jellemzői: {', '.join(animal['attributes'])}")
        print(f"Én {correct_answers} jellemzőt találtam el a {len(animal['attributes'])}-ből.")

        play_again = input("Szeretnél újra játszani? (igen/nem): ").strip().lower()
        if play_again != "igen":
            break

if __name__ == "__main__":
    main()
