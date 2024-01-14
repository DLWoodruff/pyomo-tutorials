# knapsack_Param.py 
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
opt_success = opt.solve(model)
print(f"{model.obj =}, {pyo.value(model.obj) =}")

model.pprint()

