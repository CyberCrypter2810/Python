# Base project format.
# put this on the desktop : git clone https://github.com/tritechsc/mcpi
from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep
from random import randint
import math


def init():
    mc = Minecraft.create("127.0.0.1", 4711)
    #mc = Minecraft.create("10.183.3.25", 4711)
    x, y, z = mc.player.getPos()		
    return mc

def clear_with_air_up(mc, x, y, z,h,k,l):
	air = 0;
	mc.setBlocks(x-h,y,z,x+h,y+k,z+l,air)	

def clear_with_air_block(mc, x, y, z,h,k,l):
	air = 0;
	mc.setBlocks(x-h,y-k,z-l,x+h,y+k,z+l,air)	

def layer (mc, x, y, z, s ,e,w, m):
	# s start , e end m material  , w width m material 
	w = int(w/2)
	print("w ",w)
	mc.setBlocks(x-w,y,z+s,x+w,y,z+e-1,m)
	
def layerc (mc, x, y, z, s ,e,w, m,c):
	# s start , e end m material  , aw width m material 
	w = int(w/2)
	print("w ",w)
	mc.setBlocks(x-w,y,z+s,x+w,y,z+e-1,m,c)

def body(mc,x, y, z):
	clear_with_air_up(mc, x, y, z,10,10,20)
	s,e,w = 0,17,5
	layer(mc, x,y,z+2,s,e,w,22)
	
	y  = y + 1; s,e,w = 0,16,5
	layer(mc, x,y,z+2,s,e,w,22)
	y = y + 1; s,e,w = 0,14,3
	layer(mc, x,y-1,z+2,s,e,w,0)
	y = y + 1; s,e,w = 0,1,5
	layerc(mc, x,y-2,z+2,s,e,w,35,14)
	y = y + 1; s,e,w = 0,1,3
	layerc(mc, x,y-3,z+2,s,e,w,35,0)
	y = y + 1; s,e,w = 0,1,1
	layer(mc, x,y-4,z+2,s,e,w,64)
	#print(x,y,z,s,e,w)
	#mc.setBlock(x, y, z+1, 64, 0)
	#mc.setBlock(x+1, y ,z+1, 64, 8)
	#mc.player.setPos(x,y,z-1)
	y = y + 1; s,e,w = 15,16,1
	layer(mc, x-2,y-5,z+2,s,e,w,42)
	y = y + 1; s,e,w = 15,16,1
	layer(mc, x+2,y-6,z+2,s,e,w,42)
	
	y = y + 1; s,e,w = 0,1,1
	layer(mc, x,y-6,z+2,s,e,w,6)
	y = y + 1; s,e,w = 0,15,5
	layer(mc, x,y-7,z+2,s,e,w,20)
	y = y + 1; s,e,w = 0,14,3
	layer(mc, x,y-8,z+2,s,e,w,0)
	y = y + 1; s,e,w = 0,1,5
	layer(mc, x,y-9,z+2,s,e,w,22)
	y = y + 1; s,e,w = 0,1,1
	layer(mc, x,y-10,z+2,s,e,w,0)
	
	
	y = y + 1; s,e,w = 0,14,5
	layer(mc, x,y-10,z+2,s,e,w,22)
	y = y + 1; s,e,w = 0,1,1
	layerc(mc, x-1,y-11,z+2,s,e,w,35,14)
	y = y + 1; s,e,w = 0,1,1
	layerc(mc, x+1,y-12,z+2,s,e,w,35,14)
	
	y  = y + 1; s,e,w = 0,14,5
	layer(mc, x,y-12,z+2,s,e,w,44)
	
	y = y + 1; s,e,w = 1,5,1
	layer(mc, x-2,y-18,z+2,s,e,w,49)
	y = y + 1; s,e,w = 2,4,1
	layer(mc, x-2,y-19,z+2,s,e,w,15)
	y = y + 1; s,e,w = 1,5,1
	layer(mc, x+2,y-20,z+2,s,e,w,49)
	y = y + 1; s,e,w = 2,4,1
	layer(mc, x+2,y-21,z+2,s,e,w,15)
	y = y + 1; s,e,w = 15,13,1
	layer(mc, x-2,y-22,z+2,s,e,w,49)
	y = y + 1; s,e,w = 14,14,1
	layer(mc, x-2,y-23,z+2,s,e,w,15)
	y = y + 1; s,e,w = 15,13,1
	layer(mc, x+2,y-24,z+2,s,e,w,49)
	y = y + 1; s,e,w = 14,14,1
	layer(mc, x+2,y-25,z+2,s,e,w,15)
	
	y = y + 1; s,e,w = 2,4,1
	layer(mc, x-2,y-27,z+2,s,e,w,49)
	y = y + 1; s,e,w = 2,4,1
	layer(mc, x+2,y-28,z+2,s,e,w,49)
	y = y + 1; s,e,w = 14,14,1
	layer(mc, x-2,y-29,z+2,s,e,w,49)
	y = y + 1; s,e,w = 14,14,1
	layer(mc, x+2,y-30,z+2,s,e,w,49)
	
