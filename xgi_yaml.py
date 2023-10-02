import yaml
import sys
import xgi
import matplotlib.pyplot as plt


def read_dihypergraph(node):
	""""""
	res = xgi.DiHypergraph()
	match node:
		case yaml.ScalarNode(value=scalar):
			res.add_edge([[scalar], [scalar]])
		case yaml.MappingNode(value=mapping):
			all_keys = [read_dihypergraph(k) for k, v in mapping]
			for k in all_keys:
				res.add_edge([all_keys, k])
			for k, v in mapping:
				k, v = read_dihypergraph(k), read_dihypergraph(v)
				res.add_edge([k, v])
		case yaml.SequenceNode(value=sequence):
			for l, r in zip(sequence[:-1], sequence[1:]):
				l, r = read_dihypergraph(l), read_dihypergraph(r)
				res.add_edge([l, r])
	return res
def main():
	""""""
	res = xgi.DiHypergraph()
	for doc in yaml.compose_all(sys.stdin, yaml.SafeLoader):
		res.add_edges_from(read_dihypergraph(doc).edges.dimembers())
		#res.add_edge([[res], read_dihypergraph(doc)])
	xgi.draw_dihypergraph(res, node_labels=True, node_size=50)
	plt.show()

if __name__ == "__main__":
	main()
