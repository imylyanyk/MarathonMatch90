import demo_data as data
import helpers as helper
import RollingBalls as rb

r = rb.RollingBalls()

helper._log = True
r.restorePattern(data.start, data.target)