#change_hat(Hats.Dinosaur_Hat)
#change_hat(Hats.Purple_Hat)
#set_world_size(8)
#set_execution_speed(8)

def harvest_column():
	for _ in range(get_world_size()):
		if get_ground_type() != Grounds.Soil:
			till()
		harvest()
		plant(Entities.Cactus)
		move(East)

while True:
	if spawn_drone(harvest_column):
		move(North)

