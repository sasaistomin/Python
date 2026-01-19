# Append
listNum = [1, 2, 3]

listNum.append(4)
print(f"List: {listNum} \n")

# Sort
listNumber = [1, 4, 2, 3]

listNumber.sort(reverse=False)
print(f"List sort: {listNumber}")
listNumber.sort(reverse=True)
print(f"List reverse: {listNumber} \n")

# Copy
listOld = [1, 2, 3]
listNew = listOld

listNew.append(4)
print(f"List old: {listOld}")
print(f"List new: {listNew} \n")

# Delete
list = [1, 2, 3]
print(f"List: {list}")

del list[0]
print(f"List: {list}")