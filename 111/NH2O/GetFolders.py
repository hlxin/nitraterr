#!/usr/bin/env python

import os
from os import system as shell
import subprocess as sp 
import shutil
from ase import io

ads_path = '/projects/hxin_lab_storage/hspillai/4-nitrate/AllMetals/111/NH2O/bidentate_hollow/hcp/'

metals = ['Au']#, 'Cu', 'Ir', 'Pd', 'Pt']

for metal in metals:
    path = ads_path + metal
    atoms = io.read(path + '/qn.traj')
    print(metal, atoms.get_potential_energy())
    io.write('CONTCAR' + '_' + metal, atoms)
