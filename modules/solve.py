import json
from flask import Blueprint,request

from sympy import latex
from sympy.abc import *

from sympy.solvers import solve as equation_solver

solve = Blueprint('solve', __name__)

class Solve:
   def __init__ (self):
      self.functions = [show_solve]
      self.text = ""
      
   @staticmethod
   def show_solve(eq):
      return latex(equation_solver(eq))

   solve_method = {'function_name':show_solve,'keywords':['solve']}

@solve.route('/apps/solve',methods=["GET"])
def run():
   print(request.args["input"])
   return json.dumps({"result":"$$"+Solve.show_solve(request.args["input"])+"$$"})
