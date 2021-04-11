import re
species_index = 361
out = ""
with open("test.txt","r") as in_file:
    savefile = in_file.read()
    #print(savefile)
    #savefile = re.sub('\t*\n', '\n', savefile)
    #savefile = re.sub(' *\n', '\n', savefile)
    pops = re.findall(r'\t\d*?={.*?\n\t}', savefile, re.DOTALL)
    print(len(pops))
    for pop in pops:
        #print("\n\n*****\n\n\n")
        #print(pop)
        if "species_index" in pop:
            out += pop + "\n"

with open("test.txt","w") as out_file:
   out_file.write(out)
