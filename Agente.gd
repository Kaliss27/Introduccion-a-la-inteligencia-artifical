#A estrella
extends KinematicBody2D


# Declare member variables here. Examples:
var velocity = Vector2() 


# Called when the node enters the scene tree for the first time.
func _ready():
	pass	

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	var collision = move_and_collide(velocity * delta)
	velocity.x=100

