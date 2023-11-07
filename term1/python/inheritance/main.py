class Vehicle:
    def __init__(self, make, model, km_per_litre):
        self.make = make
        self.model = model
        self.km_per_litre = km_per_litre
        self.fuel_level = 0
        self.max_distance = self.MAX_FUEL * self.km_per_litre

    MAX_FUEL = 50
    

    def fuel_level(self):
        return self.fuel_level
    
    def refuel(self, litres):
        if (self.fuel_level + litres > self.MAX_FUEL):
            self.fuel_level = self.MAX_FUEL
        else:
            self.fuel_level += litres

    def set_fuel_level(self, litres):
        self.fuel_level = litres


    # Travel method takes a distance in KM and adjusts the fuel level based on the distance
    # Returns the actual distance travelled (accounts for running out of fuel)
    def travel(self, distance):
        actual_distance = 0
        if (distance / self.km_per_litre) > self.fuel_level: # Checks whether litres req'd for distance is > fuel level
            actual_distance = self.km_per_litre * self.fuel_level
            self.set_fuel_level(0)
        else:
            self.refuel(distance / self.km_per_litre * -1) # multiply by -1 to subtract this number from the current fuel level
            actual_distance = distance

        return actual_distance




class Car(Vehicle):
    
    def wind_up_windows(self):
        print("The windows are closed")


class Motorbike(Vehicle):
    
    MAX_FUEL = 15

    def wheelie(self):
        print("You're doing a wheelie!")



# main




# CAR TEST #
'''
civic = Car("Honda", "Civic", 15) # 15KM per L

initial_fuel_level = int(input("What is the vehicle's initial fuel level? "))
civic.refuel(initial_fuel_level)
# civic.refuel(10)
civic.fuel_level # -> 20L in the tank
print(f'{civic.fuel_level}L in the tank')

kms_travelled = int(input("What is the distance travelled? "))

print(f'The actual distance travelled was {civic.travel(kms_travelled)}km\n')

print(f'{civic.fuel_level:.1f}L in the tank')

# MOTORBIKE TEST #
'''
low_rider = Motorbike("Harley Davidson", "Low Rider", 25) # 25KM per L

initial_fuel_level = int(input("What is the vehicle's initial fuel level? "))
low_rider.refuel(initial_fuel_level)
print(f'{low_rider.fuel_level}L in the tank')

kms_travelled = int(input("What is the distance travelled? "))

print(f'The actual distance travelled was {low_rider.travel(kms_travelled)}km\n')

print(f'{low_rider.fuel_level:.1f}L in the tank')




'''
civic = Car("Honda", "Civic")
civic.fuel_level # -> 0L in the tank
print(f'{civic.fuel_level}L in the tank')

civic.refuel(10)
civic.fuel_level # -> 10L in the tank
print(f'{civic.fuel_level}L in the tank')


civic.refuel(10)
civic.fuel_level # -> 20L in the tank
print(f'{civic.fuel_level}L in the tank')

civic.refuel(100)
civic.fuel_level # -> 50L in the tank

print(f'{civic.fuel_level}L in the tank')


print(f'{low_rider.fuel_level}L in the tank')
low_rider.refuel(30)

print(f'{low_rider.fuel_level}L in the tank')
low_rider.refuel(5)

print(f'{low_rider.fuel_level}L in the tank')
low_rider.refuel(20)

print(f'{low_rider.fuel_level}L in the tank')




'''

