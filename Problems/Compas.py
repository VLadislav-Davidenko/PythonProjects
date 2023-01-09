def direction(facing, turn):
    letters = ['N','NE','E','SE','S','SW','W','NW']
    degrees = [0,45,90,135,180,225,270,315]
    res = degrees[letters.index(facing)] + turn
    if res >= 360:
        res -= ((res//360) * 360)
    if res < 0:
        res -= ((res//360) * 360)
    #return letters[degrees.index(res)]
    return letters[(turn // 45 + letters.index(facing)) % 8]

print(direction("E", -135))