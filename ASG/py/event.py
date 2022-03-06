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
	hidden = yes
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
							NOT = {	is_core_of = ROOT	}
							NOT = {	is_claimed_by = ROOT	}
							check_variable = {	"""+tag+"""_state_variable = 1	}
						}
						PREV = {	transfer_state = PREV	}
					}
					retire_all_ideology_leader = yes
					drop_cosmetic_tag = yes
					ROOT = {	puppet = PREV	}
				}
			}
			else = {
				"""+tag+""" = {
					clear_autonomous_states_variable = yes
					every_state = {
						limit = {
							is_fully_controlled_by = ROOT
							NOT = {	is_core_of = ROOT	}
							NOT = {	is_claimed_by = ROOT	}
							check_variable = {	"""+tag+"""_state_variable = 1	}
						}
						PREV = {	transfer_state = PREV	}
					}
					retire_all_ideology_leader = yes
					drop_cosmetic_tag = yes
					ROOT = {	puppet = PREV	}
				}
			}
		}
	}
}
country_event = {
	id = fate_of_"""+tag+""".1
	title = fate_of_"""+tag+""".1.t
	desc = fate_of_"""+tag+""".1.d
	is_triggered_only = yes
	
	option = {
		name = fate_of_"""+tag+""".1.0
		ai_chance = {	base = 10	}
		country_event = fate_of_"""+tag+""".0
	}
}
	""")
	n += 1
fpCountries.close()
fpResult.close()
