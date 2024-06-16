import pytest
from main import DirectedGraph

@pytest.fixture
def graph():
    g = DirectedGraph()
    g.read_text_file('text.txt')
    return g

def test_calcShortestPath_same_start_end(graph):
    path, distance = graph.calcShortestPath('wow', 'wow')
    assert path == ['wow']
    assert distance == 0

def test_calcShortestPath_direct_path(graph):
    path, distance = graph.calcShortestPath('wow', 'how')
    assert path == ['wow', 'how']
    assert distance == 1

def test_calcShortestPath_indirect_path(graph):
    path, distance = graph.calcShortestPath('wow', 'one')
    assert path == ['wow', 'how', 'many', 'showers', 'do', 'you', 'have', 'one']
    assert distance == 7

def test_calcShortestPath_no_path(graph):
    path, distance = graph.calcShortestPath('wow', 'nonexistent')
    assert path == []
    assert distance == float('infinity')

if __name__ == "__main__":
    pytest.main()
