import ROOT
from array import array
import argparse

parser = argparse.ArgumentParser(
    description="make TTrees for training"
    )
parser.add_argument(
    "--era", type=str, default="94X", help="MC era, like 94X, 102X"
    )
parser.add_argument(
    "--inputFiles", type=str, default=[], nargs="+", help="MC era, like 94X, 102X"
    )

args = parser.parse_args()

era = args.era
inputFiles = args.inputFiles

tChain  = ROOT.TChain("Events")
outFile = ROOT.TFile("training_trees_pt10To100_puppi_%s.root" % era, "RECREATE")

for inputFile in inputFiles:
    tChain.Add(inputFile)

eta_bins = [
    "Eta0p0To2p5" ,
    "Eta2p5To2p75",
    "Eta2p75To3p0",
    "Eta3p0To5p0" ,
]

outTrees = []

for eta_bin in eta_bins:
    outTrees.append(ROOT.TTree(eta_bin + "_Prompt", eta_bin + "_Prompt"))
    
for eta_bin in eta_bins:
    outTrees.append(ROOT.TTree(eta_bin + "_Pileup", eta_bin + "_Pileup"))

def book_float_branch(ttree, branch_name, default_value=-999.0):
    branch_array = array("f", [default_value])
    ttree.Branch(branch_name, branch_array, "%s/F" % branch_name)        
    return branch_array

def book_int_branch(ttree, branch_name, default_value=-999):
    branch_array = array("i", [default_value])
    ttree.Branch(branch_name, branch_array, "%s/I" % branch_name)        
    return branch_array

NTrees = len(outTrees)

PV_npvsGood = NTrees*[0]
JetPuppiSel_puId_dR2Mean  = NTrees*[0]
JetPuppiSel_puId_jetR = NTrees*[0]
JetPuppiSel_puId_jetRchg = NTrees*[0]
JetPuppiSel_puId_nParticles = NTrees*[0]
JetPuppiSel_puId_nCharged = NTrees*[0]
JetPuppiSel_puId_pull = NTrees*[0]
JetPuppiSel_pt           = NTrees*[0]
JetPuppiSel_eta          = NTrees*[0]
JetPuppiSel_puId_majW            = NTrees*[0]
JetPuppiSel_puId_minW           = NTrees*[0]
JetPuppiSel_puId_frac01          = NTrees*[0]
JetPuppiSel_puId_frac02          = NTrees*[0]
JetPuppiSel_puId_frac03          = NTrees*[0]
JetPuppiSel_puId_frac04          = NTrees*[0]
JetPuppiSel_puId_ptD             = NTrees*[0]
JetPuppiSel_puId_beta     = NTrees*[0]
JetPuppiSel_closestgen_dR = NTrees*[0]
JetPuppiSel_partflav = NTrees*[0]

for i, outTree in enumerate(outTrees):

    PV_npvsGood[i] = book_float_branch(outTree, "nvtx"          )
    JetPuppiSel_puId_dR2Mean [i] = book_float_branch(outTree, "dR2Mean"          )
    JetPuppiSel_puId_jetR [i] = book_float_branch(outTree, "jetR"          )
    JetPuppiSel_puId_jetRchg [i] = book_float_branch(outTree, "jetRchg"          )
    JetPuppiSel_puId_nCharged [i] = book_float_branch(outTree, "nParticles"          )
    JetPuppiSel_puId_nParticles [i] = book_float_branch(outTree, "nCharged"          )
    JetPuppiSel_puId_pull [i] = book_float_branch(outTree, "pull"          )
    JetPuppiSel_pt          [i] = book_float_branch(outTree, "jetPt"          )
    JetPuppiSel_eta        [i] = book_float_branch(outTree, "jetEta"         )
    JetPuppiSel_puId_majW           [i] = book_float_branch(outTree, "majW"           )
    JetPuppiSel_puId_minW         [i] = book_float_branch(outTree, "minW"           )
    JetPuppiSel_puId_frac01         [i] = book_float_branch(outTree, "frac01"         )
    JetPuppiSel_puId_frac02         [i] = book_float_branch(outTree, "frac02"         )
    JetPuppiSel_puId_frac03         [i] = book_float_branch(outTree, "frac03"         )
    JetPuppiSel_puId_frac04        [i] = book_float_branch(outTree, "frac04"         )
    JetPuppiSel_puId_ptD            [i] = book_float_branch(outTree, "ptD"            )
    JetPuppiSel_puId_beta           [i] = book_float_branch(outTree, "beta"           )
    JetPuppiSel_closestgen_dR        [i] = book_float_branch(outTree, "dRMatch"        )
    JetPuppiSel_partflav         [i] = book_int_branch  (outTree, "jetFlavorParton")

   

