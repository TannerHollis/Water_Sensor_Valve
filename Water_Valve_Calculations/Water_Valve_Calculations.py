r_top = 500e3
distances = [0.5, 1, 5, 10, 50]
r_water = 1.8e5

def combo_str(combo):
    string = ""
    for j in range(len(combo)):
        string = string + "{}".format(combo[j]) + ","
    return string

resistances = [r_water * d * 1e-3 for d in distances]
combos = "R1, R2, R3, R4, R5"
r_combos = []
r_totals = []

for i in range(len(resistances)):
    for j in range(i, len(resistances)):
        r_temp = 0
        r_combo = [0,0,0,0,0]
        for k in range(i, j + 1):
            r_combo[k] = 1
            r_temp = r_temp + 1 / resistances[k]
        r_combos.append(r_combo)
        r_totals.append(1 / r_temp)

percentages = [r / (r_top + r) for r in r_totals]

with open('total_resistor_combinations.txt', 'w') as f:
    f.write("Different Combinations: {}\n".format(len(percentages)))
    f.write("{}, Vout/Vin, Resistance(Ohms)\n".format(combos))
    for i in range(len(percentages)):
        f.write("{}{},{}\n".format(combo_str(r_combos[i]), percentages[i] * 100, r_totals[i]))
