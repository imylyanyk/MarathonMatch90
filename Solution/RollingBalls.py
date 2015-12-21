# 0 y-
# 1 x+
# 2 y+
# 3 x-
import random


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
        res = [[[j, i, j, i] for j in range(m)] for i in range(n)]

        for i in range(n):
            for j in range(m):
                if start[i][j] != '#':
                    res[i][j][0] = -1 if j == 0 else (res[i][j - 1][0] if start[i][j-1] == '.' else j-1)
                    res[i][j][3] = -1 if i == 0 else (res[i - 1][j][3] if start[i-1][j] == '.' else i-1)

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if start[i][j] != '#':
                    res[i][j][1] = n if i == n - 1 else (res[i + 1][j][1] if start[i+1][j] == '.' else i+1)
                    res[i][j][2] = m if j == m - 1 else (res[i][j + 1][2] if start[i][j+1] == '.' else j+1)
        #
        # res2 = [[self.calc(i, j, start) for j in range(m)] for i in range(n)]
        #
        # for i in range(n):
        #     for j in range(n):
        #         if start[i][j] != '#':
        #             if res2[i][j] != res[i][j]:
        #                 print('not equal!')
        return res

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

    def calcAllowed(self, board):
        res = 0
        for s in board:
            for c in s:
                if c.isdigit():
                    res += 1
        return res

    def algo1(self, s, t):
        #walls = self.build(s)
        # trying to reach within one move
        n = len(s)
        m = len(s[0])
        res = []

        balls = self.calcAllowed(s)
        allowed = balls * 20

        prevSize = 0
        while True:

            # try to move to 'main' target (same color)
            for i in range(n):
                for j in range(m):
                    if s[i][j].isdigit() and t[i][j] != s[i][j]:  # the ball isn't yet in target
                        #tmp = walls[i][j]
                        tmp = self.calc(i, j, s)
                        step = [i, j, 4]
                        if t[i][tmp[0] + 1] == s[i][j]:
                            step = [i, tmp[0] + 1, 0]

                        if t[tmp[1] - 1][j] == s[i][j]:
                            step = [tmp[1] - 1, j, 1]

                        if t[i][tmp[2] - 1] == s[i][j]:
                            step = [i, tmp[2] - 1, 2]

                        if t[tmp[3] + 1][j] == s[i][j]:
                            step = [tmp[3] + 1, j, 3]

                        if step[2] != 4:
                            res += [str(i) + ' ' + str(j) + ' ' + str(step[2])]
                            s[step[0]][step[1]] = s[i][j]
                            s[i][j] = '.'
                            #walls = self.build(s)
                            #continue

            if len(res) + 2 * balls > allowed:
                # try to move anywhere on board, preferably to destination with score 0.5
                for i in range(n):
                    for j in range(m):
                        if s[i][j].isdigit() and t[i][j].isdigit() == False:
                            #tmp = walls[i][j]
                            tmp = self.calc(i, j, s)
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
                                #walls = self.build(s)

            # otherwise, move randomly on board
            for i in range(n):
                for j in range(m):
                    if s[i][j].isdigit() and t[i][j] != s[i][j]:
                        #tmp = walls[i][j]
                        tmp = self.calc(i, j, s)
                        step = [i, j, 4]
                        if t[i][tmp[0] + 1].isdigit():
                            step = [i, tmp[0] + 1, 0]

                        if t[tmp[1] - 1][j].isdigit():
                            step = [tmp[1] - 1, j, 1]

                        if t[i][tmp[2] - 1].isdigit():
                            step = [i, tmp[2] - 1, 2]

                        if t[tmp[3] + 1][j].isdigit():
                            step = [tmp[3] + 1, j, 3]

                        if step[2] == 4 or (len(res) + 2 * balls < allowed):
                            # can roll it randomly
                            move = random.randint(0, 3)
                            if move == 0:
                                step = [i, tmp[0] + 1, 0]
                            if move == 1:
                                step = [tmp[1] - 1, j, 1]
                            if move == 2:
                                step = [i, tmp[2] - 1, 2]
                            if move == 3:
                                step = [tmp[3] + 1, j, 3]

                            if step[0] == i and step[1] == j:
                                continue

                            res += [str(i) + ' ' + str(j) + ' ' + str(step[2])]
                            s[step[0]][step[1]] = s[i][j]
                            s[i][j] = '.'
                            #walls = self.build(s)

            if len(res) == prevSize:
                break
            if len(res) > allowed:
                break
            prevSize = len(res)

        if len(res) > allowed:
            res = res[:allowed]

        return res
