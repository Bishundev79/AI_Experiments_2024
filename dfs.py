# pylint: disable=all
visited = set() #unique elements add kr rha hai
stack = []
def dfs(graph, node):
    stack.append(node)

    while stack:
        m = stack.pop()
        if m not in visited:
            print(m, end=" ")
            visited.add(m)

            for neighbour in reversed(graph[m]):
                if neighbour not in visited:
                    stack.append(neighbour)


graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

print("Following is the Depth-First Search")
dfs(graph, '5')