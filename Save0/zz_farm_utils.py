# farm_utils.py
def plant_column(x, crop):
 # Plant an entire column with a given crop.
 # Handles special planting rules for trees and sunflowers.
 
 need_till_list = [Entities.Tree, Entities.Carrot, Entities.Pumpkin, Entities.Cactus, Entities.Sunflower]
 
for i in range(get_world_size()):
  # Some crops require tilling before planting
   if crop in need_till_list:
	  till()
  
  # Always water before planting
use_item(Items.Water)
  # Alternate trees and sunflowers in a checkerboard pattern
if crop == Entities.Tree:
   y = get_pos_y()
   if (x + y) % 2 == 0:
	  plant(Entities.Tree)
   else:
	  plant(Entities.Sunflower)
	  else:
	  plant(crop)
  
move(East)

def farm_column(x, crop):
 # Maintain and replant a crop column indefinitely.
 # Checks if harvestable, waters if dry, replants if empty or dead.
 
 can_plant_list = [None, Entities.Dead_Pumpkin, Entities.Grass]
 
for i in range(get_world_size()):
  # Harvest if ready
  if can_harvest():
   harvest()
   # Check soil moisture before replanting
   if get_water() < 0.5:
	  use_item(Items.Water)
  # Replant on empty, grass, or dead tiles
  if get_entity_type() in can_plant_list:
	  if crop == Entities.Tree:
	  y = get_pos_y()
   if (x + y) % 2 == 0:
	  plant(Entities.Tree)
   else:
	  plant(Entities.Sunflower)
	  else:
	  plant(crop)
move(East)