import random
gift_found = "Pan de coco", "Pastil ni Mczeal"

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.items = []

    def attack(self):
        return lambda: random.randint(5, 10)
    
    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            print(f"{self.name} has been killed!")
    
class zombie:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self):
        return lambda: random.randint(3, 10)
    
    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            print(f"{self.name} has been killed!")


class thug:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self):
        return lambda: random.randint(3, 10)
    
    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            print(f"{self.name} has been killed!")
    

def explore(player):
    print("You roam around manila....")
    event = random.choice(["zombie", "survivor", "nothing"])

    if event == "zombie":
        enemy = zombie("zombie", 10)
        print("You encountered a zombie!")
        print("You have no choice but to fight!")
        print("zombie has 10 health points")
        fight_or_run(player, enemy)
    elif event == "thug":
        enemy = thug("thug", 20)
        print("You encountered a thug!")
        print(f"{player.name}: this is stronger, I must fight.")
        print("thug has 20 health points")
        fight_or_run(player, enemy)
    elif event == "survivor":
        print("You've encountered a survivor!")
        print("survivor gave you a gift!")
        gift_found = random.choice(["Pan de coco", "Pastil ni Mczeal"])
        player.items.append(gift_found)
        print(f"You received a {gift_found} from a regular noypi!")
    else:
        print("You didn't find anything interesting.")


def fight_or_run(player, zombie):
    global game_over
    while player.health > 0 and zombie.health > 0:
        print(f"{player.name}'s health: {player.health}")
        print(f"zombie's health: {zombie.health}")
        print("What would you like to do?")
        print("1. Attack")
        print("2. Run")
        choice = input("Enter your choice: ")

        if choice == "1":
            damage = player.attack()()
            zombie.take_damage(damage)
            print(f"{player.name} dealt {damage} damage to dds.")
        elif choice == "2":
            print("You ran away!")
            print("\nYou've suddenly feel an electric shock in your head, you've been killed!")
            print("*\nSystem Shutdown*")
            game_over = True
            break
        else:
            print("Invalid choice! Please enter a valid choice.")
            continue

        if zombie.health > 0:
            player.take_damage(zombie.attack()())
            print(f"zombie dealt {damage} damage to {player.name}.")

        if player.health <= 0:
            print("You've been killed!")
            print("*System Shutdown*")
            game_over = True
            break
        elif zombie.health <= 0:
            print("You've defeated dds!")
            break

def main():
    print("I AM PLAYER")
    print("\nPlease Expand your terminal to see the full text. Enjoy :3")
    print("\nWhat is your name player?")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    print(f"\nWelcome to this simulator, {player.name}. it seems that the city is filled with zombies.")
    print("\nTo survive, you must fight them or run away. But, running away is not helpful bacause there is a nervegear attach to your head irl.")
    print("\nYou must survive this city until the administrator is satisfied with your performance.")
    print("\nIf the zombie or thugs kills you, you will be killed in real life.")
    print("\nYou have a gauntlet, you can do this, Good luck.")
    print(f"System: You currently have {player.health} health.")

    try:
        while player.health > 0:
            explore(player)
            continue_playing = input("Would you like to continue playing? (yes/no): ").lower()
            if continue_playing == "no":
                break
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print(f"\nGame over! {player.name} collected the following items: {player.items}")

if __name__ == "__main__":
    main()