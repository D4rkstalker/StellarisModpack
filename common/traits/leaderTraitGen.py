 
traitList ="""trait_overhual_radar_1_scientist
trait_overhual_radar_2_scientist
trait_overhual_radar_3_scientist
trait_overhual_radar_4_scientist
trait_overhual_fabrication_1_scientist
trait_overhual_fabrication_2_scientist
trait_overhual_fabrication_3_scientist
trait_overhual_fabrication_4_scientist"""

traits = traitList.split("\n")

frame = """ = {
	icon =  "gfx/interface/icons/traits/<<<REPLACE>>>.dds"
	cost = 0
	leader_trait = yes
	leader_class = { scientist }
	randomized = no
	initial = no
	modification = no
	modifier = {
	}
}
"""

for trait in traits:
    temp = trait.replace("_scientist", "")
    out = trait + frame.replace("<<<REPLACE>>>",temp)
    print(out)