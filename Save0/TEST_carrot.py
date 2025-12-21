change_hat(Hats.Purple_Hat)
#set_world_size(6)
#set_execution_speed(1)
def harvest_column():
	counter = 0
	for _ in range(get_world_size()):
		if get_ground_type() != Grounds.Soil:
			till()
		harvest()
		if counter == 4:
			counter = 0
			plant(Entities.Sunflower)
		else:
			plant(Entities.Carrot)
			counter = counter + 1
			#print(counter)
		move(East)

while True:
	if spawn_drone(harvest_column):
		move(North)