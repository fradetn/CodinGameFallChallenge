import sys
import math as m
import random

class Drone:
    def __init__(self, id, x, y, emmergency, battery):
        self.id = id
        self.x = x
        self.y = y
        self.emmergency = emmergency
        self.battery = battery

class Fish:
    def __init__(self, id, color, type, x, y, vx, vy):
        self.id = id
        self.color = color
        self.type = type
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

class Scan:
    def __init__(self, drone_id, fish_id):
        self.drone_id = drone_id
        self.fish_id = fish_id

class Radar:
    def __init__(self, drone_id, fish_id, radar):
        self.drone_id = drone_id
        self.fish_id = fish_id
        self.radar = radar

def get_fish(fish_id, all_fish):
    for i in all_fish:
        if (fish_id == i.id):
            return i
    return Fish(0, 0, 0, 0, 0, 0, 0)

def get_unscan_fish(all_fish, scans):
    unscan_fish = []
    for i in all_fish:
        if ((not i.id in scans) and i.type != -1):
            unscan_fish.append(i)
    return unscan_fish

def is_alltype_scanned(type, all_my_scans, all_fish):
    count = 0
    for i in all_my_scans:
        for j in all_fish:
            if (i == j.id):
                if (j.type == type):
                    count += 1
    if (count == 4):
        return 1
    else:
        return 0

def get_nb_fish(drone_id, my_radar, radar):
    count = 0
    for i in my_radar:
        if (my_radar.radar == radar and drone_id == i.drone_id):
            count += 1
    return count

def get_all_my_scans(unsave_scans, save_scans):
    all_scans = []
    for i in unsave_scans:
        all_scans.append(i)
    for j in save_scans:
        all_scans.append(j)
    return all_scans

def get_my_unsavescans(my_drones, unsave_scans):
    my_unsave_scans = []

    for drone in my_drones:
        for i in unsave_scans:
            if (i.drone_id == drone.id):
                my_unsave_scans.append(i.fish_id)
    return my_unsave_scans

def is_monster(all_fish, fish_id):
    for i in all_fish:
        if (i.id == fish_id and i.type == -1):
            return 1
    return 0

def get_closest_monster(drone, visible, all_fish):
    final_dist = 100000
    monster = Fish(0, 0, 0, 0, 0, 0, 0)
    for i in visible:
        if (is_monster(all_fish, i.id) == 1):
            dist = get_distance(drone, i)
            if (dist < final_dist):
                final_dist = dist
                monster = i
    return monster

def get_distance(drone, fish):
    add = ((fish.x - drone.x) ** 2) + ((fish.y - drone.y) ** 2)
    return (int(m.sqrt(add)))

def get_direction_fish(my_radar, unscan_fish, _type):
    for radar in my_radar:
        for fish in unscan_fish:
            if (fish.id == radar.fish_id):
                if (fish.type == _type):
                    return radar.radar
    return 0
    

# Score points by scanning valuable fish faster than your opponent.
all_fish = [] # Toutes les creatures du jeu
creature_count = int(input())
for i in range(creature_count):
    creature_id, color, _type = [int(j) for j in input().split()]
    all_fish.append(Fish(creature_id, color, _type, 0, 0, 0, 0))

