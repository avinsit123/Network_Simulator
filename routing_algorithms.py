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
    def __init__(self, network):
        self.ones = 1
        self.network = network

    def packet_process(self,packet):
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
    def __init__(self, network, nnodes, lr = 0.5):
        self.network = network
        self.nnodes = nnodes
        self.Qtable = np.zeros((nnodes,nnodes,nnodes))
        self.lr = lr

    def find_neighbour_min(self, curr_node, dest_node,packet):
        neighbour_list = [node for node in self.network.graph.adj[curr_node] if packet.visited_nodes[node] == False and  self.network.packet_queue_length[node] < self.network.max_q_sizes]
        if len(neighbour_list) == 0:
            return -1
        p_nodes = self.Qtable[curr_node][:][dest_node]
        min_node = neighbour_list[np.argmin(p_nodes[neighbour_list])]
        return min_node

    def packet_process(self,packet):
        curr_node = packet.route_list[-1]
        packet.visited_nodes[curr_node] = True
        dest_node = packet.dest

        if len(packet.route_list) > 1:
            self.network.packet_queue_length[curr_node] -= 1

        # If a packet has reached destination, set delivery status as true
        if packet.route_list[-1] == packet.dest:
            packet.packet_delivery_status = True
            return packet
            
        # Obtain List of all possible neighbors of this node
        neighbour_list = [node for node in self.network.graph.adj[curr_node] if packet.visited_nodes[node] == False and self.network.packet_queue_length[node] < self.network.max_q_sizes]

        if curr_node == 0:
            print(neighbour_list)

        if len(neighbour_list) == 0:
            packet.drop_packet = True
            return packet 

        
        # Update Q table for all reachable nodes
        for node in neighbour_list:
            next_best_node = self.find_neighbour_min(node,dest_node,packet) 
            new_estimate = self.network.graph[curr_node][node]["weight"] + self.network.packet_queue_length[node] * self.network.n_process_times + self.Qtable[node][next_best_node][dest_node]
            self.Qtable[curr_node][node][dest_node] =  self.lr * ( new_estimate -  self.Qtable[curr_node][node][dest_node] )

        # Choose next best node based on the Q table
        next_node = self.find_neighbour_min(curr_node, dest_node, packet)
        packet.processAtTime += self.network.graph[curr_node][next_node]["weight"] + self.network.packet_queue_length[next_node] * self.network.n_process_times # Add route distance
        self.network.packet_queue_length[next_node] += 1
        packet.route_list.append(next_node)
        return packet
        






        
        
        




         

        

    
    