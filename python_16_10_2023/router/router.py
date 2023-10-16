from flask import Blueprint, request
import controller.controller as Controller
routers = Blueprint('Routers',__name__) 

@routers.route('/process',methods=['GET'])
def processTest():
    return Controller.convert(request)
  