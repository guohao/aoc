visited = [(0, 0)]
for c in input():
    i, j = visited[-1]
    match c:
        case '^':
            i -= 1
        case 'v':
            i += 1
        case '>':
            j += 1
        case '<':
            j -= 1
    visited.append((i, j))
print(len(set(visited)))
