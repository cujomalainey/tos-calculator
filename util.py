class roleFactory():
    roleLimit = 15
    containerLimit = 15
    warnings = [0 for x in range(0, 15)]

    def __init__(self):
        self.roles = {"escort": escort}
        self.containers = {}
        self.containers.update(self.roles)

    def makeRole(self, role, confirmed, player):
        if self.roleLimit <= 0:
            return
        else:
            self.roleLimit -= 1
        try:
            return self.roles[role](confirmed, False, self, player)
        except Exception:
            print("Cannot make role: {}".format(role))

    def makeContainer(self, role):
        try:
            return self.roles[role](None, True, self, 0)
        except Exception:
            print("Cannot make container: {}".format(role))

    def getWarnings(self):
        return self.warnings

    def setWarning(self, player, level):
        if self.warnings[player] < level:
            self.warnings[player] = level


class role():
    """
    docstring for role
    """
    def __init__(self, confirmed, container, factory, player):
        self.confirmed = confirmed
        self.container = container
        self.factory = factory
        self.player = player

    def collision(self, level):
        if not self.confirmed and self.player is not None:
            self.factory.setWarning(self.player, level)


class anyrole(role):
    """
    """
    pass


class randomtown(role):
    """
    """
    pass


class townsupport(role):
    """
    """
    pass


class escort(role):
    """
    escort
    """
    canbe = [townsupport, randomtown, anyrole]
    unique = False


class transporter(role):
    """
    "transporter":{canbe:["transporter", "townsupport", "randomtown", "any"], unique:false},
    """
    unique = False


class mayor(role):
    """
    "mayor":{canbe:["mayor", "townsupport", "randomtown", "any"], unique:true},
    """
    unique = True


class medium(role):
    """
    "medium":{canbe:["medium", "townsupport", "randomtown", "any"], unique:false},
    """
    unique = False


class retributionist(role):
    """
    "retributionist":{canbe:["retributionist", "townsupport", "randomtown", "any"], unique:true},
    """
    unique = True


class investigator(role):
    """
    "investigator":{canbe:["investigator", "towninvestigative", "randomtown", "any"], unique:false},
    """
    unique = False


class spy(role):
    """
    "spy":{canbe:["spy", "towninvestigative", "randomtown", "any"], unique:false},
    """
    unique = False


class lookout(role):
    """
    "lookout":{canbe:["lookout", "towninvestigative", "randomtown", "any"], unique:false},
    """
    unique = False


class sheriff(role):
    """
    "sheriff":{canbe:["sheriff", "towninvestigative", "randomtown", "any"], unique:false},
    """
    unique = False


class bodyguard(role):
    """
    "bodyguard":{canbe:["bodyguard", "townprotective", "randomtown", "any"], unique:false},
    """
    unique = False


class doctor(role):
    """
    "doctor":{canbe:["doctor", "townprotective", "randomtown", "any"], unique:false},
    """
    unique = False


class jailor(role):
    """
    "jailor":{canbe:["jailor", "townprotective", "randomtown", "any"], unique:true},
    """
    unique = True


class veteran(role):
    """
    "veteran":{canbe:["veteran", "townkilling", "randomtown", "any"], unique:false},
    """
    unique = False


class vigilante(role):
    """
    "vigilante":{canbe:["vigilante", "townkilling", "randomtown", "any"], unique:false},
    """
    unique = False
    # "framer":{canbe:["framer", "mafiadeception", "randommafia", "any"], unique:false},
    # "disguiser":{canbe:["disguiser", "mafiadeception", "randommafia", "any"], unique:false},
    # "janitor":{canbe:["janitor", "mafiadeception", "randommafia", "any"], unique:false},
    # "forger":{canbe:["forger", "mafiadeception", "randommafia", "any"], unique:false},
    # "blackmailer":{canbe:["blackmailer", "mafiasupport", "randommafia", "any"], unique:false},
    # "consigliere":{canbe:["consigliere", "mafiasupport", "randommafia", "any"], unique:false},
    # "consort":{canbe:["consort", "mafiasupport", "randommafia", "any"],  unique:false},
    # "godfather":{canbe:["godfather", "mafiakilling", "randommafia", "any"], unique:true},
    # "mafioso":{canbe:["mafioso", "mafiakilling", "randommafia", "any"], unique:true},
    # "arsonist":{canbe:["arsonist", "neutralkilling", "randomneutral", "any"], unique:false},
    # "serialKiller":{canbe:["serialKiller", "neutralkilling", "randomneutral", "any"], unique:false},
    # "werewolf":{canbe:["werewolf", "neutralkilling", "randomneutral", "any"], unique:true},
    # "executioner":{canbe:["executioner", "neutralevil", "randomneutral", "any"], unique:false},
    # "jester":{canbe:["jester", "neutralevil", "randomneutral", "any"], unique:false},
    # "witch":{canbe:["witch", "neutralevil", "randomneutral", "any"], unique:false},
    # "amnesiac":{canbe:["amnesiac", "neutralbenign", "randomneutral", "any"], unique:false},
    # "survivor":{canbe:["survivor", "neutralbenign", "randomneutral", "any"], unique:false}