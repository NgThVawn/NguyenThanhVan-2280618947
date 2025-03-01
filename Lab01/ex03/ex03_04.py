def accessElement(tupleData):
    firstElement = tupleData[0]
    lastElement = tupleData[-1]
    return firstElement, lastElement
inputTuple = eval(input("Nhập vào một tuple: "))
first, last = accessElement(inputTuple)
print("Phần tử đầu tiên của tuple:", first)
print("Phần tử cuối cùng của tuple:", last)