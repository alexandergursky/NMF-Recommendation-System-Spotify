#!/bin/bash

#SBATCH --mail-type=BEGIN,END
#SBATCH --mail-user=null@georgiasouthern.edu
#SBATCH --ntasks=32
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=4G
#SBATCH -p talon-part1

module load anaconda/anaconda3
python talon-nmf-sparse91.py
