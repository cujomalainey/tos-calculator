from util import roleFactory


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
            "neutralevil", "neutralbenign", "any"]
            }

    def __init__(self, gameType, roleList):
        self.factory = roleFactory()
        self.containers = [
            self.factory.makeContainer(role) for role in self.modes[gameType]]
        self.roles = []
        for r in roleList:
            self.roles.append(self.factory.makeRole(
                r["role"], r["confirmed"], r["player"] - 1))

    def run(self):
        for r in self.roles:
            r.place(self.containers)
        return self.factory.getWarnings()

if __name__ == '__main__':
    v = [{"role": "jailor", "confirmed": True, "player": 1},
         {"role": "escort", "confirmed": False, "player": 2},
         {"role": "escort", "confirmed": False, "player": 3},
         {"role": "sheriff", "confirmed": False, "player": 4},
         {"role": "spy", "confirmed": False, "player": 5},
         {"role": "spy", "confirmed": False, "player": 6},
         {"role": "doctor", "confirmed": False, "player": 7},
         {"role": "executioner", "confirmed": False, "player": 8},
         {"role": "godfather", "confirmed": False, "player": 9},
         {"role": "forger", "confirmed": False, "player": 10},
         {"role": "mafioso", "confirmed": False, "player": 11},
         {"role": "serialkiller", "confirmed": False, "player": 12},
         {"role": "survivor", "confirmed": False, "player": 13},
         {"role": "veteran", "confirmed": False, "player": 14},
         {"role": "survivor", "confirmed": False, "player": 15}]
    c = calculator("ranked", v)
    print(c.run())
