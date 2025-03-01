def sumEvenNumbers(n):
    sum = 0
    for num in lst:
        if num % 2 == 0:
            sum += num
    return sum
inputList = input("Nhập vào một dãy số, cách nhau bởi dấu phẩy: ")
lst = list(map(int, inputList.split(',')))
print("Tổng các số chẵn trong dãy số là:", sumEvenNumbers(lst))