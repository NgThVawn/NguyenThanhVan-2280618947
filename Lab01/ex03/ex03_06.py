def deleteItem(dict, key):
    if key in dict:
        del dict[key]
        return True
    else :
        return False
myDict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
key = 'b'
result = deleteItem(myDict, key)
if(result):
    print("Xóa phần tử thành công, Dictionary sau khi xóa:", myDict)
else:
    print("Không tìm thấy phần tử cần xóa trong Dictionary")