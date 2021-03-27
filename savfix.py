savefile = open("gamestate.txt","r").readlines()
part1 = ""
part2 = ""
part3 = ""
pop_ = False
passed = False
level = 0
for line in savefile:
    if not passed:
        part1 += (line + "\n")
    else if passed:
        part3 += (line + "\n")
    if = "last_created_pop=" in line:
        pop_ = False
        passed = True
    if pop_:
        part2 += (line + "\n")
    if "pop={" in line:
        pop_ = True:

pops = re.findall(r'\w*? = {.*?\n}', part3, re.DOTALL)

for pop in pops:
    if "species_index" not in pop:
        part2 += pop
