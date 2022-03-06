fpResult = open(
	"D:\\Users\\blade\\02 Documents\\Git\\GEACPS_GFX\\ASG\\py\\test.txt", "w", encoding="utf-8")
n = 0

for tag in range(52):
	fpResult.write("""
				if = {
					limit = {	ROOT = {	NOT = {	has_cosmetic_tag = AMERICA_united_states_"""+str(tag)+"""	}	}	}
					if = {
						limit = {
							ROOT = {	has_AMERICA_united_states_n_cosmetic_tag = yes	}
							count_triggers = {
								amount = """+str(tag)+"""
								ROOT = {	any_owned_state = {	check_variable = {	ABA_state_variable = 1	}	is_core_of = ROOT	}	}
								ROOT = {	any_owned_state = {	check_variable = {	ALS_state_variable = 1	}	is_core_of = ROOT	}	}
								ROOT = {	any_owned_state = {	check_variable = {	ARK_state_variable = 1	}	is_core_of = ROOT	}	}
								ROOT = {	any_owned_state = {	check_variable = {	ARZ_state_variable = 1	}	is_core_of = ROOT	}	}
								ROOT = {	any_owned_state = {	check_variable = {	CAL_state_variable = 1	}	is_core_of = ROOT	}	}
								ROOT = {	any_owned_state = {	check_variable = {	CLD_state_variable = 1	}	is_core_of = ROOT	}	}
								ROOT = {	any_owned_state = {	check_variable = {	CNT_state_variable = 1	}	is_core_of = ROOT	}	}
								ROOT = {	any_owned_state = {	check_variable = {	DEL_state_variable = 1	}	is_core_of = ROOT	}	}
								ROOT = {	any_owned_state = {	check_variable = {	FLO_state_variable = 1	}	is_core_of = ROOT	}	}
								ROOT = {	any_owned_state = {	check_variable = {	GEG_state_variable = 1	}	is_core_of = ROOT	}	}
								ROOT = {	any_owned_state = {	check_variable = {	HAW_state_variable = 1	}	is_core_of = ROOT	}	}
								ROOT = {	any_owned_state = {	check_variable = {	IDA_state_variable = 1	}	is_core_of = ROOT	}	}
								ROOT = {	any_owned_state = {	check_variable = {	IDI_state_variable = 1	}	is_core_of = ROOT	}	}
								ROOT = {	any_owned_state = {	check_variable = {	ILI_state_variable = 1	}	is_core_of = ROOT	}	}
								ROOT = {	any_owned_state = {	check_variable = {	IOW_state_variable = 1	}	is_core_of = ROOT	}	}
								ROOT = {	any_owned_state = {	check_variable = {	KAN_state_variable = 1	}	is_core_of = ROOT	}	}
								ROOT = {	any_owned_state = {	check_variable = {	KTY_state_variable = 1	}	is_core_of = ROOT	}	}
								ROOT = {	any_owned_state = {	check_variable = {	LUI_state_variable = 1	}	is_core_of = ROOT	}	}
								ROOT = {	any_owned_state = {	check_variable = {	MAS_state_variable = 1	}	is_core_of = ROOT	}	}
								ROOT = {	any_owned_state = {	check_variable = {	MCG_state_variable = 1	}	is_core_of = ROOT	}	}
								ROOT = {	any_owned_state = {	check_variable = {	MIS_state_variable = 1	}	is_core_of = ROOT	}	}
								ROOT = {	any_owned_state = {	check_variable = {	MNE_state_variable = 1	}	is_core_of = ROOT	}	}
								ROOT = {	any_owned_state = {	check_variable = {	MNS_state_variable = 1	}	is_core_of = ROOT	}	}
								ROOT = {	any_owned_state = {	check_variable = {	MRL_state_variable = 1	}	is_core_of = ROOT	}	}
								ROOT = {	any_owned_state = {	check_variable = {	MSS_state_variable = 1	}	is_core_of = ROOT	}	}
								ROOT = {	any_owned_state = {	check_variable = {	MTA_state_variable = 1	}	is_core_of = ROOT	}	}
								ROOT = {	any_owned_state = {	check_variable = {	NCR_state_variable = 1	}	is_core_of = ROOT	}	}
								ROOT = {	any_owned_state = {	check_variable = {	NDA_state_variable = 1	}	is_core_of = ROOT	}	}
								ROOT = {	any_owned_state = {	check_variable = {	NEB_state_variable = 1	}	is_core_of = ROOT	}	}
								ROOT = {	any_owned_state = {	check_variable = {	NEV_state_variable = 1	}	is_core_of = ROOT	}	}
								ROOT = {	any_owned_state = {	check_variable = {	NHN_state_variable = 1	}	is_core_of = ROOT	}	}
								ROOT = {	any_owned_state = {	check_variable = {	NJE_state_variable = 1	}	is_core_of = ROOT	}	}
								ROOT = {	any_owned_state = {	check_variable = {	NMX_state_variable = 1	}	is_core_of = ROOT	}	}
								ROOT = {	any_owned_state = {	check_variable = {	NYR_state_variable = 1	}	is_core_of = ROOT	}	}
								ROOT = {	any_owned_state = {	check_variable = {	OHO_state_variable = 1	}	is_core_of = ROOT	}	}
								ROOT = {	any_owned_state = {	check_variable = {	OKL_state_variable = 1	}	is_core_of = ROOT	}	}
								ROOT = {	any_owned_state = {	check_variable = {	ORE_state_variable = 1	}	is_core_of = ROOT	}	}
								ROOT = {	any_owned_state = {	check_variable = {	PEN_state_variable = 1	}	is_core_of = ROOT	}	}
								ROOT = {	any_owned_state = {	check_variable = {	PUE_state_variable = 1	}	is_core_of = ROOT	}	}
								ROOT = {	any_owned_state = {	check_variable = {	RIL_state_variable = 1	}	is_core_of = ROOT	}	}
								ROOT = {	any_owned_state = {	check_variable = {	SCR_state_variable = 1	}	is_core_of = ROOT	}	}
								ROOT = {	any_owned_state = {	check_variable = {	SDA_state_variable = 1	}	is_core_of = ROOT	}	}
								ROOT = {	any_owned_state = {	check_variable = {	TEN_state_variable = 1	}	is_core_of = ROOT	}	}
								ROOT = {	any_owned_state = {	check_variable = {	TEX_state_variable = 1	}	is_core_of = ROOT	}	}
								ROOT = {	any_owned_state = {	check_variable = {	UTA_state_variable = 1	}	is_core_of = ROOT	}	}
								ROOT = {	any_owned_state = {	check_variable = {	VRG_state_variable = 1	}	is_core_of = ROOT	}	}
								ROOT = {	any_owned_state = {	check_variable = {	VRM_state_variable = 1	}	is_core_of = ROOT	}	}
								ROOT = {	any_owned_state = {	check_variable = {	WAS_state_variable = 1	}	is_core_of = ROOT	}	}
								ROOT = {	any_owned_state = {	check_variable = {	WSC_state_variable = 1	}	is_core_of = ROOT	}	}
								ROOT = {	any_owned_state = {	check_variable = {	WVI_state_variable = 1	}	is_core_of = ROOT	}	}
								ROOT = {	any_owned_state = {	check_variable = {	WYO_state_variable = 1	}	is_core_of = ROOT	}	}
							}
						}
						ROOT = {	drop_cosmetic_tag = yes	set_cosmetic_tag = AMERICA_united_states_"""+str(tag)+"""	}
					}
				}""")
fpResult.close()