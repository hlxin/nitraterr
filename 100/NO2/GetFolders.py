#!/usr/bin/env python

import os
from os import system as shell
import subprocess as sp 
import shutil
from ase import io


no3_path = '/work/common/hxin_lab/hspillai/Nitrate/yang/calculations/AllData/NO2/'

sites = {'N_O' : ['Ir', 'Ni', 'Pd', 'Pt', 'Rh'],
         'O_O': ['Ag', 'Au', 'Cu']}

for site in sites:
    metals = sites[site]
    for metal in metals:
        path = no3_path + site + '/' + metal
        atoms = io.read(path + '/qn.traj')
        print(metal, atoms.get_potential_energy())
        io.write('CONTCAR' + '_' + metal, atoms)

    
