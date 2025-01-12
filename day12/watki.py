# koorutyny

from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=20) as executor:
    for i in range(20):
        executor.submit(print,i)

# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 910
#
# 11
# 12
# 1314
# 15
#
# 16
# 1718
# 19

