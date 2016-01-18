from util import roleFactory
from flask import Flask
from flask import Response
import json


app = Flask(__name__)


class calculator():
    """
    the brains
    """
    modes = {
        "classic": [
            "sheriff", "doctor", "investigator", "jailor", "medium",
            "godfather", "framer", "executioner", "escort", "mafioso",
            "lookout", "serialkiller", "townkilling", "jester", "randomtown"],
        "ranked": [
            "jailor", "towninvestigative", "towninvestigative", "townsupport",
            "townsupport", "townprotective", "townkilling", "randomtown",
            "godfather", "mafioso", "randommafia", "neutralkilling",
            "neutralevil", "neutralbenign", "anyrole"]
            }

    def __init__(self, gameType, roleList):
        self.factory = roleFactory()
        self.containers = [
            self.factory.makeContainer(role) for role in self.modes[gameType]]
        self.roles = []
        i = 0
        for r in roleList:
            self.roles.append(self.factory.makeRole(
                r["role"], r["confirmed"], i))
            i += 1

    def run(self):
        for r in self.roles:
            r.place(self.containers)
        return self.factory.getWarnings()


@app.route("/calc")
def runCalc():
    v = [{"role": "jailor", "confirmed": True},
         {"role": "escort", "confirmed": False},
         {"role": "escort", "confirmed": False},
         {"role": "sheriff", "confirmed": False},
         {"role": "spy", "confirmed": False},
         {"role": "spy", "confirmed": False},
         {"role": "doctor", "confirmed": False},
         {"role": "executioner", "confirmed": False},
         {"role": "godfather", "confirmed": False},
         {"role": "forger", "confirmed": False},
         {"role": "mafioso", "confirmed": False},
         {"role": "serialkiller", "confirmed": False},
         {"role": "survivor", "confirmed": False},
         {"role": "veteran", "confirmed": False},
         {"role": "survivor", "confirmed": False}]
    c = calculator("ranked", v)
    return Response(json.dumps(c.run()), mimetype="application/json")

if __name__ == '__main__':
    app.run()
