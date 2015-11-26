#!/usr/bin/python
#
# Lacerda@Granada - 24/Mar/2015
#
from .objects import GasProp, runstats, H5SFRData, CALIFAPaths
from .plots import plot_zbins, plotOLSbisectorAxis
from .scripts import sort_gals, debug_var, loop_cubes, \
                     ma_mask_xyz, OLS_bisector, read_one_cube, \
                     get_morfologia, my_morf

paths = CALIFAPaths(work_dir = '/Users/lacerda/CALIFA/', v_run = -1)