class roleFactory():
    roleLimit = 15
    containerLimit = 15
    warnings = [0 for x in range(0, 15)]

    def __init__(self):
        self.roles = {"escort": escort}
        containers = {}
        self.containers = dict(self.roles, **containers)

    def makeRole(self, role, confirmed, player):
        if self.roleLimit <= 0:
            return
        else:
            self.roleLimit -= 1
        try:
            return self.roles[role](confirmed, False, self, player)
        except Exception:
            return

    def makeContainer(self, role):
        try:
            return self.roles[role](None, True, self, 0)
        except Exception:
            pass

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
        if not self.confirmed:
            self.factory.setWarning(self.player, level)


class escort(role):
    """
    "escort":{canbe:["escort", "townsupport", "randomtown", "any"], unique:false}
    """
    self.unique = False


class transporter(role):
    """
    "transporter":{canbe:["transporter", "townsupport", "randomtown", "any"], unique:false},
    """
    self.unique = False


class mayor(role):
    """
    "mayor":{canbe:["mayor", "townsupport", "randomtown", "any"], unique:true},
    """
    self.unique = True


class medium(role):
    """
    "medium":{canbe:["medium", "townsupport", "randomtown", "any"], unique:false},
    """
    self.unique = False


class retributionist(role):
    """
    "retributionist":{canbe:["retributionist", "townsupport", "randomtown", "any"], unique:true},
    """
    self.unique = True


class investigator(role):
    """
    "investigator":{canbe:["investigator", "towninvestigative", "randomtown", "any"], unique:false},
    """
    self.unique = False


class spy(role):
    """
    "spy":{canbe:["spy", "towninvestigative", "randomtown", "any"], unique:false},
    """
    self.unique = False


class lookout(role):
    """
    "lookout":{canbe:["lookout", "towninvestigative", "randomtown", "any"], unique:false},
    """
    self.unique = False


class sheriff(role):
    """
    "sheriff":{canbe:["sheriff", "towninvestigative", "randomtown", "any"], unique:false},
    """
    self.unique = False


class bodyguard(role):
    """
    "bodyguard":{canbe:["bodyguard", "townprotective", "randomtown", "any"], unique:false},
    """
    self.unique = False


class doctor(role):
    """
    "doctor":{canbe:["doctor", "townprotective", "randomtown", "any"], unique:false},
    """
    self.unique = False


class jailor(role):
    """
    "jailor":{canbe:["jailor", "townprotective", "randomtown", "any"], unique:true},
    """
    self.unique = True


class veteran(role):
    """
    "veteran":{canbe:["veteran", "townkilling", "randomtown", "any"], unique:false},
    """
    self.unique = False


class vigilante(role):
    """
    "vigilante":{canbe:["vigilante", "townkilling", "randomtown", "any"], unique:false},
    """
    self.unique = False
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