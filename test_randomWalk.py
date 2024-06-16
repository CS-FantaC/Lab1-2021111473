import pytest
from main import DirectedGraph

@pytest.fixture
def graph():
    g = DirectedGraph()
    g.read_text_file('text.txt')
    return g

def test_randomWalk_empty_graph():
    g = DirectedGraph()
    path = g.randomWalk()
    assert path == []

def test_randomWalk_non_empty_graph(graph):
    path = graph.randomWalk()
    assert len(path) > 0
    assert len(path) == len(set(path))  # 确保没有环
    for i in range(len(path) - 1):
        assert path[i + 1] in graph.nodes[path[i]]

if __name__ == "__main__":
    pytest.main()
