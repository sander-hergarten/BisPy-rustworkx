import networkx as nx
import paige_tarjan.graph_decorator as decorator
import paige_tarjan.pta as pta

def rscp(graph: nx.Graph, initial_partition: list[list[int]]):
    (q_partition, _) = decorator.initialize(graph, initial_partition)
    rscp = pta.pta(q_partition)
    return [tuple(sorted(tp)) for tp in rscp]