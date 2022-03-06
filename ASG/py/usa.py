fpCountries = open(
    'D:\\Users\\blade\\02 Documents\\Git\\GEACPS_GFX\\ASG\\py\\america_countries_tag_list.txt', "r", encoding="utf-8")
fpResult = open(
	"D:\\Users\\blade\\02 Documents\\Git\\GEACPS_GFX\\ASG\\py\\usa.txt", "w", encoding="utf-8")
n = 0

while True:
	tag = fpCountries.readline()[0:3]
	if not tag:
		break
	fpResult.write("""country_event = {
	id = debug_USA."""+str(n)+"""
	immediate = {
		release = """+tag+"""
		country_event = {	debug_USA."""+str(n+1)+"""	day = 1	}
	}
}
""")
	n += 1
fpCountries.close()
fpResult.close()