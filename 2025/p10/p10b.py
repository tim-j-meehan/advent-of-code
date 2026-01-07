import sys
from scipy.signal import convolve2d
import numpy as np
from itertools import combinations
sys.path.append("../../pylib")
import aoclib
import copy
import pprint
import networkx as nx
from scipy.optimize import linprog
from scipy.optimize import milp, LinearConstraint, Bounds
cnt = 0

#48 too low?
#48+21  too hight
#48 + 10 58
#48 + 1 49
#48 + 2 50
#48 + 3 51
# 16752
# 16753

#16748

#Im stuck on this one

# this problem is equiv to min ||x||_1 subject to Ax=b

fp = open(sys.argv[1])



def solve_min_l1_integer(A, b):
    m, n = A.shape
    
    #objective
    c = np.concatenate([np.zeros(n), np.ones(m)])
    
    # 2. Define inequality constraints (A_ub, b_ub in linprog terms, but milp uses LinearConstraint)
    # The constraints are: Ax - y <= b  and  -Ax - y <= -b
    # The full A_ineq matrix for [x, y] is:
    # [ A, -I ]
    # [-A, -I ]
    I = np.identity(m)
    A_ineq_upper = np.hstack([A, -I])
    A_ineq_lower = np.hstack([-A, -I])
    A_ineq = np.vstack([A_ineq_upper, A_ineq_lower])
    
    # The corresponding b_ineq vector is:
    # [ b ]
    # [-b ]
    b_ineq = np.concatenate([b, -b])
    
    # Use LinearConstraint for SciPy milp
    constraints = [LinearConstraint(A_ineq, np.full(2*m, -np.inf), b_ineq)] # b_l <= A_ineq @ vars <= b_u

    # 3. Define variable bounds (l <= x <= u)
    # x can be any integer, y must be non-negative. Use None for no bounds.
    # By default, milp assumes non-negative bounds unless specified otherwise.
    # Explicitly set x bounds to (-inf, inf) and y bounds to [0, inf).
    x_bounds = np.full(n, np.inf)
    y_bounds = np.full(m, np.inf)
    lb = np.concatenate([-x_bounds, np.zeros(m)])
    ub = np.concatenate([x_bounds, y_bounds])
    bounds = Bounds(lb, ub)
    
    # 4. Define integrality constraints
    # All x variables must be integers (1). y variables are continuous (0).
    integrality = np.concatenate([np.ones(n), np.zeros(m)])

    # 5. Solve the MILP
    result = milp(c=c, constraints=constraints, bounds=bounds, integrality=integrality)
    
    if result.success:
        # The first n elements of result.x are the integer solutions for x
        x_solution = result.x[:n]
        x_solution = np.round(x_solution).astype(int) 
        return x_solution, result.fun
    else:
        print(f"Optimization failed: {result.message}")
        return None, None


def solve_min_l1_constrained(A, b):
    """
    Solves min ||x||_1 subject to Ax = b using scipy.optimize.linprog.

    Parameters:
    A (np.ndarray): The matrix A in the equality constraint.
    b (np.ndarray): The vector b in the equality constraint.

    Returns:
    np.ndarray: The optimal vector x.
    """
    m, n = A.shape

    #objective
    c = np.ones( n)

    # Bounds for variables: z+ >= 0 and z- >= 0
    bounds = (0, None) 

    # Solve the linear programming problem
    #result = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs',integrality=1) 
    result = linprog(c, A_eq=A, b_eq=b, bounds=bounds, method='highs',integrality=1) 

    if result.success:
        # Extract the solution x from z+ and z-
        z_plus = result.x[:n]
        z_minus = result.x[n:]
        #x = z_plus - z_minus
        x = result.x
        return x, result.fun
    else:
        raise RuntimeError(f"Optimization failed: {result.message}")


vals = []
cnt = 0
cnt2=0
cnt3=0

for line in fp.readlines():
    #print(line,len(line))
    vals = line.split()
    lights = vals[0][1:-1]
    light = sum([1<<k if v == '#' else 0 for k,v in enumerate(lights)]) 
    joltage = np.array([int(v) for v in vals[-1][1:-1].split(',')])
    N = len(joltage)
    buttons = []
    for v in vals[1:-1]:
        buttons.append(np.zeros(N))
        for w in v[1:-1].split(','):
            buttons[-1][int(w)] = 1                         
    #print(len(buttons))
    mymat = np.array(buttons)
    A = np.transpose(mymat)
    #print(A.shape)
    b = joltage
    x_opt, l1_norm = solve_min_l1_constrained(A, b)
    x_int, l1i_norm = solve_min_l1_integer(A, b)
    res = np.sum(A @ x_opt- b)
    print("ZZZZZZZZZZ",res)
    if np.abs(res) > 1e-18:
        pass
    print("XXX  xopt ",x_opt,l1_norm)
    #print("XXXL1",x_int,l1i_norm)
    cnt+= sum(x_int)
    cnt2+= l1_norm
    cnt3+=1
    #pprint.pprint(A) 
    
    #print("lights",lights)
    #print("light",light)
    #print("joltage",N,joltage)
    #print("buttons",buttons)
    
print("FINAL",cnt)    
print("FINAL other",cnt3,cnt2)    
