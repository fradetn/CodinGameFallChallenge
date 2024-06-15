import sys
import math

class Race:
    def __init__(self, piste, pos, etourd):
        self.piste = piste
        self.pos = pos
        self.etourd = etourd

    def get_dist(self):
        pos = self.pos[p_id]
        piste = self.piste
        dist = 0
        coucou = 1
        for i in range(pos, len(piste)):
            if piste[pos] != '#' and dist != 0:
                if (piste[i] == '#'):
                    return(dist)
            dist += 1
        dist = 200
        return dist

    def race_solver(self):
        solution = {"UP": 0, "RIGHT": 0, "DOWN": 0, "LEFT": 0}
        dist = self.get_dist()
        print("pos :", self.pos[p_id], file=sys.stderr)
        print("dist :", dist, file=sys.stderr)
        if self.etourd[p_id] > 0:
            return (solution)
        if (dist > 3):
            solution["RIGHT"] = 4
            solution["UP"] = 3
            solution["DOWN"] = 3
            solution["LEFT"] = 2
        elif (dist == 2):
            solution["LEFT"] = 5
        elif (dist <= 1):
            solution["UP"] = 5
        else:
            solution["DOWN"] = 3
            solution["UP"] = 3
            solution["LEFT"] = 2
        print(solution, file=sys.stderr)
        return solution

def solver(r):
    all_solver = {"UP": 0, "RIGHT": 0, "DOWN": 0, "LEFT": 0}
    for i in r:
        for key in all_solver.keys():
            all_solver[key] += i.get(key, 0)
    
    print(all_solver, file=sys.stderr)
    max_key = max(all_solver, key=lambda x:all_solver[x])
    print(max_key)

    
    

p_id = int(input())
nb_games = int(input())

# game loop
while True:
    games = []
    all_solver = []
    for i in range(3):
        score_info = input()
    for i in range(nb_games):
        inputs = input().split()
        gpu = inputs[0]
        reg_0 = int(inputs[1])
        reg_1 = int(inputs[2])
        reg_2 = int(inputs[3])
        reg_3 = int(inputs[4])
        reg_4 = int(inputs[5])
        reg_5 = int(inputs[6])
        reg_6 = int(inputs[7])


        game = Race(gpu, [reg_0,reg_1,reg_2], [reg_3, reg_4, reg_5])
        games.append(game)
    for i in games:
        all_solver.append(i.race_solver())
    solver(all_solver)

