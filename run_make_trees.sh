#!/bin/bash
echo "Starting"
source /cvmfs/sft.cern.ch/lcg/views/LCG_96python3/x86_64-centos7-gcc8-opt/setup.sh
chmod +x makeTreeCHS.py
python makeTreeCHS.py --inputFiles=/eos/user/j/jiyoo/pileupTrain/MCUL18_DY_MG.root
