
# [1,2,3,4,5] > rot 2 > [3,4,5,1,2]


def rotate(array,rotation_factor):
    if rotation_factor <= 0:
        return array
    
    for index in range (rotation_factor):
        #print ('Checking: ', index, ' index position')
        array.append(array[0])
        array.pop(0)
    
    return array

    


if __name__ == '__main__':
    array = [1,2,3,4,5]
    rotation_factor = 2
    print(rotate(array,rotation_factor))