var calculator = {};

calculator.roles = {
    "escort":{canbe:["escort", "townSupport", "randomTown", "any"], unique:false},
    "transporter":{canbe:["transporter", "townSupport", "randomTown", "any"], unique:false},
    "mayor":{canbe:["mayor", "townSupport", "randomTown", "any"], unique:true},
    "medium":{canbe:["medium", "townSupport", "randomTown", "any"], unique:false},
    "retributionist":{canbe:["retributionist", "townSupport", "randomTown", "any"], unique:true},
    "investigator":{canbe:["investigator", "townInvestigative", "randomTown", "any"], unique:false},
    "spy":{canbe:["spy", "townInvestigative", "randomTown", "any"], unique:false},
    "lookout":{canbe:["lookout", "townInvestigative", "randomTown", "any"], unique:false},
    "sheriff":{canbe:["sheriff", "townInvestigative", "randomTown", "any"], unique:false},
    "bodyguard":{canbe:["bodyguard", "townProtective", "randomTown", "any"], unique:false},
    "doctor":{canbe:["doctor", "townProtective", "randomTown", "any"], unique:false},
    "jailor":{canbe:["jailor", "townProtective", "randomTown", "any"], unique:true},
    "veteran":{canbe:["veteran", "townKilling", "randomTown", "any"], unique:false},
    "vigilante":{canbe:["vigilante", "townKilling", "randomTown", "any"], unique:false},
    "framer":{canbe:["framer", "mafiaDeception", "randomMafia", "any"], unique:false},
    "disguiser":{canbe:["disguiser", "mafiaDeception", "randomMafia", "any"], unique:false},
    "janitor":{canbe:["janitor", "mafiaDeception", "randomMafia", "any"], unique:false},
    "forger":{canbe:["forger", "mafiaDeception", "randomMafia", "any"], unique:false},
    "blackmailer":{canbe:["blackmailer", "mafiaSupport", "randomMafia", "any"], unique:false},
    "consigliere":{canbe:["consigliere", "mafiaSupport", "randomMafia", "any"], unique:false},
    "consort":{canbe:["consort", "mafiaSupport", "randomMafia", "any"],  unique:false},
    "godfather":{canbe:["godfather", "mafiaKilling", "randomMafia", "any"], unique:true},
    "mafioso":{canbe:["mafioso", "mafiaKilling", "randomMafia", "any"], unique:true},
    "arsonist":{canbe:["arsonist", "neutralKilling", "randomNeutral", "any"], unique:false},
    "serialKiller":{canbe:["serialKiller", "neutralKilling", "randomNeutral", "any"], unique:false},
    "werewolf":{canbe:["werewolf", "neutralKilling", "randomNeutral", "any"], unique:true},
    "executioner":{canbe:["executioner", "neutralEvil", "randomNeutral", "any"], unique:false},
    "jester":{canbe:["jester", "neutralEvil", "randomNeutral", "any"], unique:false},
    "witch":{canbe:["witch", "neutralEvil", "randomNeutral", "any"], unique:false},
    "amnesiac":{canbe:["amnesiac", "neutralBenign", "randomNeutral", "any"], unique:false},
    "survivor":{canbe:["survivor", "neutralBenign", "randomNeutral", "any"], unique:false}

};

calculator.roleClasses = {
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

calculator.gameModes = {
	"classic":["sheriff", "doctor", "investigator", "jailor", "medium", "godfather",
	"framer", "executioner", "escort", "mafioso", "lookout", "serialKiller",
	"townKilling", "jester", "randomTown"],
	"ranked":["jailor", "townInvestigative", "townInvestigative", "townSupport",
	"townSupport", "townProtective", "townKilling", "randomTown", "godfather",
	"mafioso", "randomMafia", "neutralKilling", "neutralEvil", "neutralBenign",
	"any"],
	"custom":[]
};

calculator.setup = function() {
    
}

calculator.run = function() {

};

$(function() {
    $( ".claims" ).autocomplete({
      source: Object.keys(calculator.roles)
    });
  });