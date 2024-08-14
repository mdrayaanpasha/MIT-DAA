class MaxFlow:
    def __init__(self, n):
       
        self.n = n
        self.graph = [[[0, 0] for _ in range(n)] for _ in range(n)]

    def add_edge(self, u, v, capacity):
        self.graph[u][v][1] = capacity  

    def dfs(self, G, s, t, vis, path):
        vis[s] = True
        if s == t:
            return True
        for i in range(len(G)):
            if not vis[i] and G[s][i][1] - G[s][i][0] > 0: 
                if self.dfs(G, i, t, vis, path):
                    path.append((s, i))
                    return True
        return False

    def redu(self, p, G, m):
        for x in p:
            G[x[0]][x[1]][0] += m  
            G[x[1]][x[0]][0] -= m  

    def algorithm(self, s, t):
        paths = []
        
        while True:
            vis = [False] * self.n  
            path = []
            if not self.dfs(self.graph, s, t, vis, path):
                break
            m = min(self.graph[x[0]][x[1]][1] - self.graph[x[0]][x[1]][0] for x in path) 
            self.redu(path, self.graph, m)
            paths.append(path)
        
        if paths:
            print("Paths found:")
            for p in paths:
                print(p)
        else:
            print("No paths")


if __name__ == "__main__":
    mf = MaxFlow(6)
    
    
    mf.add_edge(0, 1, 16)
    mf.add_edge(0, 2, 13)
    mf.add_edge(1, 2, 10)
    mf.add_edge(1, 3, 12)
    mf.add_edge(2, 1, 4)
    mf.add_edge(2, 4, 14)
    mf.add_edge(3, 2, 9)
    mf.add_edge(3, 5, 20)
    mf.add_edge(4, 3, 7)
    mf.add_edge(4, 5, 4)
    
    mf.algorithm(0, 5)
