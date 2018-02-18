# coding=utf-8
from __future__ import division
from bearlibterminal import terminal as blt
from random import randint, choice
import time

def mainloop():
    debug_value = 0
    debug_string = (" debug")
    screen_width = 120
    screen_height = 40
    map_x = 0
    map_y = 0
    BASE_damage = 5
    player_infight = False
    player_alive = True
    player_lvl = 1
    player_EXP = 0
    player_stat1 = 5
    player_stat2 = 5
    player_stat3 = 5
    blt.set("window.title='pythonRPG'")
    blt.clear()
    blt.color("white")
    debug_view = ("[color=orange]Debug string:" + debug_string + "[/color]]") #make string in puts rather than
    blt.puts(2, 3, debug_view)                                                #create another variable
    blt.refresh()
    time.sleep(5)
    

if __name__ == "__main__":
    blt.open()
    blt.set("window: size=120x40, cellsize=auto, title='pythonRPG'; font: default")
    blt.color("white")
    mainloop()
    blt.close()
