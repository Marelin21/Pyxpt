"""
ip_arr = [2,3,4,5,6]
target = 9

idx1 = 2 idx2 = 3
idx1 = 1 idx2 = 4
"""

def two_sum(ip_arr, target):
    for idx, x in enumerate(ip_arr):
        # 0 2
        # 1 3
        # 2 4
        # ..

        newarr = ip_arr[idx + 1 : ] # ip[1: ] [3 4 5 6 ]
        print("iter", x, idx, newarr)

        for idx2, y in enumerate(newarr):
            if x + y == target:
                return [idx, idx + idx2 + 1]


def two_sum2(ip_arr, target = 10):
    mp = {}

    for idx, x in enumerate(ip_arr):
        if x in mp:
            return [idx, mp[x]] if idx < mp[x] else [mp[x], idx]
        else:
            mp[target - x] = idx    #mp[7] = 0 mp[6]= 1 mp[5] = 2
    return

def add_num(x = 10: int, y = 20)-> int:
    return x + y

def main():
    # inputs
    ip_arr = [2, 3, 4, 5, 6]
    target = 9

    print(two_sum2(ip_arr, target))

    print(add_num(2,3))
    print(add_num(2))
    print(add_num())
    #i += 1 # i++

class Bubble:
    def __init__(self):
        self.name = "bubble"
        self.val = None
    
    def setVal(self, val):
        self.val = val




if __name__ == '__main__':
    main()
