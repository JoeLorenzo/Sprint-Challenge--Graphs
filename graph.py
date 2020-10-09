"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise ValueError("vertex does not exist")

    def add_undirected_edge(self, v1, v2):
        """
        Add a undirected edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            raise ValueError("vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            raise ValueError("vertex does not exist")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create queue 
        q = Queue() 
 
        # enqueue the starting vertex
        q.enqueue(starting_vertex)
        # create a set to store visited vertices
        visited = set()
        # while the queue is not emptey...
        while q.size() > 0:
            # dequeue the first vertex
            v = q.dequeue()
            # check if it's been visited 
            # if it has not been visited...
            if v not in visited:
                # mark it as visited
                print(v) 
                visited.add(v)
                # enqueue all its neighbors
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)



    def dft(self, starting_vertex):
        """
           Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create a stack
        s = Stack()
        # push the starting vertex
        s.push(starting_vertex)
        # create a set to store the visited vertices
        visited = set()
        # while the stack is not empty...
        while s.size() > 0:
            # pop the first vertex
            v = s.pop()
            # check if its been visited 
            # check if it has not been visited
            if v not in visited:
                # mark it as visited
                print(v)
                visited.add(v)
                # push all its neighbors on to the stack 
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)


    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # set the visited to an empty set if visited is None
        if visited == None:
            visited = set()
        # check if the node has been visited
        # if not...
        if starting_vertex not in visited:
            # mark it as visited
            print(visited)
            visited.add(starting_vertex)
            print(starting_vertex)
            # call dft recursive on each neighbor 
            for neighbor in self.get_neighbors(starting_vertex):
                self.dft_recursive(neighbor, visited)


        # call dft_recursive on each neighbor
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create a queue
        q = Queue()
        # enqueue A PATH TO the starting vertex
        q.enqueue([starting_vertex])
        # create a set to store the visited vertices
        visited = set()
        # while the queue is not empty...
        while q.size() > 0:
            # dequeue the first PATH 
            path = q.dequeue()
            # GRAB THE VERTEX FROM THE END OF THE PATH
            v = path[-1]
            # check if it's been visited
            # check if it hasn't been visited
            if v not in visited:
                # mark it as visited
                visited.add(v)
                # CHECK IF IT'S THE TARGET
                if v == destination_vertex:
                    # IF SO RETURN THE PATH
                    return path
                # else enqueue A PATH to all its neighbors
                for neighbor in self.get_neighbors(v):
                    # MAKE A COPY OF THE PATH
                    path_copy = path.copy()
                    path_copy.append(neighbor)
                    # enqueue the copy
                    q.enqueue(path_copy)



    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """

        # create a stack
        s = Stack()
        # push A PATH TO the starting vertex
        s.push([starting_vertex])
        # create a set to store the visited vertices
        visited = set()
        # while the stack is not empty...
        while s.size() > 0:
            # pop the first path 
            path = s.pop()
            # GRAB THE VERTEX FROM THE END OF THE PATH
            v = path[-1]
            # check if it's been visited
            # check if it hasn't been visited
            if v not in visited:
                # mark it as visited
                visited.add(v)
                # CHECK IF IT'S THE TARGET
                if v == destination_vertex:
                    # IF SO RETURN THE PATH
                    return path
                # else push A PATH to all its neighbors
                for neighbor in self.get_neighbors(v):
                    # MAKE A COPY OF THE PATH
                    path_copy = path.copy()
                    path_copy.append(neighbor)
                    # push the copy
                    s.push(path_copy)
    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        if path is None:
            path = []
        if starting_vertex not in visited:
            visited.add(starting_vertex)
            path_copy = path.copy()
            path_copy.append(starting_vertex)
            if starting_vertex == destination_vertex:
                return path_copy
            for neighbor in self.get_neighbors(starting_vertex):
                new_path = self.dfs_recursive(neighbor, destination_vertex, visited, path_copy)
                if new_path is not None:
                    return new_path
        return None
if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices[1])
    print(graph.get_neighbors(2))

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    print(f"breadth-first order traversal")
    graph.bft(1)
    print("-----------------")

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''

    print(f"depth-first order")
    # graph.dft(1)
    graph.dft_recursive(1)
    print("----------------")

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
