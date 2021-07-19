from morsecode import morsecode as code

def english_to_morse(string):
    string = str(string).upper()
    morse_code_string = ''
    for char in string:
        if char in list(code.keys()):
            morse_code_string+= code[char]
            morse_code_string += '/'
        else:
            continue
    morse_file = open('Morse-Code-File.txt','w')
    morse_file.write(morse_code_string)
    morse_file.close()
    print("THE TEXT HAS BEEN WRITTEN INTO Morse-Code-Fall.txt IN MORSE CODE.")
    return morse_code_string

def morse_to_enlish(string):
    print('Please seperate each character witha space')
    dic_of_morsecode = {}
    n_string = ''
    for key, value in code.items():
        dic_of_morsecode[value] = key
    for group in string.split('/'):
        n_string +=  str(dic_of_morsecode[group])
    english_file = open('English-File.txt','w')
    english_file.write(n_string)
    english_file.close()
    print("THE TEXT HAS BEEN WRITTEN INTO English-File.txt IN MORSE CODE.")
    return n_string

english_to_morse('Jam Fish')
print(morse_to_enlish('•---/•-/--/|/••-•/••/•••/••••/'))
