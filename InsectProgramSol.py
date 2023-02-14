import InsectClassSol as i

bug1 = i.Insect("mosquito", 2, 4)
bug2 = i.Insect("housefly", 4, 8)


bug1.calc_flight()
bug2.calc_flight()

print(f"The {bug1.get_name()} can fly up to {bug1.get_flight()} miles.")

print(f"The {bug2.get_name()} can fly up to {bug2.get_flight()} miles.")
