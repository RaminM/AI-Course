def BFS(subway, start, end):
    # the nodes that have been expanded
    expandedList = []
    #the list of expanded paths (Queue)
    paths = [[start]]

    while paths:
        #Pop and store the path to expand then expand 
        path = paths.pop()
        #End node to expand from
        endNode = path[-1]

        #Check if the node has been expanded before 
        if endNode not in expandedList:
            #next stations (from the dictionary)
            nextStations = subway[endNode]

            for station in nextStations:
                #make temporary path
                tempPath = list(path)
                #expand
                tempPath.append(station)
                #if we are at the goal, return the shortest path
                if station == end:
                    return tempPath
                #add to queue
                paths.append(tempPath)

            #add to the expanded nodes list
            expandedList.append(endNode)