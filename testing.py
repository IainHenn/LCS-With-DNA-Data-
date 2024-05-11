
def binarySearchValueIndexEqual(plist):
    low = plist[0]
    high = plist[len(plist)-1]

    if high >= low:
        mid_index = int((high+low) / 2)
        mid_value = plist[mid_index]

        if mid_value == mid_index:
            return binarySearchValueIndexEqual(mid_index:)
        
        elif mid_value > mid:
            print("entering: " + str(plist))
            return binarySearchValueIndexEqual(plist[mid:])
        
        elif mid_value < mid:
            print("entering: " + str(plist))
            return binarySearchValueIndexEqual(plist[:mid])
        
        else:
            return plist
    
thelist = [1,2,3,4]
new = binarySearchValueIndexEqual(thelist)
print(new)