#!/usr/bin/env python

import os
from os import system as shell
import subprocess as sp 
import shutil
from ase import io


ads_path = '/work/common/hxin_lab/hspillai/Nitrate/yang/calculations/111/NHO/bidentate_bridge/'

metals = ['Au']

for metal in metals:
    path = ads_path + metal
    atoms = io.read(path + '/qn.traj')
    print(metal, atoms.get_potential_energy())
    io.write('CONTCAR' + '_' + metal, atoms)
