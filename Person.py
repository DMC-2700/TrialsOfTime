class Person():
    name = None
    room = None

    def forward (self):
        if self.room.forward is None:
            print("you slamed your face on the wall")
        else:
            self.room = self.room.forward
            
    def backward (self):
        if self.room.backward is None:
            print("you slamed your face on the wall")
        else:
            self.room = self.room.backward

    def left (self):
        if self.room.left is None:
            print("you slamed your face on the wall")
        else:
            self.room = self.room.left

    def right (self):
        if self.room.right is None:
            print("you slamed your face on the wall")
        else:
            self.room = self.room.right

