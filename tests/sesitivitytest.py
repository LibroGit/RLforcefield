from RLforcefield.rlff import sensitivity, filemanager

#top_path, pdb_path, xtc_path, dat_path = filemanager.sensitivity_file_manager()
top_path = "001_top.top"
pdb_path = "001_pdb.pdb"
xtc_path = "001_trajectory.xtc"
dat_path = "001_helix.dat"
filedir  = '/home/alireza/Desktop/myprojects/irbproject/rlff/RLforcefield/tests/samples'


sensitivity.claculate(top_path, pdb_path, xtc_path, dat_path, filedir)