#!/usr/bin/python
#-*-coding: utf-8-*-

import os
from extract_list import extract_list
from pisi.util import colorize

def menuPrinting():
  """ User menu of Pisi Clone application """
  print colorize('=' * 9 + 'Pisi Clone Menu' + '=' * 9,"yellow")
  print colorize('1-Update repository',"white")
  print colorize('2-Update Pisi',"white")
  print colorize('3-Extract package list from Pisi',"white")
  print colorize('4-Setup packages',"white")
  print colorize('0-Exit',"white")
  print colorize('=' * 24,"yellow")

def executeCode(ch):
  """ Menu choices """
  if ch == 1:
    os.system("sudo pisi ur")
    print "\n"
    
  elif ch == 2:
    os.system("sudo pisi up")
    print "\n"
    
  elif ch == 3:
    extract_list()
    print "\n"
    
  elif ch == 4:
    try:
      f = open("userpacks.lst","r")
      
      msg = ""
      for line in f:
  tmp = line.split("\n")
	msg = msg + tmp[0] + " "
      
      os.system("sudo pisi it " + msg)
      
      f.close()
    except IOError:
      print colorize("No such file named userpacks.lst in the same directory!","cyan")
    print "\n"
      
  elif ch == 0:
    exit()

def main_program():
  choice = 1
  
  while choice != 0:
    """ Menu loop """
    menuPrinting()
    choice = raw_input("Select one of them!\t")
    upperchoice=4
    lowerchoice=0
    
    if choice.isdigit() != True:
      print colorize("WRONG! Enter a NUMBER!\n","cyan")
      continue
    elif int(choice) > upperchoice or int(choice) < lowerchoice:
      print colorize("WRONG! Enter a VALID number!\n","cyan")
      continue
    else:
      executeCode(int(choice))

main_program()
