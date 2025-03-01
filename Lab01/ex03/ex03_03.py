def createTuple(lst):
    return tuple(lst)
inputList = input("Nhập vào một dãy số, cách nhau bởi dấu phẩy: ")
numbers = list(map(int, inputList.split(',')))
result = createTuple(numbers)
print("List:", numbers)
print("Tuple từ List:", result)