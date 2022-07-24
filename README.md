# pileUpStudies

These files currently are based on https://github.com/singh-ramanpreet/PUJetId_training_plotting
- Currently updated for JMENano files
- To do: change to C++ or uproot for speed

### running interactively on lxplus
#### make preprocessed trees 

```
source /cvmfs/sft.cern.ch/lcg/views/LCG_96python3/x86_64-centos7-gcc8-opt/setup.sh

python makeTreeCHS.py --inputFiles=/eos/user/j/jiyoo/pileupTrain/MCUL18_DY_MG.root
```

#### do training

```
mkdir BDT_chs_94X
 
python train_bdt.py --eta_bins Eta0p0To2p5
```
- the above only does training for the one bin cited above


### submitting jobs on HTCondor on lxplus

#### make preprocessed trees 

```
condor_submit submit.sh
```

#### do training
- assumes output directory created in home directory for log files
- also assumes directory on /eos created for output, currently @ /eos/user/j/jiyoo/condor1/

```
condor_submit submit_train_bdt.sub
```

### to do
- add functionality to loop over all 4 eta bins in script
- debug args arguments 


### other
- resources
  - https://chtc.cs.wisc.edu/uw-research-computing/file-availability.html#output
  - https://batchdocs.web.cern.ch/index.html

- change queue as needed
```
espresso     = 20 minutes
microcentury = 1 hour
longlunch    = 2 hours
workday      = 8 hours
tomorrow     = 1 day
testmatch    = 3 days
nextweek     = 1 week
```
- condor_submit FILENAME.sh
- condor_rm JOBNUMBER
- condor_q
- condor_q -hold
