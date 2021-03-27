import re

out = ""
with open("test.txt","r") as in_file:
    savefile = in_file.read()

    pops = re.findall(r'\w*? = {.*?\n}', savefile, re.DOTALL)

    for pop in pops:
        if "species_index" not in pop:
            out += pop + "\n"

with open("test.txt","w") as out_file:
    out_file.write(out)
