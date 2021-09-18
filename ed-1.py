animals = ["zebra","Lion","Dolphin", "Monkey"]
chars = 0
for animal in animals:
    chars += len(animal)


print("Total character: {}, Average Character {}".format(chars, chars/len(animals)))


def inputanimal():
    animal_list = [inputlist for inputlist in input("Enter animal names: ").split()]
   
    chars = 0
    for animals in animal_list:
        chars += len(animals)
    return print("Total character: {}, Average Character {:.0f}".format(chars, chars/len(animal_list)))


inputanimal()