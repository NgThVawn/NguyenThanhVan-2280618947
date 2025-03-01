def countDict(lst):
    dict = {}
    for num in lst:
        if num in dict:
            dict[num] += 1
        else:
            dict[num] = 1
    return dict
inputString = input("Nhập vào các từ, cách nhau bởi dấu cách: ")
words = inputString.split()
result = countDict(words)
print("Số lần xuất hiện của các từ:", result)