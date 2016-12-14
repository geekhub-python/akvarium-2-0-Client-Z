import random, functools

def food(*args):
    def food_factory(func):
        @functools.wraps(func)
        def wrapper(self, unit):
            result = type(unit) in args
            return func(self, unit, result)
        return wrapper
    return food_factory

class Seaweed():

	def __init__(self, weight):
		if weight > 3 or weight < 1:
			raise ValueError("Weight must be less then 4 and more than 0")
		self.weight = weight

class Fish():

	def __init__(self, weight):
		if weight > 9 or weight < 1:
			raise ValueError("Weight must be less then 10 and more than 0")
		self.weight = weight
		self.count_unit_eaten = 0

	def hunt(self, aquarium):
		i = random.randint(0, len(aquarium)-1)
		some_unit = aquarium[i]
		was_eat = self.eat(some_unit)
		if was_eat:						# Если хищник съел юнита, то удаляем съеденное из аквариума
			aquarium.pop(i)

	@food(Seaweed)
	def eat(self, some_unit, result = False):
		if result:
			self.weight = self.weight + some_unit.weight
			self.count_unit_eaten += 1
			return True
		
class PredatorFish(Fish):
	DEFAULT_PREDATOR_WEIGHT = 10			# this is a constant: weight, for predator fish

	def __init__(self):
		self.weight = self.DEFAULT_PREDATOR_WEIGHT
		self.count_fish_eaten = 0                            # count of fish eaten

	def hunt(self, aquarium):
		i = random.randint(0, len(aquarium)-1)
		some_fish = aquarium[i]
		was_eat = self.eat(some_fish)
		if was_eat:						
			aquarium.pop(i)

	@food(Fish)
	def eat(self, some_unit, result = False):
		if result:
			self.weight = self.weight + some_unit.weight
			self.count_fish_eaten += 1
			return True

class Sneil():

	def __init__(self, weight):
		if weight > 5 or weight < 1:
			raise ValueError("Weight must be less then 6 and more than 0")
		self.weight = weight
		self.count_unit_eaten = 0

	def hunt(self, aquarium):
		i = random.randint(0, len(aquarium)-1)
		some_unit = aquarium[i]
		was_eat = self.eat(some_unit)
		if was_eat:
			aquarium.pop(i)

	@food(Seaweed)
	def eat(self, some_unit, result = False):
		if result:
			self.weight = self.weight + some_unit.weight
			self.count_unit_eaten += 1
			return True

class Aquarium:

	@classmethod
	def instance(cls):
		if not hasattr(cls, "__instance"):
			setattr(cls, "__instance", cls())
		return getattr(cls, "__instance")

	aquarium = []

	def accept_units(self, units):	
		self.aquarium.extend(units)	
		if len(self.aquarium) > 100:
			raise ValueError("Count must be less then 101")

	def get_aquarium(self):
		return self.aquarium
