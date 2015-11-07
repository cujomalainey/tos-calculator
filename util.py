class roleFactory():
    roleLimit = 15
    containerLimit = 15
    warnings = [0 for x in range(0, 15)]

    def __init__(self):
        self.roles = {
            "escort": escort, "transporter": transporter, "mayor": mayor,
            "medium": medium, "retributionist": retributionist,
            "investigator": investigator, "spy": spy, "lookout": lookout,
            "sheriff": sheriff, "bodyguard": bodyguard, "doctor": doctor,
            "jailor": jailor, "veteran": veteran, "vigilante": vigilante}
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
        self.obj = None

    def collision(self, level):
        if not self.confirmed and self.player is not None:
            self.factory.setWarning(self.player, level)

    def place(self, containers):
        """
        algorithm to attempt to place objects
        """
        c = canbe + [self.__class__]
        l = 0
        b = False
        m = None
        for can in c:
            for cont in containers:
                if can == cont.__class__:
                    if cont.put(self):
                        b = True
                        m = cont
                        break
            if b:
                break
            l += 1
        if m is None:
            l = 5
        self.factory.setWarning(self.player, l)
        for can in c:
            for cont in containers:
                if can == cont.__class__:
                    if cont == m:
                        b = True
                        break
                    else:
                        cont.obj.collision(l)
            if b:
                break

    def put(self, obj):
        if self.obj is None:
            self.obj = obj
            return True
        return False


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
    transporter
    """
    canbe = [townsupport, randomtown, anyrole]
    unique = False


class mayor(role):
    """
    mayor
    """
    canbe = [townsupport, randomtown, anyrole]
    unique = True


class medium(role):
    """
    medium
    """
    canbe = [townsupport, randomtown, anyrole]
    unique = False


class retributionist(role):
    """
    retributionist
    """
    canbe = [townsupport, randomtown, anyrole]
    unique = True


class investigator(role):
    """
    investigator
    """
    canbe = [towninvestigative, randomtown, anyrole]
    unique = False


class spy(role):
    """
    spy
    """
    canbe = [towninvestigative, randomtown, anyrole]
    unique = False


class lookout(role):
    """
    lookout
    """
    canbe = [towninvestigative, randomtown, anyrole]
    unique = False


class sheriff(role):
    """
    sheriff
    """
    canbe = [towninvestigative, randomtown, anyrole]
    unique = False


class bodyguard(role):
    """
    bodyguard
    """
    canbe = [townprotective, randomtown, anyrole]
    unique = False


class doctor(role):
    """
    doctor
    """
    canbe = [townprotective, randomtown, anyrole]
    unique = False


class jailor(role):
    """
    jailor
    """
    canbe = [townprotective, randomtown, anyrole]
    unique = True


class veteran(role):
    """
    veteran
    """
    canbe = [veteran, townkilling, randomtown, anyrole]
    unique = False


class vigilante(role):
    """
    vigilante
    """
    canbe = [vigilante, townkilling, randomtown, anyrole]
    unique = False


class framer(role):
    """
    framer
    """
    canbe = [mafiadeception, randommafia, anyrole]
    unique = False


class disguiser(role):
    """
    disguiser
    """
    canbe = [mafiadeception, randommafia, anyrole]
    unique = False 


class janitor(role):
    """
    janitor
    """
    canbe = [mafiadeception, randommafia, anyrole]
    unique = False


class forger(role):
    """
    forger
    """
    canbe = [mafiadeception, randommafia, anyrole]
    unique = False


class blackmailer(role):
    """
    blackmailer
    """
    canbe = [mafiasupport, randommafia, anyrole]
    unique = False


class consigiliere(role):
    """
    consigiliere
    """
    canbe = [mafiasupport, randommafia, anyrole]
    unique = False


class consort(role):
    """
    consort
    """
    canbe = [mafiasupport, randommafia, anyrole]
    unique = False


class godfather(role):
    """
    godfather
    """
    canbe = [mafiakilling, randommafia, anyrole]
    unique = True


class mafioso(role):
    """
    mafioso
    """
    canbe = [mafiakilling, randommafia, anyrole]
    unique = True


class arsonist(role):
    """
    arsonist
    """
    canbe = [neutralkilling, randomneutral, anyrole]
    unique = False


class serialkiller(role):
    """
    serialkiller
    """
    canbe = [neutralkilling, randomneutral, anyrole]
    unique = False


class werewolf(role):
    """
    werewolf
    """
    canbe = [neutralkilling, randomneutral, anyrole]
    unique = True


class executioner(role):
    """
    executioner
    """
    canbe = [neutralevil, randomneutral, anyrole]
    unique = False


class jester(role):
    """
    jester
    """
    canbe = [neutralevil, randomneutral, anyrole]
    unique = False


class witch(role):
    """
    witch
    """
    canbe = [neutralevil, randomneutral, anyrole]
    unique = False


class amnesiac(role):
    """
    amnesiac
    """
    canbe = [neutralbenign, randomneutral, anyrole]
    unique = False


class survivor(role):
    """
    survivor
    """
    canbe = [neutralbenign, randomneutral, anyrole]
    unique = False
    # Mafia support, mafia killing, mafia support, neutralbenign , neutralevil, neutralkilling, towninvestigative, townkilling, townprotective
