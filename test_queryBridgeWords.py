import pytest
from main import DirectedGraph

@pytest.fixture
def graph():
    g = DirectedGraph()
    g.read_text_file('text.txt')
    return g

def test_queryBridgeWords_nonexistent(graph):
    bridges = graph.queryBridgeWords('x', 'y')
    assert bridges == None

def test_queryBridgeWords_exist(graph):
    bridges = graph.queryBridgeWords('wow', 'many')
    assert bridges == ['how']

def test_queryBridgeWords_none(graph):
    bridges = graph.queryBridgeWords('wow', 'nonexistent')
    assert bridges == None

if __name__ == "__main__":
    pytest.main()
