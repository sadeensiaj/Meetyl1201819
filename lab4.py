class Animal(object):
	def __init__(self, sound, name,age,fv_color):
		self.sound = sound
		self.name = name
		self.age = age
		self.fv_color = fv_color
	def eat(self,food):
			print('yummy!! ' + self.name + 'is eating' + food)
	def description(self):
			print(self.name + 'is' + self.age + 'years old loves the color ' + self.fv_color)
a = Animal('meow','bunny', 3,'blue')
a.eat()