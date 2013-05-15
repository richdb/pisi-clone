#-*-coding: utf-8-*-

import os
from pisi.util import colorize
from pisi.api import list_installed

def get_default_packs(default_package_list):
  flag = 0
  
  print colorize("pisi history extraction...","cyan")
  os.system("pisi hs > history.lst")
  print colorize("done!","green")
  
  print colorize("default package extraction...","cyan")
  f = open("history.lst","r")
  
  for line in f:
    if "Operation #2:" in line:#find Operation #2 label for core package list
      flag = 1#raise first flag
      continue
    
    if flag >= 1 and flag != 3:#move pointer two line below
      flag = flag + 1
      continue
    
    if flag == 3:#get package list one by one
      temp = line.split(' ')
      
      if "\n" in temp[0]:#if pack list is finished
  break# terminate loop
      
      default_package_list.append(temp[5])
      
  f.close()
  print colorize("done!","green")
  default_package_list.sort()#sort package list
  
def extract_list():
  """ Gets installed Pisi packages by user """
  print colorize("getting list of all installed packages...","cyan")
  installed_packages = list_installed()#get all installed packages
  installed_packages.sort()
  print colorize("done!","green")
  
  print colorize("getting list of default package list...","cyan")
  default_package_list = []
  get_default_packs(default_package_list)#get default package list
  print colorize("done!","green")
  
  print colorize("comparison of lists...","cyan")
  fup = open("userpacks.lst","w")
  #compare lists  
  for line in installed_packages:
    if line not in default_package_list:
      fup.write(line + "\n")
  fup.close()
  print colorize("done!","green")
