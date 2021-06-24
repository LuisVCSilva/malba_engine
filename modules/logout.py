import json
from flask import Blueprint,request

logout = Blueprint('logout', __name__)

class Logout:
   def __init__ (self):
      self.functions = [show_logout]
      self.text = ""
      
   @staticmethod
   def show_logout(func):
      return self.text 

   logout_method = {'function_name':show_logout,'keywords':['logout']}

@logout.route('/apps/logout',methods=["GET"])
def run():
   return json.dumps({"text":"logout page"})
   
   
