'use strict'
var readline = require('readline');

var rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});

rl.question("Podaj nazwisko, które chcesz przetworzyć\n", function(surname) {
	surname = surname.toLowerCase();
	surname = surname.charAt(0).toUpperCase() + surname.substr(1);
	Module.generateVariantsPerCases(surname);
	
});

process.on('uncaughtException', function(err) {
	console.log("Podane nazwisko nie posiada odpowiedniej klasy")
	process.exit()
});

var cases = [
	'Mianownik  (Kto, co?)		→',
	'Dopełniacz (Kogo, czego?)	→',
	'Celownik (Komu, czemu?)		→',
	'Biernik (Kogo, co?)		→',
	'Narzędnik (Z kim?, Z czym?)	→',
	'Miejscownik (O kim?, O czym?)	→',
	'Wołacz (Hej!) 			→'
];
var classes = {
	0: ["ski", "cki", "dzki"],
	1: ["ak", "ik", "yk"],
	2: ["ek"],
	3: ["ny"],
	4: ["ka"],
	5: ["owicz", "ewicz", "ach", "ól", "arz"],
	6: ["ur"],
	7: ["el"],
	8: ["ra"],
	9: ["an", "ąb"],
	10: ["oł", "eł", "ieł"],
	11: ["ia"],
	12: ["ień"],
	13: ["leń"]
};
var ends = {
	0: {
		0: ['ki', 'ka', 'cy', 'kie'],
		1: ['kiego', 'kiej', 'kich', 'kich'],
		2: ['kiemu', 'kiej', 'kim', 'kim'],
		3: ['kiego', 'ką', 'kich', 'kich'],
		4: ['kim', 'ką', 'kimi', 'kimi'],
		5: ['kim', 'kiej', 'kich', 'kich'],
		6: ['ki', 'ka', 'cy', 'kie']
	},
	1: {
		0: ['', '', 'owie'],
		1: ['a', '', 'ów'],
		2: ['owi', '', 'om'],
		3: ['a', '', 'ów'],
		4: ['iem', '', 'ami'],
		5: ['u', '', 'ach'],
		6: ['u', '', 'owie']
	},
	2: {
		0: ['ek', 'ek', 'kowie'],
		1: ['ka', 'ek', 'ków'],
		2: ['kowi', 'ek', 'kom'],
		3: ['ka', 'ek', 'ków'],
		4: ['kiem', 'ek', 'kami'],
		5: ['ku', 'ek', 'kach'],
		6: ['ku', 'ek', 'kowie']
	},
	3: {
		0: ['y', 'a', 'i'],
		1: ['ego', 'ej', 'ych'],
		2: ['emu', 'ej', 'ym'],
		3: ['ego', 'ą', 'ych'],
		4: ['ym', 'ą', 'ymi'],
		5: ['ym', 'ej', 'ych'],
		6: ['y', 'a', 'i']
	},
	4: {
		0: ['ka', 'ka', 'kowie'],
		1: ['ki', 'ki', 'ków'],
		2: ['ce', 'ce', 'kom'],
		3: ['kę', 'kę', 'ków'],
		4: ['ką', 'ką', 'kami'],
		5: ['ce', 'ce', 'kach'],
		6: ['ka', 'ka', 'kowie']
	},
	5: {
		0: ['', '', 'owie'],
		1: ['a', '', 'ów'],
		2: ['owi', '', 'om'],
		3: ['a', '', 'ów'],
		4: ['em', '', 'ami'],
		5: ['u', '', 'ach'],
		6: ['u', '', 'owie']
	},
	6: {
		0: ['', '', 'owie'],
		1: ['a', '', 'ów'],
		2: ['owi', '', 'om'],
		3: ['a', '', 'ów'],
		4: ['em', '', 'ami'],
		5: ['ze', '', 'ach'],
		6: ['ze', '', 'owie']
	},
	7: {
		0: ['el', 'el', 'lowie'],
		1: ['la', 'el', 'lów'],
		2: ['owi', 'el', 'lom'],
		3: ['a', 'el', 'lów'],
		4: ['em', 'el', 'lami'],
		5: ['lu', 'el', 'lach'],
		6: ['lu', 'el', 'lowie']
	},
	8: {
		0: ['a', 'a', 'owie'],
		1: ['y', 'y', 'ów'],
		2: ['ze', 'ze', 'om'],
		3: ['ę', 'ę', 'ów'],
		4: ['ą', 'ą', 'ami'],
		5: ['ze', 'ze', 'ach'],
		6: ['o', 'o', 'owie']
	},
	9: {
		0: ['', '', 'owie'],
		1: ['a', '', 'ów'],
		2: ['owi', '', 'om'],
		3: ['a', '', 'ów'],
		4: ['em', '', 'ami'],
		5: ['ie', '', 'ach'],
		6: ['ie', '', 'owie']
	},
	10: {
		0: ['ł', 'ł', 'łowie'],
		1: ['ła', 'ł', 'łów'],
		2: ['łowi', 'ł', 'łom'],
		3: ['ła', 'ł', 'łów'],
		4: ['łem', 'ł', 'łami'],
		5: ['le', 'ł', 'łach'],
		6: ['le', 'ł', 'łowie']
	},
	11: {
		0: ['a', 'a', 'owie'],
		1: ['', '', 'ów'],
		2: ['', '', 'om'],
		3: ['ę', 'ę', 'ów'],
		4: ['ą', 'ą', 'ami'],
		5: ['', '', 'ach'],
		6: ['o', 'o', 'owie']
	},
	12: {
		0: ['ień', 'ień', 'niowie'],
		1: ['nia', 'ień', 'niów'],
		2: ['niowi', 'ień', 'niom'],
		3: ['nia', 'ień', 'niów'],
		4: ['niem', 'ień', 'niami'],
		5: ['niu', 'ień', 'niach'],
		6: ['niu', 'ień', 'niowie']
	},
	13: {
		0: ['ń', 'ń', 'niowie'],
		1: ['nia', 'ń', 'niów'],
		2: ['niowi', 'ń', 'niom'],
		3: ['nia', 'ń', 'niów'],
		4: ['niem', 'ń', 'niami'],
		5: ['niu', 'ń', 'niach'],
		6: ['niu', 'ń', 'niowie']
	}
};

