import pprint
import time
import random
random.seed(0)  # to compare between the two algorithms


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
                    for i in range(len(p_q)):
                        if p_q[i][1] == j:
                            p_q.pop(i)
                            break
                    path_lengths[j] = path_lengths[cur[1]] + edges[cur[1]][j]
                    parent_array[j] = cur[1]
                    if len(p_q) == 0:  # sorting with find and insert, O(logV)
                        p_q.insert(0, (path_lengths[j], j))
                    else:
                        inserted = False
                        for i in range(len(p_q)):
                            if path_lengths[j] < p_q[i][0]:
                                p_q.insert(i, (path_lengths[j], j))
                                inserted = True
                                break
                        if inserted == False:
                            p_q.insert(len(p_q), (path_lengths[j], j))
                    # p_q.append((path_lengths[j], j))  # update new distance value of vertex
                    # p_q.sort() #  find and insert using comparison and list.insert() function
        # print(p_q)
        # print("-------")  # can print this to show the long list of duplicates in pq

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
# rows, cols = (9, 9)
# # edge set
# adj_matrix = [[0 for i in range(cols)] for j in range(rows)]
# adj_matrix[0][1] = 4
# adj_matrix[0][7] = 8
# adj_matrix[1][2] = 8
# adj_matrix[1][7] = 11
# adj_matrix[2][3] = 7
# adj_matrix[2][5] = 4
# adj_matrix[2][8] = 2
# adj_matrix[3][4] = 9
# adj_matrix[3][5] = 14
# adj_matrix[4][5] = 10
# adj_matrix[6][7] = 1
# adj_matrix[6][8] = 6
# adj_matrix[7][8] = 7
# adj_matrix[5][6] = 2
# for i in range(rows):
#     for j in range(cols):
#         if adj_matrix[i][j] != 0:
#             adj_matrix[j][i] = adj_matrix[i][j]
# # vertex set
# vertices = [i for i in range(rows)]
# # print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in adj_matrix]))
# my_dict = dijkstra(vertices, adj_matrix)
# pprint.PrettyPrinter(width=4).pprint(my_dict)

# Completed graph with V=5 and random edge weights
# rows, cols = (5, 5)
# adj_matrix = [[0 for i in range(cols)] for j in range(rows)]
# for i in range(rows):
#     for j in range(cols):
#         if j <= i:
#             continue
#         else:
#             adj_matrix[i][j] = random.randint(1, 10)
# for i in range(rows):
#     for j in range(cols):
#         if adj_matrix[i][j] != 0:
#             adj_matrix[j][i] = adj_matrix[i][j]
# vertices = [i for i in range(rows)]
# print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in adj_matrix]))
#
# start = time.perf_counter()
# my_dict = dijkstra(vertices, adj_matrix)
# end = time.perf_counter()
# pprint.PrettyPrinter(width=4).pprint(my_dict)
# duration = end - start
# print("The value of number is : ", end="")
# print('%.10f' % duration)  # average around 0.000025

# Completed graph with V=1000 and random edge weights
rows, cols = (10000, 10000)
start_graph = time.perf_counter()
adj_matrix = [[0 for i in range(cols)] for j in range(rows)]
for i in range(rows):
    for j in range(cols):
        if j <= i:
            continue
        else:
            adj_matrix[i][j] = random.randint(1, 10)
            #break  # to make sparse graph
for i in range(rows):
    for j in range(cols):
        if adj_matrix[i][j] != 0:
            adj_matrix[j][i] = adj_matrix[i][j]
end_graph = time.perf_counter()
duration_graph = end_graph - start_graph
vertices = [i for i in range(rows)]
#print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in adj_matrix]))

start = time.perf_counter()
my_dict = dijkstra(vertices, adj_matrix)
pprint.PrettyPrinter(width=4).pprint(my_dict)
end = time.perf_counter()
duration = end - start
print("Time taken to generate graph : ", end="")
print('%.10f' % duration_graph)
print("Time taken for Dijkstra algorithm : ", end="")
print('%.10f' % duration)
total = duration_graph + duration
print("Total time taken : ", end="")
print('%.10f' % total)

# sparse graph time: 0.2 (0.13 for graph generation)
# fully completed graph time: 0.85 (0.55 for graph generation)

# for V=10000 fully connected
# time taken to generate graph = 53seconds
# time taken for dijkstra's algorithm: 30seconds
# time taken total = 83seconds
