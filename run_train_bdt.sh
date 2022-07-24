#!/bin/bash
echo "Setting Env"
source /cvmfs/sft.cern.ch/lcg/views/LCG_96python3/x86_64-centos7-gcc8-opt/setup.sh

era=$1
max_N=$2
jet_type=$3
in_dir=$4
d_name="BDT_chs_94X"
eta_bin=$5

mkdir -p output
cd output

ls 
#mkdir -p $d_name

mkdir -p BDT_chs_94X

ls

chmod +x ../train_bdt.py
#python ../train_bdt.py --era $era --max_N $max_N --jet_type $jet_type --in_dir $in_dir --d_name $d_name --eta_bins $eta_bin

python ../train_bdt.py --eta_bins Eta2p5To2p75 --in_dir /afs/cern.ch/user/j/jiyoo/pileupTestTrain/ --d_name $d_name --max_N 500000

ls -al BDT_chs_94X

cd ../

tar -czvf my_job.output.tar.gz output/BDT_chs_94X/

ls -al
