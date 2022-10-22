country_tags = open('.\countries_tag_list.txt', "r", encoding="utf-8")
write_evnet = open(".\event.txt", "w", encoding="utf-8")
write_decision = open(".\decision.txt", "w", encoding="utf-8")
write_localisation = open(".\localisation.txt", "w", encoding="utf-8")
n = 0

while True:
	tag = country_tags.readline()[0:3]
	if not tag:
		break
	write_evnet.write("""
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
					release_country_setting = yes
				}
			}
			else = {	"""+tag+""" = {	release_country_setting = yes	}	}
		}
	}
	immediate = {	log = "[GetDateText]: [Root.GetName]: event fate_of_"""+tag+""".0"	}
}
country_event = {
	id = fate_of_"""+tag+""".1
	title = fate_of_"""+tag+""".1.t
	desc = fate_of_"""+tag+""".1.d
	is_triggered_only = yes
	
	option = {
		name = fate_of_"""+tag+""".1.0
		ai_chance = {	base = 10	}
		country_event = fate_of_"""+tag+""".2
	}
	option = {
		name = fate_of_"""+tag+""".1.1
	}
	option = {
		name = fate_of_"""+tag+""".1.2
	}
	option = {
		name = fate_of_"""+tag+""".1.3
	}
	immediate = {	log = "[GetDateText]: [Root.GetName]: event fate_of_"""+tag+""".1"	}
}
country_event = {
	id = fate_of_"""+tag+""".2
	title = fate_of_"""+tag+""".2.t
	desc = fate_of_"""+tag+""".2.d
	is_triggered_only = yes
	
	option = {
		name = fate_of_"""+tag+""".2.0
		ai_chance = {	base = 10	}
		ROOT = {	set_country_flag = """+tag+"""_republic_flag	}
		country_event = fate_of_"""+tag+""".3
	}
	immediate = {	log = "[GetDateText]: [Root.GetName]: event fate_of_"""+tag+""".2"	}
}
country_event = {
	id = fate_of_"""+tag+""".3
	title = fate_of_"""+tag+""".3.t
	desc = fate_of_"""+tag+""".3.d
	is_triggered_only = yes
	
	option = {
		name = fate_of_"""+tag+""".3.0
		ai_chance = {	base = 10	}
		country_event = fate_of_"""+tag+""".0
	}
	option = {
		name = fate_of_"""+tag+""".3.1
		# ROOT = {	set_country_flag = 	}
		country_event = fate_of_"""+tag+""".4
	}
	option = {
		name = fate_of_"""+tag+""".3.2
		# ROOT = {	set_country_flag = 	}
		country_event = fate_of_"""+tag+""".0
	}
	immediate = {	log = "[GetDateText]: [Root.GetName]: event fate_of_"""+tag+""".3"	}
}
""")
	write_decision.write("""
	release_"""+tag+""" = {	#"""+tag+"""
		icon = generic_prepare_civil_war
		cost = 0
		available = {	hidden_trigger = {	always = yes	}	}
		visible = {
			if = {
				limit = {	"""+tag+""" = {	release_decision_trigger_1 = no	}	}
				if = {
					limit = {	any_owned_core_claimed_state_ROOT = no	}
					any_owned_state = {
						NOT = {	is_core_of = ROOT	}
						NOT = {	is_claimed_by = ROOT	}
						check_variable = {	"""+tag+"""_state_variable = 1	}
					}
					else = {	always = no	}
				}
				else = {	always = no	}
			}
			else = {	always = no	}
		}
		complete_effect = {	country_event = fate_of_"""+tag+""".1	}
		ai_will_do = {	base = 100	}
		remove_effect = {	log = "[GetDateText]: [Root.GetName]: decision release_"""+tag+""""	}
	}
	""")
	write_localisation.write("""
 release_"""+tag+""":0 "$"""+tag+"""_ADJ$の運命"
 fate_of_"""+tag+""".1.t:0 "$release_"""+tag+"""$"
 fate_of_"""+tag+""".1.d:0 ""
 fate_of_"""+tag+""".1.0:0 "従順な国家を樹立"
 fate_of_"""+tag+""".1.1:0 "我々の領土を回収"
 fate_of_"""+tag+""".1.2:0 "友邦に領土を与える"
 fate_of_"""+tag+""".1.3:0 "地域ごとに考えよう"
 fate_of_"""+tag+""".2.t:0 "$release_"""+tag+r"""$\n国家体制"
 fate_of_"""+tag+""".2.d:0 "解放する$"""+tag+"""_ADJ$はどのような体制であるべきだろうか？"
 fate_of_"""+tag+""".2.0:0 "共和国として解放"
 fate_of_"""+tag+""".3.t:0 "$release_"""+tag+r"""$\n領域"
 fate_of_"""+tag+""".3.d:0 "解放する$"""+tag+"""_ADJ$はどのような領域であるべきだろうか？"
 fate_of_"""+tag+""".3.0:0 "$"""+tag+"""_ADJ$本土のみだな"
 fate_of_"""+tag+""".3.1:0 "地域ごとに与える領土考えよう……"
 fate_of_"""+tag+""".3.2:0 "彼の国は大きくあるべきだ"
 """)
	n += 1
write_evnet.close()


country_tags.close()
