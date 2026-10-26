
warehouse = {
    "Receiving": {"Aisle1": 40, "Aisle2": 70},
    "Aisle1": {"Aisle2": 30, "Packing Station": 90},
    "Aisle2": {"Packing Station": 35},
    "Packing Station": {}
}

heuristic = {
    "Receiving": 100,
    "Aisle1": 70,
    "Aisle2": 35,
    "Packing Station": 0
}

def a_star(start, goal):
    open_list = [start]
    visited = []
    parent = {start: None}
    cost = {start: 0}

    while open_list:
        current = min(open_list, key=lambda node: cost[node] + heuristic[node])
        open_list.remove(current)

        if current in visited:
            continue

        visited.append(current)

        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()
            print("Path found by A*:", path)
            print("Total cost of this path:", cost[goal])
            return

        for neighbor, distance in warehouse[current].items():
            new_cost = cost[current] + distance

            if neighbor not in cost or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                parent[neighbor] = current

                if neighbor not in open_list:
                    open_list.append(neighbor)

a_star("Receiving", "Packing Station")
