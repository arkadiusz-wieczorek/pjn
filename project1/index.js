var readline = require('readline');

var rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});

rl.question("Podaj nazwisko, które chcesz przetworzyć\n", function(surname) {
	generateVariantsPerCases(surname);
});

var classes = {
	0: ["ki"], // 0: ["ski", "cki", "dzki"],
	1: ["ak", "ik", "yk"],
	2: ["ek"],
	3: ["ny"],
	4: ["ka"],
	5: ["wicz"], // 5: ["owicz", "ewicz"],
	6: ["ur"],
	7: ["el"],
	8: ["ra"],
	9: ["an", "ąb"],
	10: ["oł", "eł", "ieł"],
	11: ["ia"]
}

var ends = {
	0: {
		"mianownik": ['ki', 'cy', 'ka', 'kie'],
		"dopelniacz": ['kiego', 'kich', 'kiej', 'kich'],
		"celownik": ['kiemu', 'kim', 'kiej', 'kim'],
		"biernik": ['kiego', 'kich', 'ką', 'kich'],
		"nadrzednik": ['kim', 'kimi', 'ką', 'kimi'],
		"miejscownik": ['kim', 'kich', 'kiej', 'kich'],
		"wolacz": ['ki', 'cy', 'ka', 'kie']
	},
	1: {
		"mianownik": ['', 'owie', ''],
		"dopelniacz": ['a', 'ów', ''],
		"celownik": ['owi', 'om', ''],
		"biernik": ['a', 'ów', ''],
		"nadrzednik": ['iem', 'ami', ''],
		"miejscownik": ['u', 'ach', ''],
		"wolacz": ['u', 'owie', '']
	},
	2: {
		"mianownik": ['ek', 'kowie', 'ek'],
		"dopelniacz": ['ka', 'ków', 'ek'],
		"celownik": ['owi', 'kom', 'ek'],
		"biernik": ['ka', 'ków', 'ek'],
		"nadrzednik": ['kiem', 'kami', 'ek'],
		"miejscownik": ['ku', 'kach', 'ek'],
		"wolacz": ['ku', 'kowie', 'ek']
	},
	3: {
		"mianownik": ['y', 'i', 'a'],
		"dopelniacz": ['ego', 'ych', 'ej'],
		"celownik": ['emu', 'ym', 'ej'],
		"biernik": ['ego', 'ych', 'ą'],
		"nadrzednik": ['ym', 'ymi', 'ą'],
		"miejscownik": ['ym', 'ych', 'ej'],
		"wolacz": ['y', 'i', 'a']
	},
	4: {
		"mianownik": ['ka', 'kowie', 'ka'],
		"dopelniacz": ['ki', 'ków', 'ki'],
		"celownik": ['ce', 'kom', 'ce'],
		"biernik": ['kę', 'ków', 'kę'],
		"nadrzednik": ['ką', 'kami', 'ką'],
		"miejscownik": ['ce', 'kach', 'ce'],
		"wolacz": ['ka', 'kowie', 'ka']
	},
	5: {
		"mianownik": ['', 'owie', ''],
		"dopelniacz": ['a', 'ów', ''],
		"celownik": ['owi', 'om', ''],
		"biernik": ['a', 'ów', ''],
		"nadrzednik": ['em', 'ami', ''],
		"miejscownik": ['u', 'ach', ''],
		"wolacz": ['u', 'owie', '']
	},
	6: {
		"mianownik": ['', 'owie', ''],
		"dopelniacz": ['a', 'ów', ''],
		"celownik": ['owi', 'om', ''],
		"biernik": ['a', 'ów', ''],
		"nadrzednik": ['em', 'ami', ''],
		"miejscownik": ['ze', 'ach', ''],
		"wolacz": ['ze', 'owie', '']
	},
	7: {
		"mianownik": ['el', 'lowie', 'el'],
		"dopelniacz": ['la', 'lów', 'el'],
		"celownik": ['owi', 'lom', 'el'],
		"biernik": ['a', 'lów', 'el'],
		"nadrzednik": ['em', 'lami', 'el'],
		"miejscownik": ['lu', 'lach', 'el'],
		"wolacz": ['lu', 'lowie', 'el']
	},
	8: {
		"mianownik": ['a', 'owie', 'a'],
		"dopelniacz": ['y', 'ów', 'y'],
		"celownik": ['ze', 'om', 'ze'],
		"biernik": ['ę', 'ów', 'ę'],
		"nadrzednik": ['ą', 'ami', 'ą'],
		"miejscownik": ['ze', 'ach', 'ze'],
		"wolacz": ['o', 'owie', 'o']
	},
	9: {
		"mianownik": ['', 'owie', ''],
		"dopelniacz": ['a', 'ów', ''],
		"celownik": ['owi', 'om', ''],
		"biernik": ['a', 'ów', ''],
		"nadrzednik": ['em', 'ami', ''],
		"miejscownik": ['ie', 'ach', ''],
		"wolacz": ['ie', 'owie', '']
	},
	10: {
		"mianownik": ['ł', 'łowie', 'ł'],
		"dopelniacz": ['ła', 'łów', 'ł'],
		"celownik": ['łowi', 'łom', 'ł'],
		"biernik": ['ła', 'łów', 'ł'],
		"nadrzednik": ['łem', 'łami', 'ł'],
		"miejscownik": ['le', 'łach', 'ł'],
		"wolacz": ['le', 'łowie', 'ł']
	},
	11: {
		"mianownik": ['a', 'owie', 'a'],
		"dopelniacz": ['', 'ów', ''],
		"celownik": ['', 'om', ''],
		"biernik": ['ę', 'ów', 'ę'],
		"nadrzednik": ['ą', 'ami', 'ą'],
		"miejscownik": ['', 'ach', ''],
		"wolacz": ['o', 'owie', 'o']
	},
}

function checkSurname(last_characters, surname) {
	regex = new RegExp(last_characters + "$");
	return surname.match(regex);
}

function classificationSurname(surname) {
	for (number in classes) {
		console.log('number', number)
		if (classes.hasOwnProperty(number)) {
			var table_of_ends = classes[number]; //from current class

			for (var i = 0; i < table_of_ends.length; i++) {
				var test = checkSurname(table_of_ends[i], surname);

				if (test !== null) {
					var test_properties = {
						match: test,
						class_number: number
					}
					return test_properties;
				}
			}
		}
	}
}

function generateVariantsPerCases(surname_from_user) {
	var record = classificationSurname(surname_from_user);
	console.log('record', record)

	var surname_class = ends[record.class_number]
	var surname = record.match.input;

	for (prop in surname_class) {
		var CASE = surname_class[prop];
		var cutted_surname;
		if (prop === "mianownik" && CASE[0] !== "") {
			var index_of_end = surname.lastIndexOf(CASE[0])
			cutted_surname = surname.substring(0, index_of_end)
		}
		if (cutted_surname === undefined) {
			cutted_surname = surname;
		}
		console.log('________')
		console.log(prop)
		for (var i = 0; i < CASE.length; i++) {
			console.log(cutted_surname + CASE[i])
		}
	}
}