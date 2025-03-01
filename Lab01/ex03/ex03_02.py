def reverseList(lst):
    return lst[::-1]
inputList = input("Nhập vào một dãy số, cách nhau bởi dấu phẩy: ")
numbers = list(map(int, inputList.split(',')))
result = reverseList(numbers)
print("Dãy số sau khi đảo ngược là:", result)