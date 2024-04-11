from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
ground = Entity(model= 'plane',
				texture= 'grass',
				collider= 'mesh',
				scale= (100,1,100))

player = FirstPersonController(
	collider='box')

myBox = Entity(model= 'cube',
               color= color.black,
               collider= 'box',
               position= (15, 0.5, 5))
myBall = Entity(model= 'sphere',
				color= color.red,
				collider= 'sphere',
				position= (5, 0.5, 10))

blocks = []
directions = []
window.fullscreen = True
from random import uniform

for i in range(8):
	r = uniform(-2,2)
	block = Entity(
		model='cube',
		color=color.azure,
		texture='white_cube',
		position=(r, 1+i , 3+i*5),
		scale=(3,0.5,3),
		collider='box'
	)
	if r < 0:
		directions.append(1)
	else:
		directions.append(-1)
	blocks.append(block)

goal = Entity(
	color=color.gold,
	model='cube',
	texture='white_cube',
	position=(0,7,47),
	scale=(10,1,10),
	collider='box'
)
pillar = Entity(
	color=color.green,
	model='cube',
	position=(0,33,47),
	scale=(1,52,1)
)
sky = Sky()
lvl = 1
def update():
	global lvl
	i = 0
	for block in blocks:
		block.x -= directions[i]*time.dt
		if abs(block.x) > 5:
			directions[i] *= -1
		if block.intersects().hit:
			player.x -= directions[i]*time.dt
		i = i + 1
	if player.z > 46 and lvl == 1:
		lvl = 2
		sky.texture = 'sky_sunset'

	def input(key):
		if key == 'q':
			quit()

app.run()