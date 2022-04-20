#!/usr/bin/env python

import os
from os import system as shell
import subprocess as sp 
import shutil
from ase import io


ads_path = '/projects/hxin_lab_storage/hspillai/4-nitrate/AllMetals/NH2O/'

sites = {'bidentate_bridge' : ['Au', 'Cu', 'Rh'],
         'bidentate_hollow': ['Ag', 'Ir', 'Ni', 'Pd', 'Pt'], 
         'monodentate_bridge': []}

for site in sites:
    metals = sites[site]
    for metal in metals:
        path = ads_path + site + '/' + metal
        atoms = io.read(path + '/qn.traj')
        print(metal, atoms.get_potential_energy())
        io.write('CONTCAR' + '_' + metal, atoms)

    
