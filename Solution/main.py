import time

import RollingBalls as rb
import helpers as helper

#### test code
H = int(input())
_start = []
_target = []
for i in range(H):
    _start += [input()]

H = int(input())
for i in range(H):
    _target += [input()]

o = rb.RollingBalls()

helper._log = False
start = time.time()
ret = o.restorePattern(_start, _target)
end = time.time()
helper._log = True

# output
print(len(ret))
helper.log("Res.size() = ", len(ret))
helper.log("time =", end-start)
for s in ret:
    print(s)
    #helper.log(s)
helper.sys.stdout.flush()

##### end of test code
