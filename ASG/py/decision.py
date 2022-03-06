fpCountries = open(
    'countries_tag_list.txt', "r",encoding="utf-8")
fpResult = open("decision.txt", "w",encoding="utf-8")
n = 0

while True:
	tag = fpCountries.readline()[0:3]
	if not tag:
		break
	fpResult.write("""
	release_"""+tag+""" = {
		icon = generic_prepare_civil_war
		cost = 0
		available = {
			any_state = {
				is_owned_by = ROOT
				check_variable = {	"""+tag+"""_state_variable = 1	}
				NOT = {	is_core_of = ROOT	is_claimed_by = ROOT	}
			}
			NOT = {	ROOT = {	original_tag = """+tag+"""	}	}
		}
		visible = {
			any_state = {
				is_owned_by = ROOT
				check_variable = {	"""+tag+"""_state_variable = 1	}
				NOT = {	is_core_of = ROOT	is_claimed_by = ROOT	}
			}
			NOT = {	ROOT = {	original_tag = """+tag+"""	}	}
		}
		complete_effect = {	country_event = fate_of_"""+tag+""".1	}
		ai_will_do = {	base = 100	}
	}
	""")
	n += 1
fpCountries.close()
fpResult.close()