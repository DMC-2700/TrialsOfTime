import Room
import Person
import Init_Rooms
import Init_Player

from tkinter import *

imageArea = None

## function to draw image
def drawimage(imagelocation):
    global new_image
    new_image = PhotoImage(file=imagelocation)
    canvas.itemconfig(imageArea, image=new_image)

## Create the first room in the game
initialroom = Room.Room()
initialroom.name = 'Welcome Screen'
initialroom.narrative = 'Welcome to the game'
initialroom.image = ('images\\2021-04-02.png')

## Create the end room in the game
endroom = Room.Room()
endroom.name = 'Game Over'
initialroom.narrative = 'This is the end'
endroom.image = ('images\\Unnamed.png')

## Init all rooms in game
Init_Rooms.init_Rooms(initialroom)

## init hero
print("Initializing the player")
player = Init_Player.init_Player()
player.room = initialroom
current_room = initialroom

## Draw the first image of the game
print("Initializing the canvas")
tk = Tk()
canvas = Canvas(tk, width = 800, height = 600)
canvas.pack()

def forward(evt):
    print("Forward")
    
    global current_room
    global player

    player.forward()
    
    if current_room == player.room: ## If room does not change, means player can't move. Send player to start again.
        drawimage(endroom.image)
        player.room = initialroom
        current_room = initialroom
    else:
        current_room = player.room
        drawimage(current_room.image)

def backward(evt):
    print("Backward")
    global current_room
    global player

    player.backward()
    
    if current_room == player.room: ## If room does not change, means player can't move. Send player to start again.
        drawimage(endroom.image)
        player.room = initialroom
        current_room = initialroom
    else:
        current_room = player.room
        drawimage(current_room.image)

def left(evt):
    print("Left")
    global current_room
    global player

    player.left()
    
    if current_room == player.room: ## If room does not change, means player can't move. Send player to start again.
        drawimage(endroom.image)
        player.room = initialroom
        current_room = initialroom
    else:
        current_room = player.room
        drawimage(current_room.image)

def right(evt):
    print("Right")
    global current_room
    global player

    player.right()
    
    if current_room == player.room: ## If room does not change, means player can't move. Send player to start again.
        drawimage(endroom.image)
        player.room = initialroom
        current_room = initialroom
    else:
        current_room = player.room
        drawimage(current_room.image)
    
## Bind key press
print("Binding keys")
canvas.bind_all('<KeyPress-Up>', forward)
canvas.bind_all('<KeyPress-Down>', backward)
canvas.bind_all('<KeyPress-Left>', left)
canvas.bind_all('<KeyPress-Right>', right)

print("Drawing the gamescreen")
print(player.room.narrative)
my_image = PhotoImage(file=player.room.image)
imageArea = canvas.create_image(0, 0, anchor=NW, image=my_image)