# game loop
while True:
    my_score = int(input())
    foe_score = int(input())

    save_scans = [] # scans sauvegardés
    my_scan_count = int(input())
    for i in range(my_scan_count):
        creature_id = int(input())
        save_scans.append(creature_id)
    foe_scan_count = int(input())
    for i in range(foe_scan_count):
        creature_id = int(input())

    my_drones = [] # Tous mes drones
    my_drone_count = int(input())
    for i in range(my_drone_count):
        drone_id, drone_x, drone_y, emergency, battery = [int(j) for j in input().split()]
        my_drones.append(Drone(drone_id, drone_x, drone_y, emergency, battery))
    foe_drone = [] # drones ennemis
    foe_drone_count = int(input())
    for i in range(foe_drone_count):
        drone_id, drone_x, drone_y, emergency, battery = [int(j) for j in input().split()]
        foe_drone.append(Drone(drone_id, drone_x, drone_y, emergency, battery))

    unsave_scans = [] # scans non sauvegardés
    drone_scan_count = int(input())
    for i in range(drone_scan_count):
        drone_id, creature_id = [int(j) for j in input().split()]
        unsave_scans.append(Scan(drone_id, creature_id))


    visible_fish = [] # creatures visibles
    visible_creature_count = int(input())
    for i in range(visible_creature_count):
        creature_id, creature_x, creature_y, creature_vx, creature_vy = [int(j) for j in input().split()]
        visible_fish.append(Fish(creature_id, 0, 0, creature_x, creature_y, creature_vx, creature_vy))

    my_radar = []
    radar_blip_count = int(input())
    for i in range(radar_blip_count):
        inputs = input().split()
        drone_id = int(inputs[0])
        creature_id = int(inputs[1])
        radar = inputs[2]
        my_radar.append(Radar(drone_id, creature_id, radar))

    my_unsave_scans = get_my_unsavescans(my_drones, unsave_scans)
    all_my_scans = get_all_my_scans(my_unsave_scans, save_scans)
    unscan_fish = get_unscan_fish(all_fish, all_my_scans)
    
    #--------------------- Boucle d'instructions ---------------------# 

    # Mes variables :
    # - my_drones       --> Tous mes drones
    # - foe_drone       --> Tous les drones ennemis
    # - all_my_scans    --> Tous les scans effectués (sauvegardés et non sauvegardés) : tableau d'entiers
    # - my_unsave_scans --> Tous les scans effectués non sauvegardés par mes drones : tableau d'entiers
    # - unsave_scans    --> Tous les scans effectués non sauvegardés : tableau de Scan
    # - save_scans      --> Tous les scans effectués sauvegardés : tableau d'entier
    # - all_fish        --> Toutes les creatures : tableau de Fish
    # - unscan_fish     --> Toutes les creatures non scannées : Tableau de Fish
    # - visible_fish    --> Toutes les creatures visibles


    i = 0
    for drone in my_drones:
        # Si le drone a moins de 5 de batterie,
        # on etteint la light et on defini la zone safe à 800
        #Sinon, on allume et on defini la zone safe à 2000
        if (drone.battery < 5):
            light = 0
            safe = 800
        else:
            light = 1
            safe = 2000
        print("drone id =", drone.id, file = sys.stderr)
        for j in all_fish:
            print(j.id, file = sys.stderr)
        _type = 0 if i == 0 else 2

        # On cherche le monstre visible le plus proche
        monster = get_closest_monster(drone, visible_fish, all_fish)
        distance = get_distance(drone, monster)
        
        # Si un monstre est visible et est à moins de safe + 300 unités du drone
        # on essaie de l'esquiver
        if (monster.id != 0 and distance < safe + 300):
            futur_x = monster.x + monster.vx
            futur_y = monster.y + monster.vy
            print(futur_x - drone.x, futur_y - drone.y, file = sys.stderr)
            print("MOVE", futur_x - drone.x, futur_y - drone.y, light, distance)

        # Si on a scanné tous les poisson du type recherché, 
        # on remonte a la suface
        elif (is_alltype_scanned(_type, all_my_scans, all_fish) == 1):
            print("MOVE", drone.x, 0, 0)

        # Sinon, on cherche les poissons
        else:
            target = get_direction_fish(my_radar, all_fish, _type)
            if (target == "BR"):
                print("MOVE 9999 9999", light, target, "type", _type)
            elif (target == "BL"):
                print("MOVE 0 9999", light, target, "type", _type)
            elif (target == "TR"):
                print("MOVE 9999 0", light, target, "type", _type)
            elif (target == "TL"):
                print("MOVE 0 0", light, target, "type", _type)
        i += 1
