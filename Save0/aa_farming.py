#Single tile logic
from dispatcher import decide_tile
def handle_tile(x, y):
	tile_info = {
		"can_harvest": can_harvest(),
		"ground_type": get_ground_type(),
		"culture_type": get_entity_type(),
		"x": x,
		"y": y,
		}
	dispatcher_actions = decide_tile(tile_info)
	for action in dispatcher_actions:
		if action == "harvest":
			harvest()
		if action == "plant_tree":
			plant_tree()

def change_ground_type():
	till()

def plant_tree():
	plant(Entities.Tree)

def plant_carrot():
	plant(Entities.Carrot)

def plant_pumpkin():
	plant(Entities.Pumpkin)

def plant_cactus():
	plant(Entities.Cactus)

def plant_sunflower():
	plant(Entities.Sunflower)


