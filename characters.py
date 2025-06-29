import random

# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  # Store the original health for maximum limit
        self.evading = False
        self.shielded = False

    def attack(self, opponent):
        damage = random.randint(int(self.attack_power * 0.8), int(self.attack_power * 1.2))
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    def heal(self):
        heal_amount = 20
        original_health = self.health
        self.health = min(self.health + heal_amount, self.max_health)
        actual_healed = self.health - original_health
        print(f"{self.name} heals for {actual_healed} health! Current health: {self.health}/{self.max_health}")

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)  # Boost health and attack power

    def power_attack(self, opponent):
       damage = int(self.attack_power * 1.5)
       opponent.health -= damage
       print(f"{self.name} uses Power Attack! Deals with {damage} damage!") 



# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)  # Boost attack power

    def cast_spell(self, opponent):
       damage = int(self.attack_power * 1.8)
       opponent.health -= damage
       print(f"{self.name} uses a Fireball! Deals with {damage} magic damage!")


# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)  # Lower attack power
    
    # Evil Wizard's special ability: it can regenerate health
    def regenerate(self):
        self.health += 5  # Lower regeneration amount
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

# Archer class (inherits from Character)
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health = 110, attack_power = 20)

    def quick_shot(self, opponent):
        damage = self.attack_power * 2
        opponent.health -= damage
        print(f"{self.name} uses Quick SHot! Deals {damage} damage!")

    def evade(self):
        self.evading = True
        print(f"{self.name} prepares to evade the next attack.")

# Paladin class (inherits from Character)
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health = 130, attack_power = 22)
        self.shielded = False
    
    def holy_strike(self, opponent):
        damage = self.attack_power + 10
        opponent.health -= damage
        print(f"{self.name} uses Holy Strike! Deals {damage} damage!")

    def divine_shield(self):
        self.shielded = True
        print(f"{self.name}activated Divine Shield and will block the next attack.")

