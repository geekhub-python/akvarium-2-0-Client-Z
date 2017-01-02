from units import *
from tools import *

import pytest


def test_length_create_units():
	list = create_units(Fish, 3, 5) 
	assert len(list) == 3


def test_types_create_units():
	list = create_units(Fish, 3, 5) 
	count = 0
	for el in range(len(list)):
		if isinstance(list[el], Fish):
			count = count + 1
	assert count == 3


def test_weight_create_units():
	list = create_units(Fish, 3, 5) 
	count = 0
	for el in range(len(list)):
		if list[el].weight == 5:
			count = count + 1
	assert count == 3


def test_without_weight_create_units():
	with pytest.raises(ValueError):
		create_units(Fish, 3)


def test_aquarium_is_singletone():
	aqua_1 = Aquarium.instance()
	aqua_2 = Aquarium.instance()
	assert aqua_1 == aqua_2


def test_accept_units_aquarium():
	aqua_1 = Aquarium.instance()
	fish_list = create_units(Fish, 101, 1)
	with pytest.raises(ValueError):
		aqua_1.accept_units(fish_list)

def test_init_seaweed():
	with pytest.raises(ValueError):
		create_units(Seaweed, 3, 5)