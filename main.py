from list import List


l1 = List()
for i in range(4):
    l1.push(f"Node value {i + 1}")

for i in l1:
    print(i.value)  # Just like built-in python lists