for ievent, event in enumerate(tChain):
    if ievent % 10000 == 0:
        print("processing %s" % ievent)
    if ievent > 2000: break
    
    #commented out - assumed that dilepton cut implemented in input root 
    #if event.nLeptons != 2: continue 

    for i in range(event.nJetPuppiSel):
        dRMatch_ = event.JetPuppiSel_closestgen_dR[i]
        eta_     = event.JetPuppiSel_eta     [i]
        flavor_  = event.JetPuppiSel_partflav[i]
        #print('dRMatch', dRMatch_)
        #print('eta', eta_)
        #print('flavor', flavor_)

        if event.JetPuppiSel_pt[i] > 100: continue
        if event.JetPuppiSel_pt[i] < 10: continue
        
        isPrompt = False
        isPileup = False
        
        if (dRMatch_ <= 0.2):
            isPrompt = True
            #print('isPrompt', isPrompt)
        
        #if (dRMatch_ >= 0.4 and abs(flavor_) == 0 ):
        if (dRMatch_ >= 0.4):
            isPileup = True
            #print('isPileup', isPileup)
    

        key = ""
        
        if (isPrompt and (        abs(eta_) <= 2.5 )) : key = 0
        if (isPrompt and ( 2.5  < abs(eta_) <= 2.75)) : key = 1
        if (isPrompt and ( 2.75 < abs(eta_) <= 3.0 )) : key = 2
        if (isPrompt and ( 3.0  < abs(eta_) <= 5.0 )) : key = 3
        
        if (isPileup and (        abs(eta_) <= 2.5 )) : key = 4
        if (isPileup and ( 2.5  < abs(eta_) <= 2.75)) : key = 5
        if (isPileup and ( 2.75 < abs(eta_) <= 3.0 )) : key = 6
        if (isPileup and ( 3.0  < abs(eta_) <= 5.0 )) : key = 7

        print('key', key)

        # nothing matched
        if key == "": continue

        outTree_toFill = outTrees[key]

        PV_npvsGood  [key][0] = float(event.PV_npvsGood)
        #PV_npvsGood  [key][0] = event.PV_npvsGood[i]
        JetPuppiSel_puId_dR2Mean  [key][0] = event.JetPuppiSel_puId_dR2Mean [i]
        JetPuppiSel_puId_jetR  [key][0] = event.JetPuppiSel_puId_jetR [i]
        JetPuppiSel_puId_jetRchg  [key][0] = event.JetPuppiSel_puId_jetRchg [i]
        JetPuppiSel_puId_nParticles  [key][0] = event.JetPuppiSel_puId_nParticles[i]
        JetPuppiSel_puId_nCharged [key][0] = event.JetPuppiSel_puId_nCharged [i]
        JetPuppiSel_puId_pull  [key][0] = event.JetPuppiSel_puId_pull[i]
        
        JetPuppiSel_pt          [key][0] = event.JetPuppiSel_pt[i]
        JetPuppiSel_eta         [key][0] = event.JetPuppiSel_eta[i]
        JetPuppiSel_puId_majW           [key][0] = event.JetPuppiSel_puId_majW[i]
        JetPuppiSel_puId_minW           [key][0] = event.JetPuppiSel_puId_minW[i]
        JetPuppiSel_puId_frac01         [key][0] = event.JetPuppiSel_puId_frac01[i]
        JetPuppiSel_puId_frac02         [key][0] = event.JetPuppiSel_puId_frac02[i]
        JetPuppiSel_puId_frac03         [key][0] = event.JetPuppiSel_puId_frac03[i]
        JetPuppiSel_puId_frac04         [key][0] = event.JetPuppiSel_puId_frac04[i]
        JetPuppiSel_puId_ptD            [key][0] = event.JetPuppiSel_puId_ptD[i]
        JetPuppiSel_puId_beta           [key][0] = event.JetPuppiSel_puId_beta[i]
        JetPuppiSel_closestgen_dR        [key][0] = event.JetPuppiSel_closestgen_dR[i]
        JetPuppiSel_partflav         [key][0] = event.JetPuppiSel_partflav[i]
            
        outTree_toFill.Fill()

for outTree in outTrees:
    outTree.Write("", ROOT.TObject.kOverwrite)

outFile.Write("", ROOT.TObject.kOverwrite)
outFile.Close()
