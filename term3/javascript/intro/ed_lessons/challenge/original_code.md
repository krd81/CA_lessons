## MAIN
```
import rpg

aragorn = rpg.Ranger('Aragorn', 'Human', 100, 50)
galadriel = rpg.Mage('Galadriel', 'Elf', 120, 75)
frodo = rpg.Burglar('Frodo', 'Hobbit', 50, 25)
saruman = rpg.Wizard('Saruman', 'Human', 80, 100)

frodo.inv.set_currency(9, 47, 23)

chest = rpg.Chest(['longsword', 'iron helm'], 2, 25, 50)

galadriel.battle(aragorn)

# print(chest.inv.__dict__)
# print(aragorn.__dict__)
print(galadriel.__dict__)
# print(galadriel.__dict__)

# Frodo loots a chest!
# chest.inv.transfer(frodo.inv)

# print(frodo.inv.__dict__)
# print(frodo.inv.get_currency())
# print(chest.inv.__dict__)

```

## RPG
```
class Character:
    def __init__(self, name, race, health, attack):
        self.name = name
        self.race = race
        self.health = health
        self.attack = attack
        self.inv = Inventory([], 0, 0, 0)

    def battle(self, other):
        print(f'{self.name} attacks {other.name}!')


class Ranger(Character):
    def battle(self, other):
        print(f'{self.name} launches a brutal melee attack on {other.name}!')

    def recruit_undead(self):
        pass


class Mage(Character):
    def __init__(self, name, race, health, attack):
        # Call the superclass constructor
        super().__init__(name, race, health, attack)
        self.mana = 100
        
    def battle(self, other):
        print(f'{self.name} casts a wicked spell at {other.name}!')
        self.mana -= 20


class Burglar(Character):
    pass
    # def battle(self, other):
    #     print(f'{self.name} sneaks in a stealth attack on {other.name}!')


class Wizard(Character):
    def battle(self, other):
        print(f'{self.name} summons an orc minion, which attacks {other.name}!')



class Chest:
    def __init__(self, items, gold, silver, copper):
        self.inv = Inventory(items, gold, silver, copper)

class Inventory:
    def __init__(self, items, gold, silver, copper):
        self.items = items # list
        self.set_currency(gold, silver, copper) # Delegation

    # from_inv and to_inv are instances of Inventory
    def transfer(self, to_inv):
        # Add all the items from from_inv to to_inv
        to_inv.items.extend(self.items)
        # Delete all the items from from_inv
        self.items = []
        # Add the currency from from_inv to to_inv
        to_inv.copper += self.copper
        # Set currency of from_inv to 0
        self.copper = 0

    # Setter
    def set_currency(self, gold, silver, copper):
        self.copper = gold * 10000 + silver * 100 + copper

    # Getter
    def get_currency(self):
        gold = self.copper // 10000
        silver = (self.copper % 10000) // 100
        copper = self.copper % 100
        return gold, silver, copper
```