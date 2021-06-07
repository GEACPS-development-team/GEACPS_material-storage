fpCountries = open(
    '.\countries_tag_list.txt', "r",encoding="utf-8")
fpResult = open(".\loc.txt", "w",encoding="utf-8")
n = 0

while True:
	tag = fpCountries.readline()[0:3]
	if not tag:
		break
	fpResult.write(""" release_"""+tag+""":0 "$"""+tag+"""_ADJ$の運命"
 fate_of_"""+tag+""".1.t:0 "$"""+tag+"""_ADJ$の運命"
 fate_of_"""+tag+""".1.d:0 "我々は旧$"""+tag+"""_ADJ$領土を手に入れた。この領土を我々はどのようにすべきだろうか?"
 fate_of_"""+tag+""".1.0:0 "従順な国家を"
""")
	n += 1
fpCountries.close()
fpResult.close()