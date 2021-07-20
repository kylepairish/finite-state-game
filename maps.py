#!/usr/bin/env python3
from hero import Mage
from hero import Monster

class MainMenu:

    def enter(self):
        print("you have arrived in Flasken! Where would you like to go next?")
        print("1. Stonehar")
        print("2. Riverways")
        print("3. Ariah")
        print("4. Hearthglen")

        selection = input("> ")

        if selection == '1':
            return 'Stonehar'
        elif selection == '2':
            return 'Riverways'
        elif selection == '3':
            return 'Ariah'
        elif selection == '4':
            return 'Hearthglen'


class Stonehar(MainMenu):

    def enter(self):
        print("You have entered Stonehar!\n")
        print("Go left for a fight or go right to move on to the next zone!\n")
        print("1. Left")
        print("2. Right")
        action = input(">  ")

        if action == '1':
            self.battle()
        elif action == '2':
            return 'Ariah'

    def battle(self):
        player = Mage('Mage')
        monster = Monster('Araxus')
        print("You have chosen to fight {}!".format(monster.name))
        monster.dialogue()
        print("Press 1 to hit him with a Fireball!")
        action = input("> ")
        if action == '1':
            player.fireball()
            print("Araxus HP: ", monster.get_health(), "\n") 
            monster.attack()
            print("{} HP: ".format(player.hero), player.get_health())
            print("{} ARMOR: ".format(player.hero), player.get_armor(), "\n")
            player.ice_armor()
            while monster.HEALTH > 50:
                print("Attack again! Press 1!")
                action = input("> ")
                if action == '1':
                    player.fireball()
                    print("Araxus HP: ", monster.get_health()) 
                    if monster.HEALTH < 50: 
                        print("Araxus escapes for now!")
            return Riverways().enter()


class Riverways(MainMenu):

    def enter(self):
        print("You have entered the Riverways!")

class Ariah(MainMenu):

    def enter(self):
        print("You have entered Ariah!")

class Hearthglen(MainMenu):

    def enter(self):
        print("You have entered Hearthglen!")

class Engine:

    def __init__(self, scene):
        self.scene = scene

    def play(self):
        current_scene = self.scene.opening_scene()

        while True:
            print("\n---------------")
            next_scene_name = current_scene.enter()
            current_scene = self.scene.next_scene(next_scene_name)


class Map():

    scenes = {'Mainmenu': MainMenu(),
              'Stonehar': Stonehar(),
              'Riverways': Riverways(),
              'Ariah': Ariah(),
              'Hearthglen': Hearthglen()
              }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)
    
    def opening_scene(self):
        return self.next_scene(self.start_scene) 


a_map = Map('Mainmenu')
a_game = Engine(a_map)
a_game.play()







