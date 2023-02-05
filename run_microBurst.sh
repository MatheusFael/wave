#!/bin/bash

PATH_LOADGEN="/vagrant/loadGen"

IP=$1
interface=$2

python3 loadGen/microBurst/microBurst.py -t $IP -i $interface