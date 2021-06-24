import json
from flask import Blueprint, request

clear = Blueprint('clear', __name__)

class Clear:
   def __init__ (self):
      self.functions = [show_clear]
      self.text = "<p>Dogemath is a easy to use mathematical engine</p><p>Made by Luis Vinicius Costa Silva</p><p>Meet me at Twitter/GitHub: @LuisVCSilva</p>"
   @staticmethod
   def show_clear(func):
      return self.text 

   clear_method = {'function_name':show_clear,'keywords':['clear']}
      
@clear.route('/apps/clear',methods=["GET"])
def run():
   return json.dumps({"text":"clear page"})
   
   
