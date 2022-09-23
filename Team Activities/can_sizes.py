from math import pi

def main():
    can_sizes = [
        ["#1 Picnic", 6.83, 10.16, 0.28],
        ["#1 Tall", 7.78, 11.91, 0.43],
        ["#2", 8.73, 11.59, 0.45],
        ["#2.5", 10.32, 11.91, 0.61],
        ["#3 Cylinder", 10.79, 17.78, 0.86],
        ["#5", 13.02, 14.29, 0.83],
        ["#6Z", 5.4, 8.89, 0.22],
        ["#8Z short", 6.83, 7.62, 0.26],
        ["#10", 15.72, 17.78, 1.53],
        ["#211", 6.83, 12.38, 0.34],
        ["#300", 7.62, 11.27, 0.38],
        ["#303", 8.1, 11.11, 0.42],
        ["#4", 4.5, 12.58, 0.52]
    ]

    best_cost = 0
    best_cost_name = ""
    best_sto = 0
    best_sto_name = ""

    for i in range(len(can_sizes)):
        name = can_sizes[i][0]
        radius = can_sizes[i][1]
        height = can_sizes[i][2]
        cost = can_sizes[i][3]

        vol = compute_volume(radius, height)

        area = compute_surface_area(radius, height)

        eff = compute_storage_efficiency(vol, area)

        cost_eff = compute_cost_efficiency(vol, cost)

        if eff > best_sto:
            best_sto = eff
            best_sto_name = name
            best_sto_eff = eff
        
        if cost_eff > best_cost:
            best_cost = cost_eff
            best_cost_name = name
            best_cost_eff = cost_eff

        print(f"{name}, {vol:.2f}, {area:.2f}, {eff:.2f}")
    
    print()
    print(f"The can with the best storage efficiency is {best_sto_name} at {best_sto_eff}.")
    print(f"The can with the best cost efficiency is {best_cost_name} at {best_cost_eff}.")

def compute_volume(radius, height):
    vol = pi * radius ** 2 * height
    return vol

def compute_surface_area(radius, height):
    area = 2 * pi * radius * (radius + height)
    return area

def compute_storage_efficiency(vol, area):
    eff = vol / area
    return eff

def compute_cost_efficiency(vol, cost):
    cost_eff = vol / cost
    return cost_eff

main()