graph = {}  # init dict for graph
graph["start"] = {}  # init dict for each node and his neighs
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}  # finish
costs = {}  # init dict for cost of each node
costs["a"] = graph["start"]["a"]
costs["b"] = graph["start"]["b"]
costs["fin"] = float("inf")  # at the start we do not know cost of finish node at this is infinity yet
parents = {}  # init dict for relations with parents
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None
processed_list = []  # list for processed items


def deixtra():
    node = find_lowest_cost_node(costs)  # find smallest not processed node
    while node is not None:  # while node is exist (all node need be processed)
        cost = costs[node]  # current cost of this node
        neighbors = graph[node]  # list of possible ways from node
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]  # cost of neighbor, if we go to there throw current node
            if costs[n] > new_cost:
                costs[n] = new_cost  # update info
                parents[n] = node
        processed_list.append(node)
        node = find_lowest_cost_node(costs)
    return costs[processed_list[len(processed_list) - 1]] # last node's cost


def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed_list:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


print(deixtra())