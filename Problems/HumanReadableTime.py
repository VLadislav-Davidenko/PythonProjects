def make_readable(seconds):
    HH = seconds // 3600
    MM = (seconds - HH*3600) // 60
    SS = seconds % 60
    #if HH < 10:
        #HH = "0" + str(HH)
    #if MM < 10:
        #MM = "0" + str(MM)
    #if SS < 10:
        #SS = "0" + str(SS)
    #return str(HH) + ":" + str(MM) + ":" + str(SS)
    return '{:02}:{:02}:{:02}'.format(HH, MM, SS)
print(make_readable(86399))
print(make_readable(1))