from csp import backtracking_search, NQueensCSP, min_conflicts, mrv, \
    forward_checking, AC3, CSP

class SchedulingCSP(CSP):

    def nconflicts(self, var, val, assignment):
        """Need to check conflits
        check if:
            more than on course being offered
            faculty member is teaching more than one course
            room has no more than one class at a time
            """