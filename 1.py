from oop import *

if __name__ == '__main__':

	def sort_by_weight(some_list):
		return some_list.weight

	def create_units(type_units, count_units, weight_one_unit = 0):
		units_list = []
		if(weight_one_unit != 0):
			for unit in range(count_units):
				unit = type_units(weight_one_unit)
				units_list.append(unit)
			return units_list
		else:
			for unit in range(count_units):
				unit = type_units()
				units_list.append(unit)
			return units_list

	def out_put(predator_list, sneils_list):
		print("-----FISH_PREDATORS-----")
		predator_list.sort(key = sort_by_weight)
		predator_list.reverse()
		for pred in range(len(predator_list)):
			print("Weight:", predator_list[pred].weight, "Count:", predator_list[pred].count_fish_eaten)
		
		print("-----Sneils-----")
		sneils_list.sort(key = sort_by_weight)
		sneils_list.reverse()
		for sneil in range(len(sneils_list)):
			print("Weight:", sneils_list[sneil].weight, "Count:", sneils_list[sneil].count_unit_eaten)
		
		print()
		print("*******Who`s stay?*******")
		print("Count sneils:", len(sneils_list))

# Один метод запускает все жизненные процессы существ в аквариуме
	def start_fauna(aquarium):
		while len(aquarium) > (len(predator_list) + len(sneils_list)):
			i = random.randint(0, len(aquarium)-1)
			some_unit = aquarium[i]
			if type(some_unit) == Seaweed:
				continue
			else:
				some_unit.hunt(aquarium)

	fish_list = create_units(Fish, random.randint(10,50), random.randint(1,9))
	predator_list = create_units(PredatorFish, 2)
	sneils_list = create_units(Sneil, random.randint(5,10), random.randint(1,5))
	seaweed_list = create_units(Seaweed, random.randint(10,20), random.randint(1,3))

	myAquarium = Aquarium.instance()					# Создаем пустой аквариум, через инстанс
	myAquarium.accept_units(fish_list)					# Запускаем в него сначала обычных рыб
	myAquarium.accept_units(predator_list)				# Теперь хищников (Все по ТЗ)
	myAquarium.accept_units(sneils_list)				# Улитки
	myAquarium.accept_units(seaweed_list)				# Водоросли
	
	print("Count units: ", len(myAquarium.aquarium))		# Посмотрим общее количество живности
	print("Count fish: ", len(fish_list))
	print("Count sneils: ", len(sneils_list))
	print("Count seaweed: ", len(seaweed_list))
	print()
	print("*******Play*******")
	start_fauna(myAquarium.aquarium)										# Да начнется ОХОТА! ]:-)
	out_put(predator_list, sneils_list)
	print("Count units: ", len(myAquarium.aquarium))