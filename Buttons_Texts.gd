extends Control

# Declare member variables here. Examples:
var init_pos = []			#Indica la ubicacion de la ciudad origen
var alg = 0					#Indica el algoritmo a implementar
var next_scene = preload("res://Mapa.tscn")



# Called when the node enters the scene tree for the first time.
func _ready():
	pass


# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass

# Boton seleccionado
func _on_Button_pressed():
	get_node("VBoxContainer/HBoxContainer/Ciudad").text="Veracruz"
	init_pos= [275.627,86.971]
	get_node("VBoxContainer/HBoxContainer2/Algortimo").text=str(init_pos[0])


func _on_Button2_pressed():
	get_node("VBoxContainer/HBoxContainer/Ciudad").text="Boca del rio"
	init_pos= [602.27,150.973]
	get_node("VBoxContainer/HBoxContainer2/Algortimo").text=str(init_pos[0])

func _on_Button3_pressed():
	get_node("VBoxContainer/HBoxContainer/Ciudad").text="Medellin"
	init_pos= [283.421,192.978]
	get_node("VBoxContainer/HBoxContainer2/Algortimo").text=str(init_pos[0])

func _on_Button4_pressed():
	get_node("VBoxContainer/HBoxContainer/Ciudad").text="Poza Rica"
	init_pos= [46.935,-108.112]
	get_node("VBoxContainer/HBoxContainer2/Algortimo").text=str(init_pos[0])

func _on_Button5_pressed():
	get_node("VBoxContainer/HBoxContainer/Ciudad").text="Xalapa"
	init_pos= [-85.776,-79.924]
	get_node("VBoxContainer/HBoxContainer2/Algortimo").text=str(init_pos[0])

func _on_Button6_pressed():
	get_node("VBoxContainer/HBoxContainer/Ciudad").text="Cordoba"
	init_pos= [-345.981,260.698]
	get_node("VBoxContainer/HBoxContainer2/Algortimo").text=str(init_pos[0])

func _on_Button7_pressed():
	get_node("VBoxContainer/HBoxContainer/Ciudad").text="Orizaba"
	init_pos= [-121.488,259.151]
	get_node("VBoxContainer/HBoxContainer2/Algortimo").text=str(init_pos[0])

func _on_Button8_pressed():
	get_node("VBoxContainer/HBoxContainer/Ciudad").text="Cardel"
	init_pos= [25.421,-6.087]
	get_node("VBoxContainer/HBoxContainer2/Algortimo").text=str(init_pos[0])

func _on_Button9_pressed():
	get_node("VBoxContainer/HBoxContainer/Ciudad").text="Cotaxtla"
	init_pos= [523.288,188.553]
	get_node("VBoxContainer/HBoxContainer2/Algortimo").text=str(init_pos[0])

func _on_Iniciar_pressed():
	#var thing = load("res://Agente.gd").new(init_pos,alg) # Instancia de Mapa.gd mandando datos a su constructor
	#print (thing.get_val()) # print out the value of thing
	get_tree().change_scene_to(next_scene)
