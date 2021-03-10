### [1] Counter 사용법
```sh
from collections import Counter
```

### [2] 숫자를 문자열로 만들때, 자릿수 맞추기
```sh
"1".zfill(8)
# -> 00000001

"1".rjust(8, '0')
# -> 00000001

"1".ljust(8, '0')
# -> 10000000

print("%08d" % 1)
# -> 00000001
```

