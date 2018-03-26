
import sys
import os


def findNumber(arr, k):
    out = []
    for i, v in enumerate(arr):
        if v == k:
            print  "yes"
        else:
            print "no"
    print arr
    print k
    return arr, k


# f = open(os.environ['OUTPUT_PATH'], 'w')

_arr_cnt = 0
_arr_cnt = int(raw_input("n: "))
_arr_i = 0
_arr = []
while _arr_i < _arr_cnt:
    _arr_item = int(raw_input("m: "));
    _arr.append(_arr_item)
    _arr_i += 1

_k = int(raw_input("o: "));

res = findNumber(_arr, _k)
# f.write(res + "\n")
#
# f.close()
