change_hat(Hats.Purple_Hat)
set_world_size(6)
set_execution_speed(6)

		  
def harvest_column():
	for _ in range(get_world_size()):
		#if get_ground_type() != Grounds.Soil:
		#	till()
		harvest()
		#plant(Entities.Cactus)
		move(East)

while True:
	if spawn_drone(harvest_column):
		move(North)