var Module = new function() {
	this.cases = cases;
	this.ends = ends;
	this.classes = classes;
	this.checkSurname = function(last_characters, surname) {
		var pattern = new RegExp(last_characters + "$");
		return surname.match(pattern);
	}
	this.classifySurname = function(surname) {
		var self = this;
		for (var number in self.classes) {
			if (classes.hasOwnProperty(number)) {
				var table_of_ends = self.classes[number]; //from current class

				for (var i = 0; i < table_of_ends.length; i++) {
					var test = self.checkSurname(table_of_ends[i], surname);
					if (test !== null) {
						return {
							match: test,
							class_number: number
						}
					}
				}
			}
		}
	}
	this.generateVariantsPerCases = function(surname_from_user) {
		var record = this.classifySurname(surname_from_user);
		var surname_class = ends[record.class_number]
		console.log('class →', record);

		if (record.class_number !== undefined) {
			var surname = record.match.input;
			for (var prop in surname_class) {
				var current_case = surname_class[prop];

				var cutted_surname;
				if (prop === "0" && current_case[0] !== "") {
					var index_of_end = surname.lastIndexOf(current_case[0]);
					cutted_surname = surname.substring(0, index_of_end);
				}
				if (cutted_surname === undefined) cutted_surname = surname;

				var answer = "	"
				for (var i = 0; i < current_case.length; i++) {
					answer += cutted_surname + current_case[i] + " ";
				}
				if (answer !== undefined) console.log(cases[prop] + answer);

			}
		}
	}
};
