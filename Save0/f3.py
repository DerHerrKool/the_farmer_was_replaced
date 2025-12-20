while True:
	x, y = get_pos_x(), get_pos_y()
	for i in range(get_world_size() - 1):
		if can_harvest():
			harvest()
		if get_ground_type() == Grounds.Soil:
			plant(Entities.Carrot)
		#else:
			#plant(Entities.Bush)			
		move(North)
		if can_harvest():
			harvest()
		if get_ground_type() == Grounds.Soil:
			plant(Entities.Carrot)
		else:
			plant(Entities.Bush)	
	#break
	move(East)
	for j in range(get_world_size() - 1):
		if can_harvest():
			harvest()
		if get_ground_type() == Grounds.Soil:
			plant(Entities.Carrot)
		#else:
			#plant(Entities.Bush)	
		move(South)
		if can_harvest():
			harvest()
		if get_ground_type() == Grounds.Soil:
			plant(Entities.Carrot)
		else:
			plant(Entities.Bush)	
	#move(East)
	#break
	
		