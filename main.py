from characters import Warrior, Mage, EvilWizard, Archer, Paladin

# Function to create player character based on user input
def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")  # Add Archer
    print("4. Paladin")  # Add Paladin
    
    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

# Battle function with user menu for actions
def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")
        
        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
           if isinstance(player, Warrior):
               player.power_attack(wizard)
           elif isinstance(player, Mage):
               player.cast_spell(wizard) 
           elif isinstance(player, Archer):
               print("1. Quick Shot") 
               print("2. Evade") 
               sub = input("Choose an ability: ")
               if sub == 1:
                   player.quick_shot(wizard)
               elif sub == 2:
                   player.evade()
               else:
                   print("Invalid ability choice!")
           elif isinstance(player, Paladin):
               print("1. Holy Strike") 
               print("2. Divide Shield") 
               sub = input("Choose an ability: ")
               if sub == 1:
                   player.holy_strike(wizard)
               elif sub == 2:
                   player.divine_shield()
               else:
                   print("Invalid ability choice!")
        elif choice == '3':
           player.heal()
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice, try again.")
            continue

        # Evil Wizard's turn to attack and regenerate
        if wizard.health > 0:
            wizard.regenerate()
            
            if isinstance(player, Archer) and getattr(player, "evading", False):
                print(f"{player.name} evades the attack!")
                player.evading = False # Reset event
            elif isinstance(player, Paladin) and getattr(player, "shielded", False):
                print(f"{player.name}'s Divine Shield blocks th4e attack!")
                player.shielded = False # Reset shield
            else:
                wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")

# Main function to handle the flow of the game
def main():
    # Character creation phase
    player = create_character()

    # Evil Wizard is created
    wizard = EvilWizard("The Dark Wizard")

    # Start the battle
    battle(player, wizard)

if __name__ == "__main__":
    main()