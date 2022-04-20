#!/usr/bin/env python

import os
from os import system as shell
import subprocess as sp 
import shutil
from ase import io


no3_path = '/work/common/hxin_lab/hspillai/Nitrate/yang/calculations/AllData/NO3/'

sites = {'atop' : ['Cu'],
         'bridge': ['Ag', 'Au', 'Ir', 'Ni', 'Pd', 'Pt', 'Rh'],
         'hollow': []}

for site in sites:
    metals = sites[site]
    for metal in metals:
        path = no3_path + site + '/' + metal
        print(path)
        atoms = io.read(path + '/qn.traj')
        print(atoms)
        io.write('CONTCAR' + '_' + metal, atoms)
#        shutil.copy(path + "/CONTCAR", "./CONTCAR" + '_' + metal)
#                shell("chmod +x Script.py")

#                shell("perl -pi -e 's/SYM/" + elem
#                      + "/g' Script.py")

    
