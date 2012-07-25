from django.db import models

class User(models.Model)
	name = models.CharField(max_length=50)
	password = models.CharField(max_length=50)

class Game(models.Model)
	user = models.ForeignKey(User)
	sentence = models.ForeignKey('Sentence')
	drawing = models.ForeignKey('Drawing')
	start_date = models.DateTimeField(auto_now=True)

class Sentence(models.Model)
	text = models.CharField(max_length=350)
	game = models.ForeignKey(Game)
	user = models.ForeignKey(User)
	cycle = models.ForeignKey(Cycle)

class Drawing(models.Model)
	game = models.ForeignKey(Game)
	user = models.ForeignKey(User)
	cycle = models.ForeignKey(Cycle)

class Cycle(models.Model)
	user = models.ForeignKey(User)
	drawing = models.ForeignKey(Drawing) #could be Null!!
	sentence = 
