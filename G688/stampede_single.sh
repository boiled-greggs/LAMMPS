#!/bin/bash
#SBATCH --exclusive           # Individual nodes
#SBATCH -t 2-0                # Run time (hh:mm:ss)
#SBATCH -o slurm.%j.out
#SBATCH --mail-type=ALL
#SBATCH --mail-user=alarcj137@gmail.com

#~
#~	in.elastic calls	
#~
#~	init.mod : 	Input sturcture, lattice parameters and units.
#~	potential.mod :	Desired force field.
#~	displace.mod
#~


latttype=$1
lattconst=$2
deform=$3
struct=$4


# finite deformation size (1.0e-6)
#deform in 1.0e-5 5.0e-5 1.0e-6 5.0e-6 1.0e-7; do

# Modify the pair_coeff with respect to the number of atom types
#types=`awk 'FNR == 7 {print $1}' ${struct}`
#string=$(for ((i=1; i<=$types; i++)); do printf "%s" " C "; done)
#sed -i "s/CH.airebo C.*/CH.airebo ${string}/" potential.mod

lammps -var fname ${struct} -var up ${deform} -var lattype ${latttype} -var latconst ${lattconst} < in.elastic
# For rediretion '| tee filename'
#ibrun -np $procs lmp_stampede -var fname ${struct} -var up ${deform} -var lattype ${latttype} -var latconst ${lattconst} < in.elastic 
		


