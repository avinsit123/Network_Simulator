#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 12:50:45 2020

@author: r17935avinash
"""

import numpy as np
import sys
from random import randint
import random
from queue import Queue
import networkx as nx
from network_components import Packet, Network_Builder
import sys
class Network_Env(object):
    def __init__(self,network,routing_algo):
        self.network = network
        self.packet_list = []
        self.currtime = 0
        self.max_counter = 40
        self.router = routing_algo
    def build_Packet_Initializer(self,n_packets):
        for i in range(n_packets):
            source = np.random.random_integers(0,self.network.nnodes-1)
            dest = np.random.random_integers(0,self.network.nnodes-1)
            while source == dest or nx.has_path(self.network.graph, source,dest) == False:
                dest = np.random.random_integers(0,self.network.nnodes-1)
                source = np.random.random_integers(0,self.network.nnodes-1)
            ttl = 4
            self.packet_list.append(Packet(source,dest,ttl,0,self.network.nnodes))  

    def Initialize_Simulation(self,total_runtime,n_requests):
        self.build_Packet_Initializer(n_requests)
        self.runtime = total_runtime

    def run_simulation(self):
        while self.currtime <= self.runtime :
            for i,packet in enumerate(self.packet_list):
                if self.currtime == packet.processAtTime and packet.drop_packet == False and packet.packet_delivery_status == False:
                    self.router.packet_process(packet)
            self.currtime += 1

        
class NetworkSnapshot():
    def __init__(self,network_env):
        self.env = network_env
        self.npackets_delivered = 0
        self.npackets_dropped = 0
        self.npackets_transit = 0

    def display_all_packet_status(self):
        for i,packet in enumerate(self.env.packet_list):
            print("-------------------------------------------------------------")
            print("From ",packet.source," to ",packet.dest)
            if packet.packet_delivery_status:
                print("Packets Delivered Successfully")
                print("Route List:",packet.route_list)
            else:
                print("Packet Delivery Failed")
                if packet.drop_Q_full:
                    print("As all Q were full")
                print("Route List:",packet.route_list)
            print("_________________________________________________________")

    def log_queue_list(self):
        for i,queue_length in enumerate(self.env.network.packet_queue_length):
            print("Current Queue Length for node ", i , " is ", queue_length," packets" )

    def packet_status(self):
        for i,packet in enumerate(self.env.packet_list):
            if packet.packet_delivery_status:
                self.npackets_delivered += 1
            elif packet.drop_packet:
               self.npackets_dropped += 1
            else:
               self.npackets_transit += 1  
        print("Packets Delivered ::",self.npackets_delivered )
        print("Packets Dropped ::", self.npackets_dropped)
        print("Packets In Transit ::",self.npackets_transit)



    


    




         

        

    
    