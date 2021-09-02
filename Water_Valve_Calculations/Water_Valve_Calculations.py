import math
from UliEngineering.Electronics.Resistors import *
r_round = 5e3

r_top = 500e3
distances = [0.5, 1, 2, 4, 6] #millimeters
area = (0.5e-3 * math.pi) * (1e-2) * 2 #probe contact area
r_water = 2e3

def combo_str(combo):
    string = ""
    for j in range(len(combo)):
        string = string + "{}".format(combo[j]) + "\t"
    return string

resistances = [r_water * ( d * 1e-3 / area) for d in distances]
resistances = [nearest_resistor(r, sequence=e96) for r in resistances]
combos = "".join(["R{}\t".format(i+1) for i in range(len(resistances))])
r_combos = []
r_totals = []

for i in range(len(resistances)):
    for j in range(len(resistances) - 1, i - 1, -1):
        r_temp = 0
        r_combo = [0] * len(distances)
        for k in range(j, i - 1,  -1):
            r_combo[k] = 1
            r_temp = r_temp + 1 / resistances[k]
        r_combos.append(r_combo)
        r_totals.append(1 / r_temp)

percentages = [r / (r_top + r) for r in r_totals]

with open('total_resistor_combinations.txt', 'w') as f:
    f.write("Different Combinations: {}\n".format(len(percentages)))
    for i in range(len(resistances)):
        f.write("R{}\t{:.2f}\n".format(i+1, resistances[i]))
    f.write("\n{}Vout/Vin(%)\t\tResistance(Ohms)\n".format(combos))
    for i in range(len(percentages)):
        f.write("{}{:<8.5f}\t\t{:<12.5f}\n".format(combo_str(r_combos[i]), percentages[i] * 100, r_totals[i]))
