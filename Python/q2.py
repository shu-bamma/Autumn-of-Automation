import sys
print("hello sir")
b=input("enter the palindrome")
def next_palindrome(a):
    s = str(a)
    n = len(s)
    k, r = divmod(n, 2)
    if r:
        left, mid, right = s[:k], s[k], s[k+1:]
        assert len(left) == len(right) == k
        assert s == left + mid + right
        print(s, left, mid, right)
        mid_n = int(mid)
        if left:
            left_n, right_n, right_n_rev = int(left), int(right), int(right[::-1])
            if left_n > right_n and left_n > right_n_rev:
                return int(left + mid + left[::-1])
            else:
                return int(left + str(mid_n+1) + left[::-1])
        else:
            return mid_n # 1-digit number
    else:
        left, right = s[:k], s[k:]
        assert len(left) == len(right) == k
        assert s == left + right
        print(s, left, right)
        left_n, right_n, right_n_rev = int(left), int(right), int(right[::-1])
        if left_n > right_n and left_n > right_n_rev:
            return int(left + left[::-1])
        else:
            new_left = str(left_n + 1)
            return int(new_left + new_left[::-1])


print(next_palindrome(b))