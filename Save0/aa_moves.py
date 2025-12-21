#Traversal over the farm grid (calls an action once per tile)
def move_over_farm(farming_actions):
	for x in range(get_world_size()):
		for y in range(get_world_size()):
			farming_actions(x,y)
			move(North)
		move(East)
