# Network_Simulator
Simulator to carry out network simulations using various routing algos in python. Each Simulator comes equipped with a custom-defined graph. Each node has a queue in which packets have to wait to be processed after which they are sent to the next node.Currently, the simulator supports only random routing. 
Create a python file within the repo at first.

## Initialize Custom Network 
The first task is to initialize custom graph with nodes and edges as per your choice 

```python 
from network_components import Packet, Network_Builder
edge_list = [(0,1,2),(0,2,4),(1,2,1),(2,4,3),(1,3,7),(4,3,2),(3,5,1),(4,5,5)]
n_nodes = 6
max_q_size = 10 #max queue size of each nodes
nx_graph = Network_Builder(n_nodes,max_q_size,edge_list)

```

## Intialise routing algo
Currently only random routing is supported where next node chosen from uniform distribution of reachable neighbour nodes
```python
from routing_algorithms import Random_Routing
router = Random_Routing() # Random Routing 
```

## Define Network Environment 
The Network Environment is where all network simulations run 
 ```python
 from Network_env import Network_Env
 env = Network_Env(nx_graph,router)
 n_packets = 10             # Total no.of packets to be transferred in simulation
 total_runtime = 300        # Total runtime of simulation
 env.Initialize_Simulation(total_runtime,n_packets) # Randomly Initialize Each packets source, destination and start time
 env.run_simulation()      # Run Simulation
 ```
 
 ## Network Properties 
 Once a simulation is run we need to have a look at the results of the simulations.
 ```python
 from Network_env import NetworkSnapshot
 snapshot = NetworkSnapshot(env)
 
 # Displays source, dest, route list and whether packet was successfully delivered for each packet 
 snapshot.display_all_packet_status()
 
 # No.of packets remaining at all node queues after end of every simulation
 snapshot.log_queue_list()
 
 # Displays no. of delivered, dropped and transit packets
 snapshot.packet_status()
 ```
 
 ## Todo
 <ol>
  <li> Add QR Algo, PQR Algo and GNN + QR</li>
  <li> Add Support for Custom Packet properties</li>
