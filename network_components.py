#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 12:50:45 2020

@author: r17935avinash
"""

import numpy as np
import sys
from random import randint
from queue import Queue
import networkx as nx

class Packet(object):
    def __init__(self,source,dest,ttl,starttime,nnodes):
        self.source = source
        self.dest = dest
        self.ttl = ttl
        self.curr_node = -1
        self.packet_delivery_status = False
        self.starttime = starttime
        self.processAtTime = starttime
        self.logs = []
        self.visited_nodes = [False for i in range(nnodes)]
        self.route_list = []
        self.route_list.append(source)
        self.delay = 5
        self.drop_packet = False
        self.drop_Q_full = False

    def inTransit(self):
        self.transit = True
        self.queued = False
    
    def inWait(self):
        self.transit = False
        self.queued = True


class Network_Builder(object):
    def __init__(self,n_nodes,max_q_sizes,edge_list,digraph = True):
        self.nnodes = n_nodes
        self.n_process_times = 4
        self.max_q_sizes = max_q_sizes
        self.packet_queue = [Queue(maxsize=max_q_sizes) for i in range(n_nodes)]
        self.packet_queue_length = [0 for i in range(n_nodes)]
        if digraph:
            self.graph = nx.DiGraph()
        else:
            self.graph = nx.Graph()
        self.graph.add_nodes_from(np.arange(n_nodes))
        self.packet_list = []

        for source,dest,weight in edge_list:
            self.graph.add_edge(source,dest,weight=weight)







         

        

    
    