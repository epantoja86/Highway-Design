"""python"""

import numpy as np

W = 11.1 * 1000 #N
L = 3.048 #m
h = 0.559 #m
lf = 1.12 #m
lr = L - lf #m
mu = 0.6
frl = 0.01

def max_traction_front(l):
    top = mu * W * (l + frl * h) / L
    btm = (1 + mu * h / L)
    return  top / btm

def max_traction_rear(l):
    top = mu * W * (l - frl * h) / L
    btm = (1 - mu * h / L)
    return  top / btm

print(f"\nThe max tractive effort with current FWD wheelbase ({L}m) is : {round(max_traction_front(lr),3)} N")
print(f"The max tractive effort with current RWD wheelbase ({L}m) is : {round(max_traction_rear(lf),3)} N")