import yaml
import xgi


def to_xgi(graph, doc):
    name = "main"
    match doc:
        case yaml.ScalarNode(value=scalar):
            graph.add_edge([[scalar], []])
        case yaml.MappingNode(value=[*docs_pairs]):
            for k, v in docs_pairs:
                graph.add_edge([[k.value], [v.value]])
                to_xgi(graph, k), to_xgi(graph, v)
        case yaml.SequenceNode(value=[*docs]):
            for k, v in zip(docs[:-1], docs[1:]):
                graph.add_edge([[k.value], [v.value]])
                to_xgi(graph, k), to_xgi(graph, v)
