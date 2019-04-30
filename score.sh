#!/usr/bin/env bash

TRANS=/home/cgsdfc/UbuntuDialogueCorpus/ResponseContextPairs/ModelPredictions/VHRED/First_VHRED_BeamSearch_5_GeneratedTestResponses.txt_First.txt
REF=/home/cgsdfc/UbuntuDialogueCorpus/ResponseContextPairs/raw_testing_responses.txt
CONFIG="-n 4"
PREFIX=/home/cgsdfc/Result/Test

python bleu_score.py \
    -t $TRANS \
    -r $REF \
    -p $PREFIX \
    $CONFIG
