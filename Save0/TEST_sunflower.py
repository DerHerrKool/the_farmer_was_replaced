change_hat(Hats.Purple_Hat)
def harvest_column():
	for _ in range(get_world_size()):
		if get_ground_type() != Grounds.Soil:
			till()
		harvest()
		if get_water() < 0.5:
			use_item(Items.Water)
		plant(Entities.Sunflower)
		move(East)

while True:
	if spawn_drone(harvest_column):
		move(North)
		#some text