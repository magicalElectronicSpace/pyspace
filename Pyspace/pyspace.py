import tkinter as tk
import random


class Weapon:
    def __init__(self, name, strength, evolution):
        self.name = name
        self.strength = strength
        self.level = 1
        self.evolution = evolution
        

class Whip(Weapon):
    def __init__(self):
        super().__init__("Whip", 2, FireWhip())
        
        

    
    

    def levelUp(self):
        nydict = {"evolved": False}
        self.level += 1
        if self.level == 2:
            self.strength += 2
        elif self.level == 3:
            self.strength += 4
        elif self.level == 4:
            self.strength += 6
        elif self.level == 5:
            self.strength += 4
        elif self.level == 6:
            self.strength += 3
        elif self.level == 7:
            self.strength += 2
        elif self.level == 8:
            self.strength += 1
        elif self.level == 9:
            nydict["evolved"] = True
        
        return nydict
            

        


class Sword(Weapon):
    def __init__(self):
        super().__init__("Sword", 5)

class Evolution(Weapon):
    def __init__(self, name, base):
        super.__init__(name, base.strength + base.strength)
        self.name = name
        self.base = base
        self.strength = base.strength + base.strength
        self.__dict__.update(base.__dict__)


class FireSword(Evolution):
    def __init__(self): 
        super.__init__("Fire Sword", Sword())
        self.base = Sword()

class IceSword(Evolution):
    def __init__(self):
        super.__init__("Ice Sword", FireSword())
        self.base = FireSword()
    
class ThunderSword(Evolution):
    def __init__(self):
        super.__init__("Thunder Sword", IceSword())
        self.base = IceSword()

class FireWhip(Evolution):
    def __init__(self):
        super.__init__("Fire Whip", Whip())
        self.base = Whip()

class IceWhip(Evolution):
    def __init__(self):
        super.__init__("Ice Whip", FireWhip())
        self.base = FireWhip()

class ThunderWhip(Evolution):
    def __init__(self):
        super.__init__("Thunder Whip", IceWhip())
        self.base = IceWhip()

class FlashSword(Evolution):
    def __init__(self):
        super.__init__("Flash Sword", ThunderSword())
        self.base = ThunderSword()

class FlashWhip(Evolution):
    def __init__(self):
        super.__init__("Flash Whip", ThunderWhip())
        self.base = ThunderWhip()

class ZingShot(Weapon):
    def __init__(self):
        super().__init__("Zing Shot", 30)


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Character:
    def __init__(self, name="Arlo", char="A", health=1000, weapon=Whip(), coordinate=Coordinate(0, 0), type="computer", tkintert=False):
        self.name = name
        self.char = char
        self.health = health
        self.weapon = weapon
        self.coordinate = coordinate
        self.tkintert = tkintert
        self.type = type
        self.xp = 0
        self.tkroot = tk.Tk()

    def set_coordinate(self, coordinate):
        self.coordinate = coordinate
    
    def get_coordinate(self):
        return self.coordinate
    
    
    def move(self, direction):
        if direction == "up":
            self.coordinate.y += 1
        elif direction == "down":
            self.coordinate.y -= 1
        elif direction == "left":
            self.coordinate.x -= 1
        elif direction == "right":
            self.coordinate.x += 1

    def gain_health(self, health):
        self.health += health



    def attack(self, character):
        character.health -= self.weapon.strength
        self.xp += 1
        if self.tkintert:
            label = tk.Label(self.tkroot, text=f"{self.name} attacked {character.name} with {self.weapon.name} and dealt {self.weapon.strength} damage.")
            label.pack(pady=10)
        else:
            print(f"{self.name} attacked {character.name} with {self.weapon.name} and dealt {self.weapon.strength} damage.")



class GridWorld:    
    def __init__(self, height, width, characters=[]):
        self.height= height
        self.width = width
        self.characters = characters
        self.tkroot = tk.Tk()
    

    def add_character(self, character):
        self.characters.append(character)


    def draw_with_console(self, show_coordinates=True, show_health=True):
        if show_coordinates:
            for row in range(self.height):
                for column in range(self.width):
                    found = False
                    for character in self.characters:
                        if character.coordinate.x == column and character.coordinate.y == row:
                            if self.height - 1 == row:
                                print(character.char)
                            else:
                                print(character.char, end=" ")
                            found = True
                            break
                    if not found:
                        if self.height - 1 == row:
                            print(" ")
                        else:
                            print(" ", end=" ")
                    
        if show_health:
            for character in self.characters:
                print(character.name + f" ({character.char})" + ":" + str(character.health))
            
    def draw_with_tkinter(self, show_coordinates=True, show_health=True):
        root = self.tkroot
        root.title("Grid World")
        root.geometry("400x400")
        canvas = tk.Canvas(root, width=400, height=400)
        canvas.pack()
        if show_coordinates:
            for row in range(self.height):
                for column in range(self.width):
                    found = False
                    for character in self.characters:
                        if character.coordinate.x == column and character.coordinate.y == row:
                            canvas.create_text(column*50, row*50, text=character.char)
                            found = True
                            break
                    if not found:
                        canvas.create_text(column*50, row*50, text=" ")
        if show_health:
            for character in self.characters:
                canvas.create_text(character.coordinate.x*50, character.coordinate.y*50, text=character.name + f" ({character.char})" + ":" + str(character.health))
        root.mainloop()

    def draw(self, type="console", show_coordinates=True, show_health=True):
        if type == "console":
            self.draw_with_console(show_coordinates=show_coordinates, show_health=show_health)
        elif type == "tkinter":
            self.draw_with_tkinter(show_coordinates=show_coordinates, show_health=show_health)