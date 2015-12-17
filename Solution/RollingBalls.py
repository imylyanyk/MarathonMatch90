
# 0 y-
# 1 x+
# 2 y+
# 3 x-


class RollingBalls:
    global global_var

    def restorePattern(self, start, target):
        sa = []
        ta = []
        for s in start:
            sa += [list(s)]
        for s in target:
            ta += [list(s)]
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

    def algo1(self, s, t):
        walls = self.build(s)
        # trying to reach within one move
        n = len(s)
        m = len(s[0])
        res = []
        for i in range(n):
            for j in range(m):
                if s[i][j].isdigit() and t[i][j].isdigit() == False:
                    tmp = walls[i][j]
                    step = [i, j, 4]
                    if t[i][tmp[0] + 1].isdigit():
                        step = [i, tmp[0] + 1, 0]

                    if t[tmp[1] - 1][j].isdigit():
                        step = [tmp[1] - 1, j, 1]

                    if t[i][tmp[2] - 1].isdigit():
                        step = [i, tmp[2] - 1, 2]

                    if t[tmp[3] + 1][j].isdigit():
                        step = [tmp[3] + 1, j, 3]

                    if step[2] != 4:
                        res += [str(i) + ' ' + str(j) + ' ' + str(step[2])]
                        s[step[0]][step[1]] = s[i][j]
                        s[i][j] = '.'
                        walls = self.build(s)
                        continue
        return res
