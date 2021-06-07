fpCountries = open(
    '.\countries_tag_list.txt', "r",encoding="utf,8")
fpResult = open(".\colonial.txt", "w",encoding="utf,8")
n = 0

while True:
	tag = fpCountries.readline()[0:3]
	if not tag:
		break
	fpResult.write("""
 """+tag+"""_dominion:0 "$"""+tag+"""$自治領"
 """+tag+"""_dominion_DEF:0 "$"""+tag+"""$自治領"
 """+tag+"""_colony:0 "$OVERLORDADJ$領$"""+tag+"""$植民地"
 """+tag+"""_colony_DEF:0 "$OVERLORDADJ$領$"""+tag+"""$植民地"
 """+tag+"""_colony_ADJ:0 "$OVERLORDADJ$領$"""+tag+"""$"
 """+tag+"""_overseas_territory:0 "$OVERLORDADJ$領$"""+tag+"""$"
 """+tag+"""_overseas_territory_DEF:0 "$OVERLORDADJ$領$"""+tag+"""$"
 """+tag+"""_overseas_territory_HOL:0 "$OVERLORDADJ$領$"""+tag+"""$地域"
 """+tag+"""_overseas_territory_HOL_DEF:0 "$OVERLORDADJ$領$"""+tag+"""$地域"
 """+tag+"""_overseas_territory_POR:0 "$OVERLORDADJ$領$"""+tag+"""$海外州"
 """+tag+"""_overseas_territory_POR_DEF:0 "$OVERLORDADJ$領$"""+tag+"""$海外州"
 """+tag+"""_overseas_territory_SPR:0 "$OVERLORDADJ$領$"""+tag+"""$州"
 """+tag+"""_overseas_territory_SPR_DEF:0 "$OVERLORDADJ$領$"""+tag+"""$州"
 """+tag+"""_overseas_territory_ADJ:0 "$OVERLORDADJ$領$"""+tag+"""$"
 """+tag+"""_federation_of_colonies:0 "$OVERLORDADJ$領$"""+tag+"""$連邦"
 """+tag+"""_federation_of_colonies_DEF:0 "$OVERLORDADJ$領$"""+tag+"""$連邦"
 """+tag+"""_federation_of_colonies_ADJ:0 "$OVERLORDADJ$領$"""+tag+"""$"
 """+tag+"""_colony_and_protectorate:0 "$OVERLORDADJ$領$"""+tag+"""$植民地及び保護領"
 """+tag+"""_colony_and_protectorate_DEF:0 "$OVERLORDADJ$領$"""+tag+"""$植民地及び保護領"
 """+tag+"""_colony_and_protectorate_ADJ:0 "$OVERLORDADJ$領$"""+tag+"""$"
 """+tag+"""_protected_territory:0 "$OVERLORDADJ$保護領$"""+tag+"""$"
 """+tag+"""_protected_territory_DEF:0 "$OVERLORDADJ$保護領$"""+tag+"""$"
 """+tag+"""_protected_territory_ADJ:0 "$OVERLORDADJ$領$"""+tag+"""$"
 """+tag+"""_mandate:0 "$OVERLORDADJ$委任統治領$"""+tag+"""$地域"
 """+tag+"""_mandate_DEF:0 "$OVERLORDADJ$委任統治領$"""+tag+"""$地域"
 """+tag+"""_mandate_ADJ:0 "$OVERLORDADJ$領$"""+tag+"""$"
 """+tag+"""_imperial_member:0 "$OVERLORDADJ$領$"""+tag+"""$王国"
 """+tag+"""_imperial_member_DEF:0 "$OVERLORDADJ$領$"""+tag+"""$王国"
 """+tag+"""_imperial_member_ADJ:0 "$OVERLORDADJ$領$"""+tag+"""$"
 """+tag+"""_imperial_overseas_territory:0 "$OVERLORDADJ$領$"""+tag+"""$"
 """+tag+"""_imperial_overseas_territory_DEF:0 "$OVERLORDADJ$領$"""+tag+"""$"
 """+tag+"""_imperial_overseas_territory_ADJ:0 "$OVERLORDADJ$領$"""+tag+"""$"
 """+tag+"""_us_commonwealth:0 "$OVERLORDADJ$領$"""+tag+"""$自治連邦区"
 """+tag+"""_us_commonwealth_DEF:0 "$OVERLORDADJ$領$"""+tag+"""$自治連邦区"
 """+tag+"""_us_commonwealth_ADJ:0 "$OVERLORDADJ$領$"""+tag+"""$"
 """+tag+"""_us_territory:0 "$OVERLORDADJ$領$"""+tag+"""$準州"
 """+tag+"""_us_territory_DEF:0 "$OVERLORDADJ$領$"""+tag+"""$準州"
 """+tag+"""_us_territory_ADJ:0 "$OVERLORDADJ$領$"""+tag+"""$"
 """+tag+"""_soviet_member_federal_republic:0 "$"""+tag+"""$・ソビエト連邦社会主義共和国"
 """+tag+"""_soviet_member_federal_republic_DEF:0 "$"""+tag+"""$・ソビエト連邦社会主義共和国"
 """+tag+"""_soviet_member_republic:0 "$"""+tag+"""$・ソビエト社会主義共和国"
 """+tag+"""_soviet_member_republic_DEF:0 "$"""+tag+"""$・ソビエト社会主義共和国"
 """+tag+"""_soviet_autonomous_republic:0 "$"""+tag+"""$自治ソビエト社会主義共和国"
 """+tag+"""_soviet_autonomous_republic_DEF:0 "$"""+tag+"""$自治ソビエト社会主義共和国"
""")
	n += 1
fpCountries.close()
fpResult.close()