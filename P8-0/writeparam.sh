#!/bin/bash

for subdir in */; 
do
	sed -i "$ s/.*/${subdir::-1}/" parameters.md
	cp parameters.md ${subdir}
done
