import pprint


def dijkstra(nodes, edges, source_index=0):
    path_lengths = {v: float('inf') for v in nodes}  # path lengths from source node to node, initialised to inf
    path_lengths[source_index] = 0
    parent_array = {v: -1 for v in nodes}  # dict where key is the node and value is the parent node, initialised to -1
    parent_array[source_index] = 0
    confirmed = [0 for v in nodes]  # set of vertices whose shortest paths have been determined
    p_q = [(0, source_index)]  # inserting source node with distance 0 in priority queue
    while p_q:
        cur = p_q.pop(0)
        # print("cur : ")
        # print(cur)
        confirmed[cur[1]] = 1
        # print("confirmed list: ")
        # print(confirmed)
        for j in range(len(nodes)):
            if edges[cur[1]][j] != 0:  # loop through all adjacent vertices, j = vertex
                if confirmed[j] != 1 and path_lengths[j] > path_lengths[cur[1]] + edges[cur[1]][j]:
                    path_lengths[j] = path_lengths[cur[1]] + edges[cur[1]][j]
                    parent_array[j] = cur[1]
                    p_q.append((path_lengths[j], j))  # update new distance value of vertex
                    p_q.sort()
                    # print(p_q)
                    # print("-------")
    return path_lengths


# # test case 1
# rows, cols = (7, 7)
# # edge set
# adj_matrix = [[0 for i in range(cols)] for j in range(rows)]
# adj_matrix[0][1] = 2
# adj_matrix[0][2] = 6
# adj_matrix[1][3] = 5
# adj_matrix[2][3] = 8
# adj_matrix[3][4] = 10
# adj_matrix[3][5] = 15
# adj_matrix[4][6] = 2
# adj_matrix[5][6] = 6
# for i in range(rows):
#     for j in range(cols):
#         if adj_matrix[i][j] != 0:
#             adj_matrix[j][i] = adj_matrix[i][j]
# # vertex set
# vertices = [i for i in range(rows)]
# # print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in adj_matrix]))
# my_dict = dijkstra(vertices, adj_matrix)
# pprint.PrettyPrinter(width=4).pprint(my_dict)

# test case 2
rows, cols = (9, 9)
# edge set
adj_matrix = [[0 for i in range(cols)] for j in range(rows)]
adj_matrix[0][1] = 4
adj_matrix[0][7] = 8
adj_matrix[1][2] = 8
adj_matrix[1][7] = 11
adj_matrix[2][3] = 7
adj_matrix[2][5] = 4
adj_matrix[2][8] = 2
adj_matrix[3][4] = 9
adj_matrix[3][5] = 14
adj_matrix[4][5] = 10
adj_matrix[6][7] = 1
adj_matrix[6][8] = 6
adj_matrix[7][8] = 7
adj_matrix[5][6] = 2
for i in range(rows):
    for j in range(cols):
        if adj_matrix[i][j] != 0:
            adj_matrix[j][i] = adj_matrix[i][j]
# vertex set
vertices = [i for i in range(rows)]
# print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in adj_matrix]))
my_dict = dijkstra(vertices, adj_matrix)
pprint.PrettyPrinter(width=4).pprint(my_dict)


