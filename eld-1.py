def element_skip(elements):
    for index, element in enumerate(elements):
     if index%2 == 0:
            print(element)



element_skip(["a","b","c","b","f"])