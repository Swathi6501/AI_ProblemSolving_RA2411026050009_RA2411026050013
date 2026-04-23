def is_safe(node, color, graph, assignment):
    for neighbor in graph.get(node, []):
        if assignment.get(neighbor) == color:
            return False
    return True


def solve_with_steps(node_list, graph, colors, assignment, steps):
    if len(assignment) == len(node_list):
        steps.append(assignment.copy())
        return True

    node = None
    for n in node_list:
        if n not in assignment:
            node = n
            break

    for color in colors:
        if is_safe(node, color, graph, assignment):
            assignment[node] = color
            steps.append(assignment.copy())

            if solve_with_steps(node_list, graph, colors, assignment, steps):
                return True

            del assignment[node]
            steps.append(assignment.copy())

    return False


def map_coloring_with_steps(graph, colors):
    nodes = list(graph.keys())
    assignment = {}
    steps = []

    solve_with_steps(nodes, graph, colors, assignment, steps)
    return steps