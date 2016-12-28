from tools import *


if __name__ == '__main__':

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


	min_count_units = len(predator_list) + len(sneils_list)
	start_fauna(myAquarium.aquarium, min_count_units)										# Да начнется ОХОТА! ]:-)
	out_put(predator_list, sneils_list)
	print("Count units: ", len(myAquarium.aquarium))