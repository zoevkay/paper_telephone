from django.db import models

class User(models.Model):
	name = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	join_date = models.DateTimeField(auto_now_add=True)

class Game(models.Model):
	start_date = models.DateTimeField('date game began', auto_now=True)
	user = models.ForeignKey(User)
	# cycle = models.ForeignKey('Cycle')

# class Cycle(models.Model):
	# creation = models.ForeignKey('Doodle')
	# game = models.ForeignKey(Game)
	# user = models.ForeignKey(User)

class Doodle(models.Model):
	text = models.CharField(max_length=350, blank=True, null=True)
	drawing = models.URLField(blank=True, null=True)
	user = models.ForeignKey(User)
	# cycle = models.ForeignKey(Cycle)
	game = models.ForeignKey(Game)
	order = models.IntegerField()

