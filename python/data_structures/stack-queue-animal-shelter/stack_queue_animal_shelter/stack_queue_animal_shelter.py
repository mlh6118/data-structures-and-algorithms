from .queue2 import Queue
from .node import Node
from .invalid_operation_error import InvalidOperationError


class AnimalShelter:
    def __init__(self):
        self.animal_shelter = Queue()
        self.animal_shelter.enqueue("Waiting Room")

    def enqueue(self, animal):
        self.animal_shelter.enqueue(animal)

    def dequeue(self, animal):
        if animal != "cat" and animal != "dog":
            return None
        while type(self.animal_shelter.peek()) == str or self.animal_shelter.peek().value != animal:
            temp_animal = self.animal_shelter.dequeue()
            self.animal_shelter.enqueue(temp_animal)
        if animal == "cat" or animal == "dog":
            return self.animal_shelter.dequeue()


class Dog:
    def __init__(self, value="dog"):
        self.value = value


class Cat:
    def __init__(self, value="cat"):
        self.value = value
