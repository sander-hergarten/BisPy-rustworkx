from bispy.utilities.graph_entities import (
    _QBlock as _Block,
    _Vertex,
)
import rustworkx as rx
import rustworkx.generators as generators

# 1
graph1 = rx.PyDiGraph()
graph1.add_nodes_from(range(4))
graph1.add_edges_from_no_data([(0, 1), (1, 1), (2, 3), (3, 1)])

# 2
graph2 = rx.PyDiGraph()
graph2.add_nodes_from(range(4))
graph2.add_edges_from_no_data([(0, 1), (0, 2), (0, 3), (3, 2), (2, 2)])

graphs = [
    graph1,
    graph2,
    generators.complete_graph(10).to_directed(),
    generators.star_graph(10).to_directed(),
    generators.empty_graph(20).to_directed(),
    generators.cycle_graph(10).to_directed(),
]

# block counterimage
block_counterimaged_block = []

block_counterimaged_block.append([1])

block_counterimaged_block.append([1, 2])

# FBA correctness
# 0
checker_graphs = []

graph0 = rx.PyDiGraph()
graph0.add_nodes_from(range(8))
graph0.add_edges_from_no_data(
    [(0, 1), (1, 2), (2, 0), (3, 0), (3, 4), (4, 5), (5, 0), (3, 6), (6, 7)]
)
checker_graphs.append(graph0)

# 1
graph1 = rx.PyDiGraph()
graph1.add_nodes_from(range(8))
node_map = dict((t, 7 - t) for t in range(8))
graph1.add_edges_from_no_data(
    [(node_map[src], node_map[dst]) for src, dst in graph0.edge_list()]
)
checker_graphs.append(graph1)

# 2
graph2 = rx.PyDiGraph()
graph2.add_nodes_from(range(7))
graph2.add_edges_from_no_data(
    [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0), (0, 5), (5, 6)]
)
checker_graphs.append(graph2)
