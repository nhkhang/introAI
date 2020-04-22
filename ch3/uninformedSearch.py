import collections 

class Graph:
    def __init__(self, gdict = None):
        if gdict == None:
            gdict = {}
        self.gdict = gdict

class Graph_weight:
    def __init__(self):
        self.edges = {}
        self.weights = {}

    def neighbors(self, node):
        return self.edges[node]

    def get_cost(self, from_node, to_node):
        return self.weights[(from_node + to_node)]
    
def BFS(graph, start_node):
    '''
    Breadth-First-Search: Expand shallowest unexpanded node
    Completeness: yes
    Time complexity: total number of node generated
    Space complexity: idem if each node is retained in memory
    Optimality: it always find the least-cost solution
    '''
    seen, queue = set([start_node]), collections.deque([start_node])
    while queue:
        vertex = queue.popleft()
        print(vertex)
        for node in graph:
            if node not in seen:
                seen.add(node)
                queue.append(node)

def UCS(graph, start_node, goal):
    '''
    Uniform-Cost-Search: Extension of BFS (expand node with lowest path cost)
    Completeness: yes
    Time complexity:
    Space complexity: idem to time complexity
    Optimality: nodes expands in order of 
    '''
    visited = set()
    queue = collections.deque()
    queue.put((0, start_node))

    while queue:
        cost, node = queue.get()
        if node not in visited:
            visited.add(node)

            if node == goal:
                return
            for i in graph.neighbors(node):
                if i not in visited:
                    total_cost = cost + graph.get_cost(node, i)
                    queue.put((total_cost, i))

dq = collections.deque([1,2,3])
a = dq.popleft()
print(dq.popleft())