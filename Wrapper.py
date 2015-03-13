class RogueAPI(object) :
    def __init__(self) :
        pass

class Personnage(RogueAPI) :
    def __init__(self) :
        self.x = 0
        self.y = 0

    def move_right(self) :
        self.x = (self.x + 1)
    def move_left(self) :
        self.x = (self.x - 1)
    def move_up(self) :
        self.y = (self.y + 1)
    def move_down(self) :
        self.y = (self.y - 1)

    def get_x(self) :
        return self.x
    def get_y(self) :
        return self.y
    def set_x(self,x) :
        try :
            self.x = x
        except (e) :
            print(e)
    def set_y(self,y) :
        try :
            self.y = y
        except (e) :
            print(e)

    def get_coordinates(self) :
        return (self.x,self.y)
    def set_coordinates(self,x,y) :
        try :
            self.x = x
            self.y = y
        except (e) :
            print(e)
