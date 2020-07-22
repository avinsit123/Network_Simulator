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

class Random_Routing():
    def __init__(self):
        self.ones = 1

    def packet_process(self,packet,network):
        self.network = network
        curr_node = packet.route_list[-1]
        packet.visited_nodes[curr_node] = True 

        if len(packet.route_list) > 1:
            self.network.packet_queue_length[curr_node] -= 1
        
        # If a packet has reached destination, set delivery status as true
        if packet.route_list[-1] == packet.dest:
            packet.packet_delivery_status = True
            return packet
            
        # Obtain List of all possible neighbors of this node
        neighbour_list = [node for node in self.network.graph.adj[curr_node] if packet.visited_nodes[node] == False and self.network.packet_queue_length[node] < self.network.max_q_sizes]
        
        #If no node is found drop packet and randomly chose node
        if len(neighbour_list) == 0:
            packet.drop_packet = True
            return packet

        next_node = random.choice(neighbour_list)
        packet.processAtTime += self.network.graph[curr_node][next_node]["weight"] + self.network.packet_queue_length[next_node] * self.network.n_process_times # Add route distance
        self.network.packet_queue_length[next_node] += 1
        packet.route_list.append(next_node)
        
        return packet 


class QRoutingAlgo():
    def __init__(self, parameter_list):
        pass
        




         

        

    
    