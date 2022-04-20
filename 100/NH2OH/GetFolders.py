#!/usr/bin/env python

import os
from os import system as shell
import subprocess as sp 
import shutil
from ase import io


ads_path = '/projects/hxin_lab_storage/hspillai/4-nitrate/AllMetals/NH2OH/ontop/rotate_45/'

sites = {'bidentate_bridge' : ['Au', 'Cu', 'Rh'],
         'ontop': ['Ag', 'Ir', 'Ni', 'Pd', 'Pt'], 
         'monodentate_bridge': []}

metals = ['Au', 'Cu', 'Ag', 'Rh', 'Ir', 'Pt', 'Ni', 'Pd']

for metal in metals:
    path = ads_path + metal
    atoms = io.read(path + '/qn.traj')
    print(metal, atoms.get_potential_energy())
    io.write('CONTCAR' + '_' + metal, atoms)
    
# for site in sites:
#     metals = sites[site]
#     for metal in metals:
#         path = ads_path + site + '/' + metal
#         atoms = io.read(path + '/qn.traj')
#         print(metal, atoms.get_potential_energy())
#         io.write('CONTCAR' + '_' + metal, atoms)

    
