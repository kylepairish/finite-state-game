#!/usr/bin/env python3

from random import randint

class Player:
    MANA = 100
    AGILITY = 5
    STRENGTH = 5
    DEXTERITY = 5
    
    def __init__(self, hero):
        self.hero = hero
        self.health = 100
        self.armor = 50
    
    def get_health(self):
        return self.health

    def get_armor(self):
        return self.armor


class Monster:

    def __init__(self, name):
        self.name = name
        self.health = 200

    def dialogue(self):
        print("I am the {}! I am here to crush your soul peasant!".format(self.name))

    def attack(self, player):
        if player.health > 0:
            swipe = randint(19,20)
            player.health -= swipe
            print("Swipe hits for " + str(swipe))
            if swipe == 20:
                player.armor -= swipe
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
        if self.armor < 100:
            print("Casting Ice Armor!")
            self.armor += 50
            print("Armor:", self.armor)

class Warlock(Player):

    def shadowbolt(self, monster):
        if monster.health > 0:
            shadowbolt = randint(30, 69)
            monster.health -= shadowbolt
            print("Shadowbolt hits for " + str(shadowbolt))
            if shadowbolt == 69:
                print("CRITICAL HIT!!")



    

    




        
