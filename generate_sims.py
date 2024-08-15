#!/usr/bin/env python3
from os import system

simulation_days = 5
casenames = ["2D1",
             #"2D2",
             ]


with open('Templates/basic-sub.template', 'r') as f:
    pbs_script = f.read()

verbose = 1
pbs_filename = 'run_sim.sh'
for casename in casenames:
    if verbose: print(casename)
    pbs_case = pbs_script.format(casename,simulation_days)

    with open(pbs_filename, 'w+') as f:
        f.write(pbs_case)

    cmd_run = f'qsub {pbs_filename}'
    if verbose: print(cmd_run)
    system(cmd_run)

    print()