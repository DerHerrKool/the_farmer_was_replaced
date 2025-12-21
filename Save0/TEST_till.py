change_hat(Hats.Purple_Hat)
for x in range(get_world_size()):
	for y in range(get_world_size()):
		harvest()
		if get_ground_type() == Grounds.Soil:
			till()
		move(North)
	move(East)