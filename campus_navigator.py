
campus = {
    "Hostel": {"Cafeteria": 150, "Admin Block": 300},
    "Cafeteria": {"Academic Block": 200},
    "Admin Block": {"Academic Block": 120},
    "Academic Block": {"Library": 100},
    "Library": {}
}

heuristic = {
    "Hostel": 350,
    "Cafeteria": 260,
    "Admin Block": 150,
    "Academic Block": 90,
    "Library": 0
}

def gbfs(start, goal):
    frontier = [start]
    visited = []
    parent = {start: None}

    while frontier:
        frontier.sort(key=lambda node: heuristic[node])
        current = frontier.pop(0)

        if current in visited:
            continue

        visited.append(current)

        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()
            cost = 0

            for i in range(len(path) - 1):
                cost += campus[path[i]][path[i + 1]]

            print("Path found by GBFS:", path)
            print("Total cost of this path:", cost)
            return

        for neighbor in campus[current]:
            if neighbor not in visited and neighbor not in frontier:
                frontier.append(neighbor)
                parent[neighbor] = current

gbfs("Hostel", "Library")
