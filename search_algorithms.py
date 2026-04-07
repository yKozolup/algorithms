# Linear search
array = [5, 9, 0, -2, 12, 14, 9, 4, 7, 8]
key = int(input())
is_find = False
for item in array:
    if item == key:
        is_find = True
        break
if is_find:
    print("Success")
else:
    print("Not found")
# Complexity - O(n)