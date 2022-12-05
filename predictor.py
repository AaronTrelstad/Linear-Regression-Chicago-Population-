from statistics import mean
import numpy as np
import csv

y = 0
p = 0
t = []
ty = []
with open('chicago.csv') as f:
    reader = csv.reader(f)
    chicago = list(reader)
    for x in range(len(chicago)):
        t.append(int(chicago[x][1]) * int(chicago[x][0]))
        ty.append(int(chicago[x][0]) * int(chicago[x][0]))
        y += int(chicago[x][0])
        p += int(chicago[x][1])
ym = y/(len(chicago))
pm = p/(len(chicago))

def slope_intercept(ym, pm, y, p):
    m = ((ym*pm) - mean(t)) / ((ym*ym) - mean(ty))

    b = pm - m*ym

    return m, b

m, b = slope_intercept(ym, pm, y, p)

print(f"y = {m}x + {b}")

predict = input("Do you want to estimate the population at a specfic year(y/n)? ")
if predict.lower() == 'y':
    value = float(input("What year would you like to predict? "))
    print(f"Estimated population of {(m*value) + b} people")
if predict.lower() != 'y':
    exit