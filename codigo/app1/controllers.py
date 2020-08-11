
from flask.views import MethodView
from flask import render_template


class RegisterControllers(MethodView):
    """
        Register
    """
    def post(self):
        return render_template('register.html')


    def get(self):
        return 'Esta es la vista registro por metodo GET'


class LoginControllers(MethodView):
    """
        Login
    """
    def post(self):
        return 'Esta es la vista login'


class PhoneControllers(MethodView):
    """
        Linea Nueva
    """
    def post(self):
        return 'esta es la vista del POST'
    def get(self):
        return 'esta es la vista del GET'
    def put(self):
        return 'esta es la vista del PUT'
    def delete(self):
        return 'esta es la vista del DELETE'
