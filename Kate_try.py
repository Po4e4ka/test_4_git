def decodeMorse(morse_code):
    words = morse_code.split('   ')
    buks = []
    result = []
    for i in words:
        buks += [i for i in i.split(' ') if i!= ''] + [' ']




    print(buks)

decodeMorse(' . ')
