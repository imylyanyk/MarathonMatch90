import sys

class RollingBalls:
    def restorePattern(self, start, target):
        return ("0 2 1")

    def algo1(self, s, t):
        #trying to reach within one move
        n = len(s)
        m = len(s[0])
        for i in range(n):
            for j in range(m):
                if s[i][j].isdigit() and !target[i][j].isdigit():
                    #investigate all directions (U,D,L,R)
                    it = i - 1
                    while it >= 0 and s[it][j].isdigit():
                        
                        it -= 1

#### test code
H = int(input())
start = []
target = []
for i in range(H):
    start += [input()]

H = int(input())
for i in range(H):
    target += [input()]

o = RollingBalls()
ret = o.restorePattern(start, target)

#output
print(len(ret))
for s in ret:
    print(s)
sys.stdout.flush()

##### end of test code