def ring(mc,xs,ys,zs,r):
	y = ys
	count = 0
	for t in range (0,360,15):
		radians = (t * (3.141592/180))
		rval=randint(1,20)
		x = math.cos(radians) * r
		z = math.sin(radians) * r
		# raval is random number  and wc will be wool color
		wc = count % 7
		count = count +1
		mc.setBlocks(x,y,z,x,y+rval,z,35,wc)	
		print(t,x,y)
		
def main():
	mc = init()
	x, y, z = mc.player.getPos()
	ring(mc,x,y,z,10)
	ring(mc,x,y,z,20)
	ring(mc,x,y,z,30)	
	body(mc, x,y,z)

main()

# multiple line comment
"""
AIR                   0
STONE                 1
GRASS                 2
DIRT                  3
COBBLESTONE           4
WOOD_PLANKS           5
SAPLING               6
BEDROCK               7
WATER_FLOWING         8
WATER                 8
WATER_STATIONARY      9
LAVA_FLOWING         10
LAVA                 10
LAVA_STATIONARY      11
SAND                 12
GRAVEL               13
GOLD_ORE             14
IRON_ORE             15
COAL_ORE             16
WOOD                 17
LEAVES               18
GLASS                20
LAPIS_LAZULI_ORE     21
LAPIS_LAZULI_BLOCK   22
SANDSTONE            24
BED                  26
COBWEB               30
GRASS_TALL           31
WOOL                 35
FLOWER_YELLOW        37
FLOWER_CYAN          38
MUSHROOM_BROWN       39
MUSHROOM_RED         40
GOLD_BLOCK           41
IRON_BLOCK           42
STONE_SLAB_DOUBLE    43
STONE_SLAB           44
BRICK_BLOCK          45
TNT                  46
BOOKSHELF            47
MOSS_STONE           48
OBSIDIAN             49
TORCH                50
FIRE                 51
STAIRS_WOOD          53
CHEST                54
DIAMOND_ORE          56
DIAMOND_BLOCK        57
CRAFTING_TABLE       58
FARMLAND             60
FURNACE_INACTIVE     61
FURNACE_ACTIVE       62
DOOR_WOOD            64
LADDER               65
STAIRS_COBBLESTONE   67
DOOR_IRON            71
REDSTONE_ORE         73
SNOW                 78
ICE                  79
SNOW_BLOCK           80
CACTUS               81
CLAY                 82
SUGAR_CANE           83
FENCE                85
GLOWSTONE_BLOCK      89
BEDROCK_INVISIBLE    95
STONE_BRICK          98
GLASS_PANE          102
MELON               103
FENCE_GATE          107
GLOWING_OBSIDIAN    246
NETHER_REACTOR_CORE 247
"""
