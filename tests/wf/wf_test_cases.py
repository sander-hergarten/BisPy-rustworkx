import networkx as nx
import rustworkx as rx

graphs_wf_nwf = []

# 1
graph1 = nx.DiGraph()
graph1.add_nodes_from(range(6))
graph1.add_edges_from([(0, 1), (1, 2), (2, 3), (2, 4), (4, 5), (5, 2)])
graphs_wf_nwf.append((graph1, [3], [0, 1, 2, 3, 4, 5]))

# 2 : tree
graph2 = nx.DiGraph()
graph2.add_nodes_from(range(7))
graph2.add_edges_from([(0, 1), (1, 2), (2, 3), (0, 4), (4, 5), (5, 6)])
graphs_wf_nwf.append((graph2, list(range(7)), []))

# 3: cycle
graph3 = nx.DiGraph()
graph3.add_nodes_from(range(4))
graph3.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 0)])
graphs_wf_nwf.append((graph3, [], list(range(4))))

graphs_wf_nwf_rx = []

# 1
graph1 = rx.PyDiGraph()
graph1.add_nodes_from(range(6))
graph1.add_edges_from_no_data([(0, 1), (1, 2), (2, 3), (2, 4), (4, 5), (5, 2)])
graphs_wf_nwf_rx.append((graph1, [3], [0, 1, 2, 3, 4, 5]))

# 2 : tree
graph2 = rx.PyDiGraph()
graph2.add_nodes_from(range(7))
graph2.add_edges_from_no_data([(0, 1), (1, 2), (2, 3), (0, 4), (4, 5), (5, 6)])
graphs_wf_nwf_rx.append((graph2, list(range(7)), []))

# 3: cycle
graph3 = rx.PyDiGraph()
graph3.add_nodes_from(range(4))
graph3.add_edges_from_no_data([(0, 1), (1, 2), (2, 3), (3, 0)])
graphs_wf_nwf_rx.append((graph3, [], list(range(4))))
