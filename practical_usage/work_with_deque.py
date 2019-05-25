"""
    deque stands for 'double-ended queue', which is a generalization of stacks and queues
"""
from collections import deque
d = deque(['g']*10000000)
arr = ['g']*10000000
def drop(d):
    del d[0]

drop(d)
"""
%%time del d[0]: Wall time: 10 µs
%%time del arr[0]: Wall time: 8.99 ms
"""

##############################
"""
%time del d[-1]: Wall time: 9.06 µs
%time del arr[-1]: Wall time: 6.91 µs
"""