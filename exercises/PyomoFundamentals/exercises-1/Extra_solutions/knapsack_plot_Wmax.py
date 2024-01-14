# knapsack_plot_Wmax.py created from knapsack_Param.py 
import matplotlib.pyplot as plt
import pyomo.environ as pyo

A = ['hammer', 'wrench', 'screwdriver', 'towel']
b = {'hammer':8, 'wrench':3, 'screwdriver':6, 'towel':11}
w = {'hammer':5, 'wrench':7, 'screwdriver':4, 'towel':3}

model = pyo.ConcreteModel()

model.W_max = pyo.Param(initialize=14, mutable=True)
model.x = pyo.Var( A, within=pyo.Binary )

model.obj = pyo.Objective(
    expr = sum( b[i]*model.x[i] for i in A ), 
    sense = pyo.maximize )

model.weight_con = pyo.Constraint(
    expr = sum( w[i]*model.x[i] for i in A ) <= model.W_max )

opt = pyo.SolverFactory('glpk')

wmaxes = list()
objs = list()
for wmax in range(-2,20):
    model.W_max = wmax
    results = opt.solve(model)
    if not pyo.check_optimal_termination(results):
        print(f"No optimal solution for W_max={pyo.value(model.W_max)}")
        continue
    print(f"{wmax =}, {pyo.value(model.obj) =}")
    wmaxes.append(wmax)
    objs.append(pyo.value(model.obj))
plt.plot(wmaxes, objs)
plt.xlabel("W_max")
plt.ylabel("Total Value")

print(f"{pyo.value(model.weight_con) =}")  # not surprising

##pyo.assert_optimal_termination(results) 
##model.pprint()

