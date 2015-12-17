import helpers as helper


# 0 y-
# 1 x+
# 2 y+
# 3 x-


class RollingBalls:
    def restorePattern(self, start, target):
        sa = []
        ta = []
        for s in start:
            sa += [list(s)]
        for s in target:
            ta += [list(s)]
        x = self.build(sa)
        for i in x:
            helper.log(i)
        return tuple(self.algo1(sa, ta))

    def build(self, start):
        n = len(start)
        m = len(start[0])
        return [[self.calc(i, j, start) for j in range(m)] for i in range(n)]

    def calc(self, x, y, start):
        n = len(start)
        m = len(start[0])
        res = [y - 1, x + 1, y + 1, x - 1]
        while res[0] >= 0 and start[x][res[0]] == '.':
            res[0] -= 1
        while res[1] < n and start[res[1]][y] == '.':
            res[1] += 1
        while res[2] < m and start[x][res[2]] == '.':
            res[2] += 1
        while res[3] >= 0 and start[res[3]][y] == '.':
            res[3] -= 1
        return res

    @staticmethod
    def algo1(s, t):
        # trying to reach within one move
        n = len(s)
        m = len(s[0])
        res = []
        for i in range(n):
            for j in range(m):
                if s[i][j].isdigit() and t[i][j].isdigit() == False:
                    # investigate all directions (U,D,L,R)
                    it = i - 1
                    while it >= 0 and s[it][j] == '.':
                        it -= 1
                    it += 1
                    if t[it][j].isdigit():
                        res += [str(i) + ' ' + str(j) + ' ' + str(3)]
                        s[it][j] = s[i][j]
                        s[i][j] = '.'
                        continue
        return res
