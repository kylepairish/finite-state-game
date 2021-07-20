#!/usr/bin/env python3

class Engine():
    def __init__(self, first_scene):
        self.first_scene = first_scene

    def play(self):
        current_scene = self.first_scene.opening_scene()

        while True:
            print("\n---------")
            next_scene_name = current_scene.enter()
            current_scene = self.first_scene.next_scene(next_scene_name)

class First():
    def enter(self):
        print("this is the first map")

class Map():
    scenes = {'first': First()}

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('first')
a_game = Engine(a_map)
a_game.play()


