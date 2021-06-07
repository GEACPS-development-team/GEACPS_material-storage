fpCountries = open(
    '.\countries_tag_list.txt', "r",encoding="utf-8")
fpResult = open(".\event.txt", "w",encoding="utf-8")
n = 0

while True:
	tag = fpCountries.readline()[0:3]
	if not tag:
		break
	fpResult.write("""
add_namespace = fate_of_"""+tag+"""
country_event = {
	id = fate_of_"""+tag+""".0
	title = fate_of_"""+tag+""".0.t
	desc = fate_of_"""+tag+""".0.d
	is_triggered_only = yes
	option = {
		name = fate_of_"""+tag+""".0.0
		ai_chance = {	base = 10	}
		hidden_effect = {
			if = {
				limit = {	country_exists = """+tag+"""	}
				create_dynamic_country = {
					original_tag = """+tag+"""
					clear_autonomous_states_variable = yes
					every_state = {
						limit = {
							is_fully_controlled_by = ROOT
							check_variable = {	"""+tag+"""_state_variable = 1	}
							NOT = {	is_core_of = ROOT	is_claimed_by = ROOT	}
						}
						PREV = {	transfer_state = PREV	}
					}
					retire_all_ideology_leader = yes
					set_cosmetic_tag = """+tag+"""
					ROOT = {	puppet = PREV	}
				}
			}
			else = {
				"""+tag+""" = {
					clear_autonomous_states_variable = yes
					every_state = {
						limit = {
							is_fully_controlled_by = ROOT
							check_variable = {	"""+tag+"""_state_variable = 1	}
						}
						"""+tag+""" = {	transfer_state = PREV	}
					}
					retire_all_ideology_leader = yes
					set_cosmetic_tag = """+tag+"""
					ROOT = {	puppet = """+tag+"""	}
				}
			}
			country_event = {	id = fate_of_"""+tag+""".1	day = 10	}
		}
	}
}
	""")
	n += 1
fpCountries.close()
fpResult.close()