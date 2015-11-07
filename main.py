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

    def __init__(self, gameType):
        self.factory = roleFactory()
        self.containers = [
            self.factory.makeContainer(role) for role in self.modes[gameType]]

    def run(self):
        pass

if __name__ == '__main__':
    c = calculator("ranked")
