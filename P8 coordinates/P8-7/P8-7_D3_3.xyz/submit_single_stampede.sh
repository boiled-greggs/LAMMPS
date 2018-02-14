#!/bin/bash

#-      bash submit_single_stampede.sh -N numbernodes -np numberoftasks -t latticetype -c latticeconstant -s structure
#-
#-      comet has 24 nodes per core.
#-      stampede has 16 nodes per core.

# ALLOCATIONS
xsede=TG-TRA140037
terro=TG-DMR160090

# INPUT
while [[ $# > 1 ]]; do
        key="$1"

        case $key in
                -i|--input)
                infile="$2"
                shift # past argument
                ;;
                *)
                echo "Unkown option."
                exit
                    # unknown option
                ;;
        esac
        shift # past argument or value
done
# INPUT PARAMETERS
args=()
i=0
while read line 
do
    args[i]=$line
    i=$(($i + 1))
done < "$infile"

queue="${args[0]}"
nodes="${args[1]}"
procs="${args[2]}"
latttype="${args[3]}"
lattconst="${args[4]}"
deform="${args[5]}"
struct="${args[6]}"
echo "bash submit_single_stampede.sh $queue $nodes $procs
	$latttype $lattconst
	$deform $struct" > README.md


# Determine the host
host=$(hostname)
set -- "$host"
IFS="."; declare -a array=($*)
echo "${array[@]}"
flag="${array[1]}"
IFS=" "

case "$flag" in
        "stampede")
                cluster="$flag"
                partition=$queue
                cpern=16

		runfiles=/home1/03561/alarcj/LAMMPS
		cp ${runfiles}/stampede_single.sh .
		;;
        "sdsc")
                cluster=comet
                files=/oasis/scratch/comet/alarcj/temp_project/AMINO/data/op_run
                partition=compute
                echo "Running on comet.sdsc.xsede.org"
                ;;
        *)
                echo "Unkown option."
                exit
esac

sbatch -A $xsede -p $partition -N $nodes -n $procs -J $struct stampede_single.sh $procs $latttype $lattconst $deform $struct
