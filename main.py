import heapq
import random
import re

class DirectedGraph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes[node] = {}

    def add_edge(self, from_node, to_node, weight):
        if from_node in self.nodes and to_node in self.nodes:
            self.nodes[from_node][to_node] = weight

    def calcShortestPath(self, start, end):
        distances = {node: float('infinity') for node in self.nodes}
        previous_nodes = {node: None for node in self.nodes}
        distances[start] = 0
        pq = [(0, start)]
        if end not in self.nodes:
            return [], float('infinity')
        while pq:
            current_distance, current_node = heapq.heappop(pq)
            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self.nodes[current_node].items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(pq, (distance, neighbor))

        path = []
        current_node = end
        if distances[end] == float('infinity'):
            return path, distances[end]

        while current_node is not None:
            path.append(current_node)
            current_node = previous_nodes[current_node]

        path.reverse()
        return path, distances[end]

    def queryBridgeWords(self, word1, word2):
        if word1 not in self.nodes or word2 not in self.nodes:
            return None
        bridge_words = []
        for bridge in self.nodes[word1]:
            if word2 in self.nodes[bridge]:
                bridge_words.append(bridge)
        return bridge_words

    def randomWalk(self):
        if not self.nodes:
            return []
        current_node = random.choice(list(self.nodes.keys()))
        path = [current_node]
        while True:
            if not self.nodes[current_node]:
                break
            next_node = random.choice(list(self.nodes[current_node].keys()))
            if next_node in path:
                break
            path.append(next_node)
            current_node = next_node
        return path

    def read_text_file(self, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                # 去掉标点符号并转换为小写
                words = re.sub(r'[^\w\s]', '', line).strip().lower().split()
                for i in range(len(words) - 1):
                    self.add_node(words[i])
                    self.add_node(words[i + 1])
                    self.add_edge(words[i], words[i + 1], 1)

# 示例调用
# graph = DirectedGraph()
# graph.read_text_file('text.txt')
