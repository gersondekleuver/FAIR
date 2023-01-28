#!/bin/sh

RANDOMN=$20034$
RANDOM=$20034$
runName=kd_Vgg19_11
newRun=false
serviceType=kd
ablationType=Vgg19_11

mkdir Experiments/$ablationType/$runName/$RANDOM
expOut=Experiments/$ablationType/$runName/$RANDOM/$RANDOM.out
errorOut=Experiments/$ablationType/$runName/$RANDOM/error+$RANDOMN.out

cp Experiments/$ablationType/$runName/args.yaml Experiments/$ablationType/$runName/$RANDOM/args.yaml

CUDA_VISIBLE_DEVICES=2,3 python -u main.py $runName $newRun $serviceType $RANDOM $ablationType > $expOut 2>$errorOut