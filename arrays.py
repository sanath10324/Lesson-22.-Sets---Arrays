import array as arr

array_num = arr.array('i', [1, 2, 3, 4, 3, 4, 5, 6, 3])
print("Original number array:"+ str(array_num))

print("Number of occurences for the numebr 3 in the array is:"+str(array_num.count(3)))

array_num.reverse()
print("Reversed type of array:"+str(array_num))