import pytest
from bispy.dovier_piazza_policriti.ranked_partition import RankedPartition
from .dovier_piazza_policriti_test_cases_rx import graphs
from bispy.utilities.graph_decorator import decorate_graph
import rustworkx as rx
import rustworkx.generators as generators
from bispy.utilities.graph_entities import _QBlock


@pytest.mark.parametrize(
    "rank, expected", zip([float("-inf"), *(range(5))], range(6))
)
def test_rank_to_partition_idx(rank, expected):
    assert RankedPartition.rank_to_partition_idx(rank) == expected


@pytest.mark.parametrize("graph", graphs)
def test_create_initial_partition(graph):
    vertexes, _ = decorate_graph(graph)
    partition = RankedPartition(vertexes)

    # at least one block per rank, except for float('-inf')
    assert all(len(partition[idx]) for idx in range(1, len(partition)))

    # right vertexes in the right place
    for idx in range(len(partition)):
        rank = float("-inf") if idx == 0 else idx - 1

        # right number of vertexes
        assert partition[idx][0].vertexes.size == [
            vertex.rank == rank for vertex in vertexes
        ].count(True)
        # right rank
        assert all(
            vertex.rank == rank for vertex in partition[idx][0].vertexes
        )


@pytest.mark.parametrize("graph", graphs)
def test_nvertexes(graph):
    vertexes, _ = decorate_graph(graph)
    partition = RankedPartition(vertexes)
    assert partition.nvertexes == len(graph.nodes())


def test_get_item():
    vertexes, _ = decorate_graph(generators.full_rary_tree(2, 3).to_directed())
    partition = RankedPartition(vertexes)
    assert partition[0] == partition._partition[0]


def test_append_at_rank():
    num_nodes = (
        2**2 - 1
    )  # Calculating the total number of nodes for a full binary tree
    branching_factor = 2  # For a binary tree
    vertexes, _ = decorate_graph(
        rx.generators.full_rary_tree(branching_factor, num_nodes)
    )
    partition = RankedPartition(vertexes)
    block = _QBlock([], None)
    partition.append_at_rank(block, 1)
    assert partition[2][-1] == block


def test_append_at_index():
    num_nodes = (
        2**2 - 1
    )  # Calculating the total number of nodes for a full binary tree
    branching_factor = 2  # For a binary tree
    vertexes, _ = decorate_graph(
        rx.generators.full_rary_tree(branching_factor, num_nodes)
    )
    partition = RankedPartition(vertexes)
    block = _QBlock([], None)
    partition.append_at_index(block, 1)
    assert partition[1][-1] == block


def test_len():
    num_nodes = (
        2**3 - 1
    )  # Calculating the total number of nodes for a full binary tree
    branching_factor = 2  # For a binary tree
    vertexes, _ = decorate_graph(
        rx.generators.full_rary_tree(branching_factor, num_nodes)
    )
    partition = RankedPartition(vertexes)
    assert len(partition) == 4


def test_scc_leaf_length():
    num_nodes = (
        2**2 - 1
    )  # Calculating the total number of nodes for a full binary tree
    branching_factor = 2  # For a binary tree
    vertexes, _ = decorate_graph(
        rx.generators.full_rary_tree(branching_factor, num_nodes)
    )
    partition = RankedPartition(vertexes)
    assert partition[0][0].size == 0


def test_clear_rank():
    num_nodes = (
        2**2 - 1
    )  # Calculating the total number of nodes for a full binary tree
    branching_factor = 2  # For a binary tree
    vertexes, _ = decorate_graph(
        rx.generators.full_rary_tree(branching_factor, num_nodes)
    )
    partition = RankedPartition(vertexes)
    partition.clear_rank(1)
    assert len(partition[2]) == 0


def test_clear_index():
    num_nodes = (
        2**2 - 1
    )  # Calculating the total number of nodes for a full binary tree
    branching_factor = 2  # For a binary tree
    vertexes, _ = decorate_graph(
        rx.generators.full_rary_tree(branching_factor, num_nodes)
    )
    partition = RankedPartition(vertexes)
    partition.clear_index(1)
    assert len(partition[1]) == 0


def test_iter():
    num_nodes = (
        2**2 - 1
    )  # Calculating the total number of nodes for a full binary tree
    branching_factor = 2  # For a binary tree
    vertexes, _ = decorate_graph(
        rx.generators.full_rary_tree(branching_factor, num_nodes)
    )
    partition = RankedPartition(vertexes)
    idx = 0
    for r in partition:
        assert r == partition._partition[idx]
        idx += 1
