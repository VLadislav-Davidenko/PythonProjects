def sum_of_intervals(intervals):
    result = set()
    for start, stop in intervals:
        for x in range(start, stop):
            result.add(x)
    return len(result)
print(sum_of_intervals([(1, 4), (7, 10), (3, 5)]))
print(sum_of_intervals([(-358, 187), (-231, 202), (-220, 188), (-186, 65), (-11, 65), (72, 384), (96, 418), (100, 103), (151, 335), (298, 413), (335, 447)]))
print(sum_of_intervals([(-475, -364), (-407, 370), (-343, 278), (-248, 362), (-172, 360), (-140, 262), (-91, 261), (-90, 87), (-9, 199), (60, 167), (66, 104), (147, 192), (247, 374), (342, 482), (344, 358), (428, 439), (445, 467)]))
print(sum_of_intervals([(-248, -105), (-237, 255), (-18, 217), (114, 163), (338, 364)]))