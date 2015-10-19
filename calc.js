var calculator = {};

calculator.roles = {
    "escort":{canbe:["escort", "townsupport", "randomtown", "any"], unique:false},
    "transporter":{canbe:["transporter", "townsupport", "randomtown", "any"], unique:false},
    "mayor":{canbe:["mayor", "townsupport", "randomtown", "any"], unique:true},
    "medium":{canbe:["medium", "townsupport", "randomtown", "any"], unique:false},
    "retributionist":{canbe:["retributionist", "townsupport", "randomtown", "any"], unique:true},
    "investigator":{canbe:["investigator", "towninvestigative", "randomtown", "any"], unique:false},
    "spy":{canbe:["spy", "towninvestigative", "randomtown", "any"], unique:false},
    "lookout":{canbe:["lookout", "towninvestigative", "randomtown", "any"], unique:false},
    "sheriff":{canbe:["sheriff", "towninvestigative", "randomtown", "any"], unique:false},
    "bodyguard":{canbe:["bodyguard", "townprotective", "randomtown", "any"], unique:false},
    "doctor":{canbe:["doctor", "townprotective", "randomtown", "any"], unique:false},
    "jailor":{canbe:["jailor", "townprotective", "randomtown", "any"], unique:true},
    "veteran":{canbe:["veteran", "townkilling", "randomtown", "any"], unique:false},
    "vigilante":{canbe:["vigilante", "townkilling", "randomtown", "any"], unique:false},
    "framer":{canbe:["framer", "mafiadeception", "randommafia", "any"], unique:false},
    "disguiser":{canbe:["disguiser", "mafiadeception", "randommafia", "any"], unique:false},
    "janitor":{canbe:["janitor", "mafiadeception", "randommafia", "any"], unique:false},
    "forger":{canbe:["forger", "mafiadeception", "randommafia", "any"], unique:false},
    "blackmailer":{canbe:["blackmailer", "mafiasupport", "randommafia", "any"], unique:false},
    "consigliere":{canbe:["consigliere", "mafiasupport", "randommafia", "any"], unique:false},
    "consort":{canbe:["consort", "mafiasupport", "randommafia", "any"],  unique:false},
    "godfather":{canbe:["godfather", "mafiakilling", "randommafia", "any"], unique:true},
    "mafioso":{canbe:["mafioso", "mafiakilling", "randommafia", "any"], unique:true},
    "arsonist":{canbe:["arsonist", "neutralkilling", "randomneutral", "any"], unique:false},
    "serialKiller":{canbe:["serialKiller", "neutralkilling", "randomneutral", "any"], unique:false},
    "werewolf":{canbe:["werewolf", "neutralkilling", "randomneutral", "any"], unique:true},
    "executioner":{canbe:["executioner", "neutralevil", "randomneutral", "any"], unique:false},
    "jester":{canbe:["jester", "neutralevil", "randomneutral", "any"], unique:false},
    "witch":{canbe:["witch", "neutralevil", "randomneutral", "any"], unique:false},
    "amnesiac":{canbe:["amnesiac", "neutralbenign", "randomneutral", "any"], unique:false},
    "survivor":{canbe:["survivor", "neutralbenign", "randomneutral", "any"], unique:false}

};

calculator.roleClasses = {
    "townKilling":["vigilante", "veteran", "jailor"],
    "townProtective":["doctor", "bodyguard"],
    "townSupport":["escort", "transporter", "mayor", "medium", "retributionist"],
    "townInvestigative":["sheriff", "investigator", "lookout", "spy"],
    "mafiaDeception":["framer", "forger", "disguiser", "janitor"],
    "mafiaSupport":["blackmailer", "consigliere", "consort"],
    "mafiaKilling":["godfather", "mafioso"],
    "neutralKilling":["werewolf", "arsonist", "serialkiller"],
    "neutralBenign":["amnesiac", "survivor"],
    "neutralEvil":["executioner", "jester", 'witch']
};

calculator.gameModes = {
	"classic":["sheriff", "doctor", "investigator", "jailor", "medium", "godfather",
	"framer", "executioner", "escort", "mafioso", "lookout", "serialkiller",
	"townkilling", "jester", "randomtown"],
	"ranked":["jailor", "towninvestigative", "towninvestigative", "townsupport",
	"townsupport", "townprotective", "townkilling", "randomtown", "godfather",
	"mafioso", "randommafia", "neutralkilling", "neutralevil", "neutralbenign",
	"any"],
	"custom":[]
};


calculator.setup = function() {
    l = [];
    for (i = 1; i < 16; i++) {
        l.push($("#" + i));
    }
    calculator.people = l;
}

calculator.run = function() {
    // remove all warnings
    this.clearWarnings();
    // reset the pool
// remove all verified rules from pool
// count claims against pool
// look for roles that extend into RT, and any
// highlight roles based on dnager
};

calculator.clearWarnings = function(){

};