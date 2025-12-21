#It decides what (if anything) should be planted on any given tile
def decide_tile(tile_info):
	can_harvest = tile_info["can_harvest"]
	get_ground_type = tile_info["ground_type"]
	get_entity_type = tile_info["culture_type"]
	x = tile_info["x"]
	y = tile_info["y"]
	return tree_decision(can_harvest, x, y)

#def final_decision():
	#tree_decision(can_harvest, x, y)


def tree_decision(can_harvest, x, y):
	if can_harvest and allowed_tree_position(x, y):
		return ["harvest", "plant_tree"]
	if can_harvest and not allowed_tree_position(x, y):
		return ["harvest"]
	if not can_harvest and allowed_tree_position(x, y):
		return ["plant_tree"]
	else:
		return []

def allowed_tree_position (x, y):
	N = 1
	allowed = (x + y) % 2 == 0
	idx = (x + y) // 2
	allowed_position = allowed and (idx % N == 0)
	return allowed_position






#def plant_carrot():
	#if get_ground_type() != Grounds.Grassland:
		#till()
		#plant(Entities.Carrot)
