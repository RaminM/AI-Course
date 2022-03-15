from queue import Queue

class BreadthFirstSearch:
    def __init__(self, graph, start, end):
        self.graph = graph
        self.start = start
        self.end = end

    def bfs_best(self):
        # the nodes that have been expanded
        expandedList = []
        # the list of expanded paths (Queue)
        paths = Queue()
        paths.put([self.start])
    
        while not paths.empty():
            # Pop and store the path to expand then expand
            path = paths.get()
            # End node to expand from
            endNode = path[-1]
    
            # Check if the node has been expanded before
            if endNode not in expandedList:
                # next stations (from the dictionary)
                nextStations = self.graph[endNode]
    
                for station in nextStations:
                    # make temporary path
                    tempPath = list(path)
                    # expand
                    tempPath.append(station)
                    # if we are at the goal, return the shortest path
                    if station == self.end:
                        return tempPath
                    # add to queue
                    paths.put(tempPath)
    
                # add to the expanded nodes list
                expandedList.append(endNode)
