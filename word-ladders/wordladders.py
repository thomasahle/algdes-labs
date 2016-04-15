import sys, collections
# Build graph from filename in argv[1]
snip2words = collections.defaultdict(list)
for word in open(sys.argv[1]):
    word = word.strip()
    s = ''.join(sorted(word))
    for i in range(5):
        snip = s[:i] + s[i+1:]
        snip2words[snip].append(word)
# Read input from stdin
for line in sys.stdin:
    w1, w2 = line.split()
    # Do BFS
    par = {}
    queue = collections.deque([w1])
    while queue:
        w = queue.popleft()
        snip = ''.join(sorted(w[1:]))
        for w3 in snip2words[snip]:
            if w3 not in par and w3 != w1:
                par[w3] = w
                queue.append(w3)
    # Recover path
    path = [w2]
    while path[-1] in par:
        path.append(par[path[-1]])
    if len(path) == 1 and w1 != w2:
        path = [':-(']
    print(' -> '.join(path[::-1]))

