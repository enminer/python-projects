from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

for z in range(10):
	for x in range(10):
		Entity(
			model="cube",  color=color.dark_gray, collider="box", ignore=True,
			position = (x, 0 ,z),
			parent=scene,
			origin_y = 0.5,
			texture = "white_cube"  	
		)

class TextureBox(Button):
	def __init__(self, position=(5,2,5)):
		super().__init__(
			parent=scene,
			position=position,
			model="cube",
			origin_y=0.5,
			texture="blue.jpg",
			color=color.color(0,0,1)
		)

		self.texture_choice = 0
		self.textures = ["blue.jpg", "wood.jpg", "stone.jpg"]

	def input(self, key):
		if self.hovered:
			if key == 'left mouse down':
				self.texture_choice += 1
				self.texture_choice %= len(self.textures)
				self.texture = self.textures[self.texture_choice]

TextureBox()

player = FirstPersonController()
app.run()