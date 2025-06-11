import random

class Player:
    def __init__(self):
        self.health = 100
        self.food = 3
        self.energy = 100

    def rest(self):
        if self.food > 0:
            self.food -= 1
            self.energy += 20
            print("Sa puhkasid ja taastasid energiat.")
        else:
            print("Sul pole toitu!")

    def take_damage(self, amount):
        self.health -= amount
        print(f"Sa said kahju: -{amount} tervist.")

    def status(self):
        print(f"Tervis: {self.health}, Toit: {self.food}, Energia: {self.energy}")

def event(player):
    roll = random.randint(1, 100)
    if roll <= 30:
        damage = random.randint(10, 30)
        print("Sind ründas röövel!")
        player.take_damage(damage)
    elif roll <= 50:
        print("Leidsid toitu!")
        player.food += 1
    elif roll <= 60:
        print("Sa said puhata rahus.")
        player.energy += 10
    else:
        print("Midagi ei juhtunud.")

def main():
    player = Player()
    turns_left = 10

    print("Tere tulemast mängu 'Sundöö'!")
    while turns_left > 0 and player.health > 0:
        print("\n" + "-" * 30)
        print(f"Käike jäänud: {turns_left}")
        player.status()

        print("Vali tegevus:")
        print("1 - Puhka")
        print("2 - Liigu edasi")
        print("3 - Otsi toitu")
        choice = input("Valik: ")

        if choice == "1":
            player.rest()
        elif choice == "2":
            print("Liikusid edasi...")
            event(player)
            player.energy -= 10
        elif choice == "3":
            print("Otsid toitu...")
            if random.randint(1, 100) <= 50:
                print("Leidsid midagi!")
                player.food += 1
            else:
                print("Ei leidnud midagi.")
            player.energy -= 5
        else:
            print("Tundmatu valik.")

        turns_left -= 1

    print("\nMäng läbi!")
    if player.health > 0:
        print("Sa jäid ellu!")
    else:
        print("Sa surid...")

if __name__ == "__main__":
    main()
