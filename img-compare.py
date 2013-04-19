from sys import argv
from os import system
  
for arg in argv[1:]:
  system("start " + arg)