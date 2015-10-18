var calculator = {};

var calculator.roles = {
    "escort":["escort", "townSupport", "randomTown", "any"],
    "transporter":["transporter", "townSupport", "randomTown", "any"],
    "mayor":["mayor", "townSupport", "randomTown", "any"],
    "medium":["medium", "townSupport", "randomTown", "any"],
    "retributionist":["retributionist", "townSupport", "randomTown", "any"],
    "investigator":["investigator", "townInvestigative", "randomTown", "any"],
    "spy":["spy", "townInvestigative", "randomTown", "any"],
    "lookout":["lookout", "townInvestigative", "randomTown", "any"],
    "sheriff":["sheriff", "townInvestigative", "randomTown", "any"],
    "bodyguard":["bodyguard", "townProtective", "randomTown", "any"],
    "doctor":["doctor", "townProtective", "randomTown", "any"],
    "jailor":["jailor", "townProtective", "randomTown", "any"],
    "veteran":["veteran", "townKilling", "randomTown", "any"],
    "vigilante":["vigilante", "townKilling", "randomTown", "any"],
    "framer":["framer", "mafiaDeception", "randomMafia", "any"],
    "disguiser":["disguiser", "mafiaDeception", "randomMafia", "any"],
    "janitor":["janitor", "mafiaDeception", "randomMafia", "any"],
    "forger":["forger", "mafiaDeception", "randomMafia", "any"],
    "blackmailer":["blackmailer", "mafiaSupport", "randomMafia", "any"],
    "consigliere":["consigliere", "mafiaSupport", "randomMafia", "any"],
    "consort":["consort", "mafiaSupport", "randomMafia", "any"],
    "godfather":["godfather", "mafiaKilling", "randomMafia", "any"],
    "mafioso":["mafioso", "mafiaKilling", "randomMafia", "any"],
    "arsonist":["arsonist", "neutralKilling", "randomNeutral", "any"],
    "serialKiller":["serialKiller", "neutralKilling", "randomNeutral", "any"],
    "werewolf":["werewolf", "neutralKilling", "randomNeutral", "any"],
    "executioner":["executioner", "neutralEvil", "randomNeutral", "any"],
    "jester":["jester", "neutralEvil", "randomNeutral", "any"],
    "witch":["witch", "neutralEvil", "randomNeutral", "any"],
    "amnesiac":["amnesiac", "neutralBenign", "randomNeutral", "any"],
    "survivor":["survivor", "neutralBenign", "randomNeutral", "any"]

};

var calculator.roleClasses = {
    "townKilling":["vigilante", "veteran", "jailor"],
    "townProtective":["doctor", "bodyguard"],
    "townSupport":["escort", "transporter", "mayor", "medium", "retributionist"],
    "townInvestigative":["sheriff", "investigator", "lookout", "spy"],
    "mafiaDeception":["framer", "forger", "disguiser", "janitor"],
    "mafiaSupport":["blackmailer", "consigliere", "consort"],
    "mafiaKilling":["godfather", "mafioso"],
    "neutralKilling":["werewolf", "arsonist", "serialKiller"],
    "neutralBenign":["amnesiac", "survivor"],
    "neutralEvil":["executioner", "jester", 'witch']
};