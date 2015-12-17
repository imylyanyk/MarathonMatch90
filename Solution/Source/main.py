import sys


def log(*objs):
    print("LOG: ", *objs, file=sys.stderr)


class RollingBalls:
    def restorePattern(self, start, target):
        sa = []
        ta = []
        for s in start:
            sa += [list(s)]
        for s in target:
            ta += [list(s)]
        return tuple(self.algo1(sa, ta))

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


#### test code
H = int(input())
_start = []
_target = []
for i in range(H):
    _start += [input()]

H = int(input())
for i in range(H):
    _target += [input()]

o = RollingBalls()
ret = o.restorePattern(_start, _target)

# output
print(len(ret))
log("Res.size() = ", len(ret))
for s in ret:
    print(s)
    log(s)
sys.stdout.flush()

##### end of test code
