class Animal:
    def move(self):
        raise NotImplementedError("Subclass must implement this method")

class Dog(Animal):
    def move(self):
        return "The dog runs 🐕"

class Fish(Animal):
    def move(self):
        return "The fish swims 🐟"

class Bird(Animal):
    def move(self):
        return "The bird flies 🐦"

# Example usage
animals = [Dog(), Fish(), Bird()]

for animal in animals:
    print(animal.move())
