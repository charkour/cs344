from search import UndirectedGraph, Problem, hill_climbing, simulated_annealing, exp_schedule

print('Here\'s the problem formulation.')

# romania_map = UndirectedGraph(dict(
#     A=dict(B=10, C=20, D=30),
#     B=dict(C=40, D=50),
#     C=dict(D=60)
# ))

# Create matrix of distances.
distances = {}
cities = []

n = 5
for city in range(0, n):
    distances[city] = {}
    cities.append(city)


## TODO: Need to make a random number of cities and distances!!!

distances[0][1] = 12
distances[0][2] = 10
distances[0][3] = 19
distances[0][4] = 8
distances[1][2] = 3
distances[1][3] = 7
distances[1][4] = 2
distances[2][3] = 6
distances[2][4] = 20
distances[3][4] = 4

distances[1][0] = 12
distances[2][0] = 10
distances[3][0] = 19
distances[4][0] = 8
distances[2][1] = 3
distances[3][1] = 7
distances[4][1] = 2
distances[3][2] = 6
distances[4][2] = 20
distances[4][3] = 4

random_start_state = [0, 1, 2, 3, 4]


class TSPProblem(Problem):

    def __init__(self, num, initial, distances):
        self.n = num
        self.initial = initial
        self.distances = distances

    def actions(self, state):
        actions = []
        for city1 in range(self.n):
            for city2 in range(self.n):
                copy_state = state[:]
                if city1 != city2:
                    # Swap two cities
                    copy_state[city1], copy_state[city2] = copy_state[city2], copy_state[city1]
                    actions.append(copy_state)
        return actions

    def result(self, state, action):
        """Set the new state to the aciton"""
        new_state = action
        return new_state

    # def path_cost(self, c, state1, action, state2):
    #     """Add up all of the distances"""
    #     cost = 0;
    #     for n in range(0, self.n):
    #         cost += self.distances[state2[n]][state2[(n + 1) % self.n]]
    #     return cost

    # TODO: Need to check the goal state? make sure it is valid?


    def value(self, state):
        """Get cost of current state. HC tries to maximize"""
        # return -1 * self.path_cost(None, None, None, state)
        cost = 0;
        for n in range(0, self.n):
            cost += self.distances[state[n]][state[(n + 1) % self.n]]
        return -1 * cost

# https://stackoverflow.com/questions/976882/shuffling-a-list-of-objects
from random import shuffle
shuffle(random_start_state)
print(random_start_state)

p = TSPProblem(n, random_start_state, distances)



# print(cities)

print(p.value(random_start_state))
print(p.initial)

print(p.actions(random_start_state))

hill_solution = hill_climbing(p)
print('\nHill-climbing:')
print('\tSolution:\t' + str(hill_solution))
print('\tValue:\t\t' + str(p.value(hill_solution)))

# Solve the problem using simulated annealing.
annealing_solution = \
    simulated_annealing(p, exp_schedule(k=20, lam=0.005, limit=10000))
print('\nSimulated annealing:')
print('\tSolution:\t' + str(annealing_solution))
print('\tValue:\t\t' + str(p.value(annealing_solution)))