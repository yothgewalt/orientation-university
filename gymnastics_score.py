d1, d2, d3, d4 = [float(score) for score in input().split()]
score_list: list[float] = sorted([d1, d2, d3, d4])

print((score_list[1] + score_list[2]) / 2)

