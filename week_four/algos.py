def binarySearch(listToSearch, item):
   # listToSearch.sort()
    if len(listToSearch) == 0:
        return False
    lowerBound = 0
    upperBound = len(listToSearch)-1
    if listToSearch[lowerBound] == item or listToSearch[upperBound] == item:
        return True
    while (upperBound - lowerBound) > 1:
        midPoint = (lowerBound + upperBound)//2
        midVal = listToSearch[midPoint]
        if midVal == item:
            return True
        if item < midVal:
            upperBound = midPoint
        else:
            lowerBound = midPoint
        
    return False

my_list = [0,3,7,12,15,18,19]
second_list = [5, 2, 47, 1, 55, 8]
#print( binarySearch(my_list, 3))
#print( binarySearch(my_list, 5))
#print( binarySearch(sorted(second_list), 47))
#print( binarySearch(sorted(second_list), 42)) 
#string_list = [ 420, 1, "Mike","Pat","Troy"]
#print(binarySearch(string_list, "Pat"))
#print(binarySearch(string_list, "Not_Pat_Jones"))


