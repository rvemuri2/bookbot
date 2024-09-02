arr = ["hello", "this", "is", "me"]
h = {}
for i in arr:
    lowercase_string = i.lower()
    for j in lowercase_string:
        h[j] = h.get(j, 0) + 1

print(h)

