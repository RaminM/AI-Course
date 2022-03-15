import BreadthFirst as bfs

graph = {
    1: [2, 3, 4],
    2: [1, 5, 6],
    3: [1],
    4: [1, 7, 8],
    5: [2, 9, 10],
    6: [2],
    7: [4, 11, 12],
    8: [4],
    9: [5],
    10: [5],
    11: [7],
    12: [7]
}
start = 1
end = 6
search = bfs.BreadthFirstSearch(graph, start, end)
print(search.bfs_best())
