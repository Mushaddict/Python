import numpy as np
n=np.frombuffer(b'mingrisoft',dtype='S1')
print(n)

import array
a = array.array("i", [1, 2, 3, 4])
na = np.frombuffer(a, dtype=int)
print(na)
a.append(5)
print(na)

