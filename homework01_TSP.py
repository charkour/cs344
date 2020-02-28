from search import Problem, hill_climbing, simulated_annealing, exp_schedule
from random import shuffle, randint

# create matrix of distances.
distances = {}
cities = []

n = randint(5, 51)

# initialize matrix
for city in range(0, n):
    distances[city] = {}
    cities.append(city)

# generate random values
for city1 in range(0, n):
    for city2 in range(0, n):
        if city1 != city2:
            distances[city1][city2] = distances[city1][city2] = randint(1, 101)
        else:
            distances[city1][city2] = distances[city1][city2] = 0

# referenced: https://stackoverflow.com/questions/976882/shuffling-a-list-of-objects
shuffle(cities)


class TSPProblem(Problem):
    """TSPProblem inherits the Problem class.
    Expects the number of cities (int), initial state (int[]), and distances
    between cities (a dictionary matrix of ints as distances)
    This problem tries to find the shortest path between all of the points.
    The problem class wants to maximize the value to multiplying the value
    by negative one will allow the algorithm to (hopefully) find the optimal (shortest) path.
    The problem will return a solution as a list of cities, with the origin city only at the start.
    When calculating the path length, the distance from the last city to the origin is calculated.
    """

    def __init__(self, num, initial, dist):
        self.n = num
        self.initial = initial
        self.distances = dist

    def actions(self, curr_state):
        """Find the possible actions by swapping two cities"""
        actions = []
        for c1 in range(self.n):
            for c2 in range(self.n):
                tmp_state = curr_state[:]
                if c1 != city2:
                    # Swap two cities
                    tmp_state[c1], tmp_state[c2] = tmp_state[c2], tmp_state[c1]
                    actions.append(tmp_state)
        return actions

    def result(self, state, action):
        """Set the new state to the action"""
        new_state = action
        return new_state

    # No goal state check because we can never know the optimal (shortest) path

    def value(self, state):
        """Get cost of current state. Local search tries to maximize
        So by negating the value, the path will be the shortest possible.
        """
        value = 0;
        for n in range(0, self.n):
            value += self.distances[state[n]][state[(n + 1) % self.n]]
        return -1 * value

# Setup program
p = TSPProblem(n, cities, distances)

print('Initial path: ' + str(cities))
print('Initial value: ' + str(p.value(cities)))

hill_solution = hill_climbing(p)
print('\nHill-climbing:')
print('\tSolution Path:\t' + str(hill_solution))
print('\tValue:\t\t\t' + str(p.value(hill_solution)))
print('\tTotal Length:\t' + str(-1 * p.value(hill_solution)))

# adapted from u02local/queens.py
annealing_solution = simulated_annealing(p, exp_schedule(k=20, lam=0.005, limit=10000))
print('\nSimulated annealing:')
print('\tSolution Path:\t' + str(annealing_solution))
print('\tValue:\t\t\t' + str(p.value(annealing_solution)))
print('\tTotal Length:\t' + str(-1 * p.value(annealing_solution)))
