#change_hat(Hats.Dinosaur_Hat)
#change_hat(Hats.Purple_Hat)
#set_world_size(8)
#set_execution_speed(8)


def harvest_column():
	counter = 0
	for _ in range(get_world_size()):
		if get_ground_type() != Grounds.Soil:
			till()
		harvest()
		if get_water() < 0.5:
			use_item(Items.Water)
		if counter == 4:
			counter = 0
			plant(Entities.Sunflower)
		else:
			plant(Entities.Cactus)
			counter = counter + 1
			#print(counter)
		move(East)

while True:
	if spawn_drone(harvest_column):
		move(North)