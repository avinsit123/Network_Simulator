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
from network_components import Packet, Network_Builder
from Network_env import Network_Env, NetworkSnapshot
from routing_algorithms import Random_Routing, QRoutingAlgo
import random 

if __name__ == "__main__":
    edge_list = [(0,1,2),(0,2,4),(1,2,1),(2,4,3),(1,3,7),(4,3,2),(3,5,1),(4,5,5)]
    n_nodes = 6
    max_q_size = 10
    nx_graph = Network_Builder(n_nodes,max_q_size,edge_list)
    router = QRoutingAlgo(nx_graph,n_nodes)
   # router = Random_Routing()
    # edge_list = [
    #     (0, 1, 4),
    #     (0, 7, 8),
    #     (1, 2, 8),
    #     (1, 7, 11),
    #     (2, 3, 7),
    #     (2, 8, 2),
    #     (2, 5, 4),
    #     (3, 4, 9),
    #     (3, 5, 14),
    #     (4, 5, 10),
    #     (5, 6, 2),
    #     (6, 7, 1),
    #     (6, 8, 6),
    #     (7, 8, 7)
    # ]
    # nx_graph = Network_Builder(9,10,edge_list)

    env = Network_Env(nx_graph,router)
    snapshot = NetworkSnapshot(env)
    n_packets = 20
    total_runtime = 300
    env.Initialize_Simulation(total_runtime,n_packets)
    env.run_simulation()
    snapshot.display_all_packet_status()
    snapshot.log_queue_list()
    snapshot.packet_status()
    print(router.Qtable[0][:][1])
    # ql = QLearning()
    # env.transfer_data(ql)
    # ql.Display()






         

        

    
    