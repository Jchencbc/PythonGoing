

# yield form 实现伪代码

RESULT = yield from EXPR
################################

_i = iter(EXPR)
try:
    _y = next(_i)
except StopIteration as _e:
    _r = _e.value
else:
    while 1:
        try:
            _s = yield _y
    else:
        try:
            if _s is None:
                _y = next(_i)
            else:
                _y = _i.send(_s)
        except StopIteration as _e:
            _r = _e.value
            break
RESULT = _r
        
        
