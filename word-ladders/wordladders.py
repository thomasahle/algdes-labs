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
    dist = collections.defaultdict(lambda: 10**6)
    queue = collections.deque([w1])
    dist[w1] = 0
    while queue:
        w = queue.popleft()
        snip = ''.join(sorted(w[1:]))
        for w3 in snip2words[snip]:
            if dist[w3] > dist[w]+1:
                dist[w3] = dist[w]+1
                queue.append(w3)
    if dist[w2] == 10**6:
        print(-1)
    else: print(dist[w2])

