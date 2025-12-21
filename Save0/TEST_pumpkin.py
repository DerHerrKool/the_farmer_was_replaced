change_hat(Hats.Purple_Hat)
while True:
	def planting():
			if get_ground_type() != Grounds.Soil:
				till()
			plant(Entities.Pumpkin)


	for x in range(get_world_size()):
		counter = 0
		for y in range(get_world_size()):
			counter = counter + 1
			harvest()
			if counter == 8:
				counter = 0
				plant(Entities.Sunflower)
			else:
				planting()
			move(North)
		move(East)