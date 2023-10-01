import networkx as nx
import yaml
import matplotlib.pyplot as plt
import xgi

from xgi_yaml import to_xgi



def test_sequence():
    doc = yaml.compose('[src, tgt]')
    graph = xgi.DiHypergraph()
    to_xgi(graph, doc)
    expected = [{'tgt', 'src'}, {'src'}, {'tgt'}]
    actual = xgi.convert.hyperedges.to_hyperedge_list(graph)
    assert actual == expected


def test_mapping():
    doc = yaml.compose('src: tgt')
    graph = xgi.DiHypergraph()
    to_xgi(graph, doc)
    expected = [{'tgt', 'src'}, {'src'}, {'tgt'}]
    actual = xgi.convert.hyperedges.to_hyperedge_list(graph)
    assert actual == expected


def test_scalar():
    doc = yaml.compose('src')
    graph = xgi.DiHypergraph()
    to_xgi(graph, doc)
    expected = [{'src'}]
    actual = xgi.convert.hyperedges.to_hyperedge_list(graph)
    assert actual == expected


