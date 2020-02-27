from csp import backtracking_search, NQueensCSP, min_conflicts, mrv, \
    forward_checking, AC3, CSP

# Create list of variables,
classes = ["cs108", "cs112", "cs212", "cs214", "cs262", "cs232"]


# Create list of domains,
not_domains = {
    "faculty":
        ["schuurman", "adams", "vanderlinden", "norman"],
    "time":
        ["mwf900", "mwf1030", "mwf1130", "tth1030"],
    "room":
        ["nh253", "sb382"]
}

# https://stackoverflow.com/questions/798854/all-combinations-of-a-list-of-lists
# Note: I first had it faculty, time, room, and then faculty one teacher would do the majority of teaching.
import itertools
a_fun_list = [not_domains["time"], not_domains["room"], not_domains["faculty"], ]
values = list(itertools.product(*a_fun_list))
print(values)

# https://www.geeksforgeeks.org/python-map-function/
domains = dict(map(lambda aClass: (aClass, values[:]), classes))
print(domains['cs108'])



# domains = {
#     "classes": {
#         "cs108": "schuurman",
#         "cs112": "adams",
#         "cs212": "vanderlinden",
#         "cs214": "norman",
#         "cs262": "adams",
#         "cs232": "norman",
#     },
#     "time":
#         ["mwf900", "mwf1030", "mwf1130", "tth1030"],
#     "room":
#         ["nh253", "sb382"]
# }



# Create list of constrains
def constraints(A, a, B, b):
    # They are the same class (var)

    # a and b are tuples in the form (time, room, faculty)
    print("A: " + str(A))
    print("B: " + str(B))
    print("a: " + str(a))
    print("b: " + str(b))
    if A == B:
        return True

    # check to make sure faculty is not teaching at the same time
    if a[0] == b[0] and a[2] == b[2]:
        return False

    # Check to make sure class is not in the same room at the same time
    if a[0] == b[0] and a[1] == b[1]:
        return False
    return True


#TODO: What are neighbors?
neighbors = {
    "cs108": ["cs112", "cs212", "cs214", "cs262", "cs232"],
    "cs112": ["cs108", "cs212", "cs214", "cs262", "cs232"],
    "cs212": ["cs108", "cs112", "cs214", "cs262", "cs232"],
    "cs214": ["cs108", "cs112", "cs212", "cs262", "cs232"],
    "cs262": ["cs108", "cs112", "cs212", "cs214", "cs232"],
    "cs232": ["cs108", "cs112", "cs212", "cs214", "cs262"]
}

# Pass all to CSP


class SchedulingCSP(CSP):

    def __init__(self, c, d, n, cs):
        CSP.__init__(self, c, d, n, cs)

    # def nconflicts(self, var, val, assignment):
    #     """Need to check conflits
    #     check if:
    #         more than on course being offered
    #         faculty member is teaching more than one course
    #         room has no more than one class at a time
    #         """


problem = SchedulingCSP(classes, domains, neighbors, constraints)

solution = backtracking_search(problem)

# # 3. Print the results.
# Handle AC3 solutions (boolean values) first, they behave differently.
if type(solution) is bool:
    if solution and problem.goal_test(problem.infer_assignment()):
        print('AC3 Solution:')
    else:
        print('AC Failure:')
    print(problem.curr_domains)

# Handle other solutions next.
elif solution is not None and problem.goal_test(solution):
    print('Solution:')
    print(solution)
#    problem.display(problem.infer_assignment())
else:
    print('Failed - domains: ' + str(problem.curr_domains))
    problem.display(problem.infer_assignment())

