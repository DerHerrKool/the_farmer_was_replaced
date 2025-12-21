change_hat(Hats.Purple_Hat)
set_world_size(8)
set_execution_speed(1)

import farm_utils
# task to farm a line, reading crop info from its current x position
def task():
	x = get_pos_x()
	crop = crops[x]
	farm_utils.plant_column(x, crop)
	while True:
		farm_utils.farm_column(x, crop)

# list of crops, one per column
crops = [
 Entities.Tree,
 Entities.Carrot,
 Entities.Pumpkin,
 Entities.Cactus,
 Entities.Sunflower,
 Entities.Grass,
 # ...
]
# assign one drone per crop line
for i in range(get_world_size()):
 if spawn_drone(task):
  move(North)  # move east to assign the next drone
# the main drone farms the last line itself
task()

