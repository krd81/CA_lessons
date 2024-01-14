class Character {
    constructor(name, race, health, attack){
        this.name = name
        this.race = race
        this.health = health
        this.attack = attack
        this.inv = new Inventory([], 0, 0, 0)
    }

    battle(other){
        console.log(`${this.name} attacks ${other.name}!`)
    }
}

class Ranger extends Character{
    constructor(name, race, health, attack){
        super(name, race, health, attack)
    }

    battle(other){        
        console.log(`${this.name} launches brutal melee attack on ${other.name}!`)
    }

    recruitUndead(){
        
    }
}

class Mage extends Character{
    constructor(name, race, health, attack){
        super(name, race, health, attack)
        this.mana = 100
    }

    battle(other){        
        console.log(`${this.name} casts a wicked spell at ${other.name}!`)
        this.mana -= 20
    }
}

class Burglar extends Character{
    constructor(name, race, health, attack){
        super(name, race, health, attack)
    }

    battle(other){        
        console.log(`${this.name} sneaks in a stealth attack on ${other.name}!`)
    }
}

class Wizard extends Character{
    constructor(name, race, health, attack){
        super(name, race, health, attack)
    }

    battle(other){        
        console.log(`${this.name} summons an orc minion, which attacks ${other.name}!`)
    }
}

class Inventory{
    constructor(items, gold, silver, copper){
        this.items = items
        this.setCurrency(gold, silver, copper)
    }

    transfer(toInv){
        // items are transferred to another character's Inventory
        toInv.items.push(this.items)
        // items are removed from this character's Inventory
        this.items = []
        // Currency is transferred to another character
        toInv.copper += this.copper
        // This character's currency is set to zero
        this.copper = 0
    }

    setCurrency(gold, silver, copper){
        this.copper = gold * 10000 + silver * 100 + copper
    }

    getCurrency(){
        this.gold = (this.copper - (this.copper % 10000)) / 10000
        this.copper -= this.gold * 10000
        this.silver = (this.copper - (this.copper % 100)) / 100
        this.copper -= this.silver * 100
        return this.gold, this.silver, this.copper
    }
}

class Chest{
    constructor(items, gold, silver, copper){
        this.inv = new Inventory(items, gold, silver, copper)
    }
}


aragorn = new Ranger("Aragorn", "Human", 100, 50)
galadriel = new Mage('Galadriel', 'Elf', 120, 75)
frodo = new Burglar('Frodo', 'Hobbit', 50, 25)
saruman = new Wizard('Saruman', 'Human', 80, 100)
chestObject = new Chest(["longsword", "iron helm"], 2, 25, 50)

frodo.inv.setCurrency(9, 47, 23)

galadriel.battle(aragorn)
console.log(aragorn)
console.log(galadriel)
console.log(frodo)
console.log(chestObject)

// Frodo loots a chest!
chestObject.inv.transfer(frodo.inv)
console.log(frodo)
console.log(frodo.inv)
console.log(frodo.inv.getCurrency())

console.log(chestObject)


