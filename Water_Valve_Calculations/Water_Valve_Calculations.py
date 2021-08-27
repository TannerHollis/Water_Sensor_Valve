r_top = 500e3
distances = [0.5, 1, 5, 10, 50]
r_water = 1.8e5

resistances = [r_water * d * 1e-3 for d in distances]

r_totals = []
for i in range(len(resistances)):
    for j in range(i, len(resistances)):
        r_temp = 0
        for k in range(i, j + 1):
            r_temp = r_temp + 1 / resistances[k]
        r_totals.append(1 / r_temp)

percentages = [r / (r_top + r) for r in r_totals]

with open('total_resistor_combonations.txt', 'w') as f:
    f.write("Different Combinations: {}\n".format(len(percentages)))
    f.write("Vout/Vin,Resistance(Ohms)\n")
    for i in range(len(percentages)):
        f.write("{},{}\n".format(percentages[i] * 100, r_totals[i]))