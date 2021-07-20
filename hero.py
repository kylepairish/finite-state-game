#!/usr/bin/env python3

from random import randint

class Player:
    HEALTH = 100
    MANA = 100
    AGILITY = 5
    STRENGTH = 5
    DEXTERITY = 5
    ARMOR = 50
    
    def __init__(self, hero):
        self.hero = hero
    
    def get_health(self):
        return self.HEALTH

    def get_armor(self):
        return self.ARMOR


class Monster:

    def __init__(self, name):
        self.name = name
        self.health = 200

    def dialogue(self):
        print("I am the {}! I am here to crush your soul peasant!".format(self.name))

    def attack(self):
        if Player.HEALTH > 0:
            swipe = randint(19,20)
            Player.HEALTH -= swipe
            print("Swipe hits for " + str(swipe))
            if swipe == 20:
                Player.ARMOR -= swipe
                print("CRITICAL HIT!! Your armor has been damaged!")

    def get_health(self):
        return self.health



class Mage(Player):

    def fireball(self, monster):
        if monster.health > 0:
             fireball = randint(40, 60)
             monster.health -= fireball
             print("Fireball hits for " + str(fireball))
             if fireball == 20:
                 print("CRITICAL HIT!!")

    def ice_armor(self):
        if self.ARMOR < 100:
            print("Casting Ice Armor!")
            self.ARMOR += 50
            print("Armor:", self.ARMOR)

class Warlock(Player):

    def shadowbolt(self, monster):
        if monster.health > 0:
            shadowbolt = randint(30, 69)
            monster.health -= shadowbolt
            print("Shadowbolt hits for " + str(shadowbolt))
            if shadowbolt == 69:
                print("CRITICAL HIT!!")



    

    




        
