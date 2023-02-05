#!/usr/bin/env python3

'''
Created on Fev 05, 2023
@author: leandro almeida (leandro.almeida@ifpb.edu.br)
'''

__version__ = 0.1
__updated__ = '2023-02-05'

import argparse
import sys
import socket
import random
import struct

from scapy.all import sendp, get_if_hwaddr,sendpfast
from scapy.all import Packet
from scapy.all import Ether, IP, UDP, TCP
from time import sleep


def run(args):
    
    addr = args.target
    iface = args.interface

    payload = "1"*466    
    pkt = Ether(src=get_if_hwaddr(iface)) / IP(dst=addr) / UDP(dport=1234, sport=random.randint(49152,65535)) / payload 
    
    while True:
        
        Sleep = random.uniform(0.01,1)
        sendp(pkt, iface=iface)
        pkt.show()
        sleep(Sleep)


def main():

    parser = argparse.ArgumentParser()
    program_version = "v%s" % __version__
    program_build_date = str(__updated__)

    parser.add_argument('-V', '--version', action='version', version='%%(prog)s %s (%s)' % (program_version, program_build_date))
    parser.add_argument("-v", "--verbose", dest="verbose", action="count", help="set verbosity level [default: %(default)s]")
    parser.add_argument("-t", "--target", dest="target", help="set the target IP", required=True)
    parser.add_argument("-i", "--interface", dest="interface", help="set the interface", required=True)
    args = parser.parse_args()
     
    run(args)

if __name__ == '__main__':
    main()