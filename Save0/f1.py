while True:
	x, y = get_pos_x(), get_pos_y()
	max_x, max_y = get_world_size(), get_world_size()
	#print(max_x)
	#print(max_y)
	#print(x)
	#print(y)
	if y < (max_y - 1):
		move(North)
	else:
		move(East)
		break
		
	if y > 0:
		move(South)
	else:
		move(East)
		break
		
		