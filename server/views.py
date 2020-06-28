from tornado.web import RequestHandler

from database.engine import session
from database.models import ScenarioDB, FlightPlanDB



class HomeView(RequestHandler):
    """Handle get request for the SIM homepage"""
    def get(self):
        self.render("index.html")



class ScenarioDBView(RequestHandler):
    """Handle retrieve, create, modify Scenarios in the DB"""
    def get(self):
        pass

    def post(self):
        pass

    def put(self):
        pass



class FlighPlanDBView(RequestHandler):
    """Handle retrieve, create, modify Flightplans in the DB"""
    def get(self):
        pass

    def post(self):
        pass

    def put(self):
        pass