import networkx as nx
import pytest
from bispy.utilities.graph_decorator import decorate_graph
from bispy.utilities.rank_computation import (
    compute_rank,
)
from .wf_test_cases import graphs_wf_nwf, graphs_wf_nwf_rx


@pytest.mark.parametrize("graph, wf_nodes, nwf_nodes", graphs_wf_nwf)
def test_mark_wf_nodes_correct_nx(graph, wf_nodes, nwf_nodes):
    vertexes, _ = decorate_graph(graph)

    for i in range(len(graph.nodes)):
        assert (i in wf_nodes and vertexes[i].wf) or (
            i in nwf_nodes and not vertexes[i].wf
        )


@pytest.mark.parametrize("graph, wf_nodes, nwf_nodes", graphs_wf_nwf_rx)
def test_mark_wf_nodes_correct_rx(graph, wf_nodes, nwf_nodes):
    vertexes, _ = decorate_graph(graph)

    for i in range(len(graph.nodes())):
        assert (i in wf_nodes and vertexes[i].wf) or (
            i in nwf_nodes and not vertexes[i].wf
        )
