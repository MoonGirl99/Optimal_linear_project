import gurobipy as gp
import pyomo.environ as pyo
from pyomo.environ import *
from pyomo.opt import SolverFactory

def Calculation():
    main = int(input("enter 1 if you want maximization or 2 for minimization: "))
    if main == 1:
        model = pyo.ConcreteModel()
        model.idx = pyo.RangeSet(int(input('please enter the numbers of your variables : ')))
        model.x = pyo.Var(model.idx, within=pyo.NonNegativeReals)
        x = model.x
        model.obj = pyo.Objective(expr=eval(input('enter obj. :')), sense=maximize)
        model.c1 = pyo.Constraint(expr=eval(input('enter c1 :')))
        model.c2 = pyo.Constraint(expr=eval(input('enter c2 :')))
        model.c3 = pyo.Constraint(expr=eval(input('enter c3 : ')))

        solver = SolverFactory('gurobi')
        solver.solve(model)
        pyo.display(model)
    else :
        model = pyo.ConcreteModel()
        model.idx = pyo.RangeSet(int(input('please enter the numbers of your variables : ')))
        model.x = pyo.Var(model.idx,within= pyo.NonNegativeReals)
        x = model.x
        model.obj = pyo.Objective(expr=eval(input('enter obj. :')), sense=minimize)
        model.c1 = pyo.Constraint(expr=eval(input('enter c1 :')))
        model.c2 = pyo.Constraint(expr=eval(input('enter c2 :')))
        model.c3 = pyo.Constraint(expr=eval(input('enter c3')))

        solver = SolverFactory('gurobi')
        solver.solve(model)
        pyo.display(model)
