executable           = run_make_trees.sh 
output               = std_make_trees_$(ClusterId)_$(ProcId)
error                = std_make_trees_$(ClusterId)_$(ProcId)
log                  = log_make_trees_$(ClusterId)_$(ProcId)

transfer_input_files = makeTreeCHS.py,

#arguments            = 94X /eos/user/s/singhr/jme_ntuples/dy_inc_2017/cut_pt10/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8.root
arguments            = 102X /eos/user/j/jiyoo/pileupTrain/MCUL18_DY_MG.root

+JobFlavour          = "espresso"
MaxTransferOutputMB = -1

queue
