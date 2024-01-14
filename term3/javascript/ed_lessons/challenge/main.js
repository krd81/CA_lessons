aragorn = new Ranger("Aragorn", "Human", 100, 50)
galadriel = new Mage('Galadriel', 'Elf', 120, 75)
frodo = new Burglar('Frodo', 'Hobbit', 50, 25)
saruman = new Wizard('Saruman', 'Human', 80, 100)

frodo.inv.setCurrency(9, 47, 23)

chest = new Chest(["longsword", "iron helm"], 2, 25, 50)
galadriel.battle(aragorn)