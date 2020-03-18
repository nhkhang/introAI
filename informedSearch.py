import collections 
from queue import PriorityQueue

class Node:
    def __init__(self, parent = None, position = None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other_postion):
        return self.position == other_postion

def a_star_matrix(maze, start, end):
    '''
    A-Star Algorithm: find shortest path between two node
    Version: NxN number matrix
    arg start   (int, int): geometry of start node
    arg end     (int, int): geometry of end node
    '''
    # start, end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = start_node.h = start_node.f = 0

    open_list = []
    closed_list = []
    
    open_list.append(start_node)

    while len(open_list) > 0:
        # Get current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index
        
        # Update open and closed list
        open_list.pop(current_index)
        closed_list.append(current_node)        
        
        # Found goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # return reverse

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
            
            # Check new position is in range
            if node_position[0] > len(maze) or node_position[1] > len(maze[0]) or node_position[0] < 0 or node_position[1] < 0:
                continue

            # Check it walkable
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            new_node = Node(current_node, node_position)

            children.append(new_node)

        for child in children:
            # Check closed child
            meet_closed = False
            for closed_child in closed_list:
                if child == closed_child:
                    meet_closed = True
                    break
            if meet_closed == True:
                continue

            # Calculate f,g,h
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2 + (child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child in open_list
            meet_open = False
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    meet_open = True
                    break
            if meet_open == False:
                open_list.append(child)

def main():
    maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    start = (0, 0)
    end = (1, 5)

    path = a_star_matrix(maze, start, end)

    for i in range(len(maze)):
        for j in range(len(maze[0])):
            node_printed = None
            for node in path:
                if node == (i, j):
                    node_printed = node
                    break
            if node_printed != None:
                print('X', end="")
            elif maze[i][j] != 0:
                print('#', end="")
            else:
                print('-', end="")
        print('\n')

if __name__ == "__main__":
    main()
    
