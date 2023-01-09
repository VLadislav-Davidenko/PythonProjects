def decodeBitsAdvanced(bits):
    # ToDo: Accept 0's and 1's, return dots, dashes and spaces
    return decodeMorse(bits.replace('000', ' ').replace('111', '-').replace('1', '.').replace('0', ''))
    #return decodeMorse("-.-.")
    #return bits.replace('000', ' ').replace('111', '-').replace('1', '.').replace('0', ' ')
    
def decodeMorse(morseCode):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    return morseCode.replace(' ', ' ').replace('-...', 'B').replace('-.-.', 'C').replace('..-.', 'F').replace('....', 'H').replace('.---', 'J').replace('.-..', 'L').replace('.--.', 'P').replace('...-', 'V').replace('-..-', 'X').replace('--.-', 'Q').replace('-.--', 'Y').replace("--..", "Z").replace('.--', 'W').replace('-..', 'D').replace('--.', 'G').replace('-.-', 'K').replace('---', 'O').replace('...', 'S').replace('.-.', 'R').replace('..-', 'U').replace('.-', 'A').replace('..', 'I').replace('--', 'M').replace('-.', 'N').replace('-', 'T').replace('.', 'E')

print(decodeBitsAdvanced("0000000011011010011100000110000001111110100111110011111100000000000111011111111011111011111000000101100011111100000111110011101100000100000"))
print(decodeBitsAdvanced("10111"))