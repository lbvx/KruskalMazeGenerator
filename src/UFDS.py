class UFDS:
    def __init__(self, rows:int, columns:int) -> None:
        self.parent = [[(i, j) for j in range(columns)] for i in range(rows)]
        self.rank = [[1 for j in range(columns)] for i in range(rows)]

    def find(self, s:tuple) -> tuple:
        if self.parent[s[0]][s[1]] != s:
            self.parent[s[0]][s[1]] = self.find(self.parent[s[0]][s[1]])
        return self.parent[s[0]][s[1]]

    def union(self, s1:tuple, s2:tuple) -> None:
        p1 = self.find(s1)
        p2 = self.find(s2)
        
        if p1 == p2:
            return

        if self.rank[p1[0]][p1[1]] < self.rank[p2[0]][p2[1]]:
            p1, p2 = p2, p1

        self.parent[p2[0]][p2[1]] = p1
        self.rank[p1[0]][p1[1]] += self.rank[p2[0]][p2[1]]

    def same_set(self, s1:tuple, s2:tuple) -> bool:
        return self.find(s1) == self.find(s2)
