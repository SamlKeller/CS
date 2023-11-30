def test ():
    string = "AbAB"
    text = input("Input two letters to switch:")
    
    string = string.replace(text[1], '^`^`')
    string = string.replace(text[0], text[1])
    string = string.replace('^`^`', text[0])

    string = string.replace(text[1].upper(), '^`^`')
    string = string.replace(text[0].upper(), text[1].upper())
    string = string.replace('^`^`', text[0].upper())

    print(string)

test()