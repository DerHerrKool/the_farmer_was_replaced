change_hat(Hats.Purple_Hat)
set_world_size(32)
set_execution_speed(128)
def ground_soiling():
	if get_ground_type() != Grounds.Soil:
		till()

counter = 1
pumpkin_num = 0
stop = False
while stop == False:
	harvest_pumpkin = True
	for x in range(get_world_size()):
		for y in range(get_world_size()):
			ground_soiling()
			if get_entity_type() == Entities.Dead_Pumpkin or get_entity_type() == None:
				harvest_pumpkin = False
				plant(Entities.Pumpkin)
			move(North)
		move(East)
	if harvest_pumpkin:
		harvest()
		pumpkin_num += 1
		print(pumpkin_num)
		if pumpkin_num == counter:
			stop = True
		