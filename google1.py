def solution(x):
    y = ''
    for char in x:
        if char >= 'a' and char <= 'z':
            y += chr(ord('z') - (ord(char) - ord('a')))
        else: 
            y += char
    return y

print(solution("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"))