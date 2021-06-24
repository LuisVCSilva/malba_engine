import json
from flask import Blueprint,request

login = Blueprint('login', __name__)

class Login:
   def __init__ (self):
      self.functions = [show_login]
      self.text = "<p>Dogemath is a easy to use mathematical engine</p><p>Made by Luis Vinicius Costa Silva</p><p>Meet me at Twitter/GitHub: @LuisVCSilva</p>"
   @staticmethod
   def show_login(func):
      return self.text 

   login_method = {'function_name':show_login,'keywords':['login']}

@login.route('/apps/login',methods=["GET"])
def run():
   return json.dumps({"text":"login page"})
   
   
