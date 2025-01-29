import math

def main():
    cans = []

    class Can:
        def __init__(self, name, radius, height, cost):
            self.name = name
            self.radius = radius
            self.height = height
            self.cost = cost


    with open('cans.txt','r') as cans_file:
        for line in cans_file:
            name, radius, height, cost = line.split('\t')
            radius = float(radius)
            height = float(height)
            cost = float(cost[1:])
            cans.append(Can(name, radius, height, cost))

    for can in cans:
        print(f"{can.name}'s storage efficiency is {compute_storage_efficiency(can.radius, can.height):.2f} and cost efficiency is {compute_cost_efficiency(can.radius, can.height, can.cost):.2f}")

def compute_volume(radius, height):
    return math.pi * radius ** 2 * height

def compute_surface_area(radius, height):
    return 2 * math.pi * radius * (radius + height)

def compute_storage_efficiency(radius, height):
    return compute_volume(radius,height) / compute_surface_area(radius,height)

def compute_cost_efficiency(radius, height, cost):
    return compute_volume(radius, height) / cost


main()