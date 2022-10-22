fpCountries = open(
    'countries_tag_list.txt', "r",encoding="utf-8")
fpResult = open("decision.txt", "w",encoding="utf-8")
n = 0

while True:
	tag = fpCountries.readline()[0:3]
	if not tag:
		break
	fpResult.write("""
	release_ABK = {	#ABK
		icon = generic_prepare_civil_war
		cost = 0
		available = {	always = yes	}
		visible = {	
			ABK = {	release_country_decision_trigger = yes	}
			release_CCS_decision_trigger = no
			release_SCC_decision_trigger = no
		}
		complete_effect = {	country_event = fate_of_ABK.1	}
		ai_will_do = {	base = 100	}
	}
	""")
	n += 1
fpCountries.close()
fpResult.close()
