def skip_list(elements):
    new_list = []
    i = 0

    for element in elements:
        if elements.index(element) == i:

            new_list.append(element)
            i += 2

    return new_list


print(skip_list(['a', 'thus', 'send', 'bo', 'do', 'do', 'set']))
