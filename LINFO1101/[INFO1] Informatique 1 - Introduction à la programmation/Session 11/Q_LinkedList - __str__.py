def __str__(self) :
    string_list = "[ "
    element = self.first()
    while element is not None :
        string_list += "{} ".format(element.value())
        element = element.next()
    return string_list + "]"
