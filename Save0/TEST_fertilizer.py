change_hat(Hats.Purple_Hat)
while True:
	for x in range(get_world_size()):
		for y in range(get_world_size()):
			harvest()
			use_item(Items.Fertilizer)
			move(North)
		move(East)

