from collections import Counter
# Two cases, string length is gt than size
# string length is lt than size (we need to repeat the string)


# Case 2. Size is greater than string.
# Here we need to build the 
def fill_string(size,string):
    new_string = ''
    while len(new_string) <= size:
        new_string = new_string + string
    return new_string


def repeated_string(size,string):
    # if we have a big size with a single 'a' return just the size.
    if string == 'a':
        return size
    
    if len(string) < size:
        string = fill_string(size,string)    
    #trim
    string = string[:size]
    #get the number of occurences of 'a'
    return (Counter(string).get('a'))

if __name__ == '__main__':
    repeated_string(10,'abc')