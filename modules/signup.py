import json
from flask import Blueprint,request

signup = Blueprint('signup', __name__)

class Signup:
   def __init__ (self):
      self.functions = [show_signup]
      self.text = ""
      
   @staticmethod
   def show_signup(func):
      return self.text 

   signup_method = {'function_name':show_signup,'keywords':['signup']}
      
@signup.route('/apps/signup',methods=["GET"])
def run():
   return json.dumps({"text":"signup page"})
   
   
