from morsecode import morsecode as code

def english_to_morse(string):
    string = str(string).upper()
    morse_code_string = ''
    for char in string:
        if char in list(code.keys()):
            morse_code_string+= code[char]
        else:
            continue
    morse_file = open('Morse-Code-Fall.txt','w')
    morse_file.write(morse_code_string)
    morse_file.close()
    print("THE TEXT HAS BEEN WRITTEN INTO Morse-Code-Fall.txt IN MORSE CODE.")


english_to_morse('He fumbled in the darkness looking for the light switch, but when he finally found it there was someone already there.')