import sys

sys.path.append('../packages')
#Above, append the address of where you have stored the world_cup package on your computer. 

from world_cup.stadia.stadium_manager import *

print(open())

from world_cup.ticketing import corporate as corporate_ticketing
from world_cup.ticketing import standard as standard_ticketing

print(corporate_ticketing.corporate())
print(standard_ticketing.standard())

from world_cup.hospitality import corporate as corporate_hospitality
from world_cup.hospitality import standard as standard_hospitality

print(corporate_hospitality.corporate())
print(standard_hospitality.standard())

from world_cup.media.internet import view_game
from world_cup.media.radio import hear_game
from world_cup.media.tv import view_game as tv_game

print(view_game())
print(hear_game())
print(tv_game())

print(close())


