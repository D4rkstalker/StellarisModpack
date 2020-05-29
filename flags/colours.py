#Black is a required colour

#Name of stellaris colors file
filename = "colors.txt"
#Define file to write to
colour_file = open(filename, "w")

#Dictionary containing all colours
colour_dict = { 
		"light_green"	: "{ flag = hsv { 0.35 0.5 0.60 }	map = hsv { 0.32 0.4 0.7 }		ship = hsv { 0.36 0.6 1.1 } }", #VANILLA
		"aqua"			: "{ flag = rgb { 52 178 132 }		map = rgb { 88 186 146 }		ship = hsv { 0.48 0.65 1.15 } }",
		"cyan"			: "{ flag = rgb { 73 184 176 }		map = rgb { 81 192 185 }		ship = hsv { 0.50 0.59 1.15 } }",
		"cerulean"		: "{ flag = rgb { 72 158 191  }		map = rgb { 84 173 202 }		ship = hsv { 0.535 0.64 1.2 } }",
		"light_blue"	: "{ flag = hsv { 0.6 0.6 0.7 }		map = hsv { 0.6 0.4 0.8 }		ship = hsv { 0.60 0.5 1.1 } }", #VANILLA
		"periwinkle"	: "{ flag = rgb { 129 102 204 }		map = rgb { 149 120 201 }		ship = hsv { 0.73 0.29 1.2 } }",
		"lavender"		: "{ flag = rgb { 156 102 194 }		map = rgb { 171 115 199 }		ship = hsv { 0.81 0.29 1.2 } }",
		"green"			: "{ flag = hsv { 0.32 0.6 0.40 }	map = hsv { 0.32 0.4 0.55 }		ship = hsv { 0.4 0.8  1.1 } }", #VANILLA
		"teal"			: "{ flag = hsv { 0.42 0.6 0.5 }	map = hsv { 0.43 0.3 0.5 }		ship = hsv { 0.45 0.7 1.1 } }", #VANILLA
		"turquoise"		: "{ flag = hsv { 0.49 0.6 0.6 }	map = hsv { 0.5 0.7 0.8 }		ship = hsv { 0.51 0.8 1.1 } }", #VANILLA
		"azure"			: "{ flag = rgb { 30 107 167 }		map = rgb { 40 129 180 }		ship = hsv { 0.53 1.00 1.05 } }",
		"blue"			: "{ flag = hsv { 0.64 0.7 0.6 }	map = hsv { 0.6 0.5 0.6 }		ship = hsv { 0.59 0.8 1.3 } }", #VANILLA
		"violet"		: "{ flag = rgb { 86 56 175 }		map = rgb { 96 60 162 }			ship = hsv { 0.73 0.49 1.15 } }",
		"purple"		: "{ flag = rgb { 100 54 158 }		map = hsv { 0.8 0.4 0.5 }		ship = hsv { 0.75 0.65 1.2 } }", #VANILLA
		"dark_green"	: "{ flag = hsv { 0.33 0.6 0.27 }	map = hsv { 0.33 0.4 0.3 }		ship = hsv { 0.42 0.99 0.9 } }", #VANILLA
		"viridian"		: "{ flag = rgb { 0 63 47 }			map = rgb { 1 92 73 }			ship = rgb { 10 224 194 } }",
		"dark_teal"		: "{ flag = hsv { 0.5 0.6 0.3 }		map = hsv { 0.48 0.6 0.42 }		ship = hsv { 0.49 0.9 0.9 } }", #VANILLA
		"cobalt"		: "{ flag = rgb { 9 65 121 }		map = rgb { 1 76 129 }			ship = hsv { 0.53 1.00 0.95 } }",
		"dark_blue"		: "{ flag = hsv { 0.64 0.85 0.45 }	map = hsv { 0.58 0.7 0.4 }		ship = hsv { 0.62 0.9 1.2 } }", #VANILLA
		"indigo"		: "{ flag = hsv { 0.71 0.85 0.5 }	map = hsv { 0.71 0.85 0.5 }		ship = hsv { 0.71 0.7 1.0 } }", #VANILLA
		"dark_purple"	: "{ flag = rgb { 61 27 96 }		map = hsv { 0.85 0.6 0.35 }		ship = hsv { 0.76 0.75 1.0 } }", #VANILLA
		"lime"			: "{ flag = rgb { 128 158 27 }		map = rgb { 150 168 57 }		ship = hsv { 0.19 0.82 1.1 } }",
		"citrine"		: "{ flag = rgb { 170 159 0 }		map = rgb { 193 181 28 }		ship = hsv { 0.16 0.93 1.1 } }",
		"yellow"		: "{ flag = hsv { 0.11 0.8 0.8 }	map = hsv { 0.10 0.75 0.99 }	ship = hsv { 0.11 0.75 0.9 } }", #VANILLA
		"light_orange"	: "{ flag = hsv { 0.09 1.0 0.8 }	map = hsv { 0.09 0.8 0.8 }		ship = hsv { 0.10 0.97 1.1 } }", #VANILLA
		"red_orange"	: "{ flag = hsv { 0.01 0.75 0.7 }	map = hsv { 0.028 0.75 0.7 }	ship = hsv { 0.015 0.7 0.9 } }", #VANILLA
		"coral"			: "{ flag = rgb { 205 106 113 }		map = rgb { 232 133 142 }		ship = hsv { 0.98 0.29 1.2 } }",
		"rose"			: "{ flag = rgb { 204 102 139 }		map = rgb { 228 123 156 }		ship = hsv { 0.94 0.29 1.2 } }",
		"olive"			: "{ flag = rgb { 91 125 13 }		map = rgb { 105 131 36 }		ship = rgb { 213 253 21 } }",
		"mustard"		: "{ flag = rgb { 129 115 0 }		map = rgb { 159 146 31 }		ship = rgb { 244 232 9 } }",
		"gold"			: "{ flag = rgb { 152 92 0 }		map = rgb { 180 115 18 }		ship = hsv { 0.13 1.00 1.075 } }",
		"orange"		: "{ flag = hsv { 0.06 0.9 0.7 }	map = hsv { 0.075 0.8 0.7 }		ship = hsv { 0.07 0.8 1.2 } }", #VANILLA
		"red"			: "{ flag = hsv { 0.0 0.95 0.5 }	map = hsv { 0.99 0.8 0.7 }		ship = hsv { 0.0 0.95 0.8 } }", #VANILLA
		"byzantine"		: "{ flag = rgb { 138 31 71 }		map = rgb { 143 37 78 }			ship = rgb { 243 80 161 } }",
		"pink"			: "{ flag = rgb { 130 50 105 }		map = hsv { 0.95 0.35 0.6 }		ship = hsv { 0.9 0.65 1.1 } }", #VANILLA
		"dark_olive"	: "{ flag = rgb { 54 78 10 }		map = rgb { 61 88 17 }			ship = rgb { 205 252 40 } }",
		"dark_mustard"	: "{ flag = rgb { 87 70 1 }			map = rgb { 121 106 23 }		ship = rgb { 235 223 0 } }",
		"ochre"			: "{ flag = rgb { 105 60 0 }		map = rgb { 150 89 6 }			ship = rgb { 247 182 11 } }",
		"vermillion"	: "{ flag = rgb { 143 44 0 }		map = rgb { 180 72 22 }			ship = rgb { 255 133 3 } }",
		"dark_red"		: "{ flag = rgb { 85 17 17 }		map = rgb { 123 25 36 }			ship = rgb { 227 40 25 } }",
		"burgundy"		: "{ flag = hsv { 0.95 0.8 0.35 }	map = hsv { 0.93 0.6 0.42 }		ship = hsv { 0.92 0.5 0.6 } }", #VANILLA
		"plum"			: "{ flag = rgb { 79 24 62 }		map = rgb { 92 24 79 }			ship = rgb { 197 40 182 } }",
		"chestnut"		: "{ flag = rgb { 84 48 37 }		map = rgb { 122 77 61 }			ship = rgb { 216 159 152 } }",
		"brown"			: "{ flag = hsv { 0.07 0.6 0.4 }	map = hsv { 0.08 0.5 0.55 }		ship = hsv { 0.08 0.7 0.7 } }", #VANILLA
		"drab"			: "{ flag = rgb { 122 100 59 }		map = rgb { 146 119 81 }		ship = rgb { 232 207 158 } }",
		"beige"			: "{ flag = hsv { 0.1 0.4 0.6 }		map = hsv { 0.075 0.4 0.7 }		ship = hsv { 0.09 0.5 1.2 } }", #VANILLA
		"taupe"			: "{ flag = rgb { 91 73 62 }		map = rgb { 101 81 68 }			ship = rgb { 202 161 147 } }",
		"slate"			: "{ flag = rgb { 70 75 95 }		map = rgb { 101 108 129 }		ship = rgb { 206 220 255 } }",
		"gunmetal"		: "{ flag = rgb { 38 45 62 }		map = rgb { 68 77 94 }			ship = rgb { 175 194 245 } }",
		"sienna"		: "{ flag = rgb { 52 30 23 }		map = rgb { 83 47 32 }			ship = rgb { 205 132 125 } }",
		"dark_brown"	: "{ flag = hsv { 0.07 0.6 0.23 }	map = hsv { 0.06 0.5 0.35 } 	ship = hsv { 0.05 0.7 0.8 } }", #VANILLA
		"sepia"			: "{ flag = rgb { 84 68 35 }		map = rgb { 113 92 53 }			ship = rgb { 217 191 131 } }",
		"white"			: "{ flag = hsv { 0.65 0.03 0.725 }	map = rgb { 212 209 206 }		ship = hsv { 0.5 0.02 1.20 } use_as_border_color = no }",
		"grey"			: "{ flag = hsv { 0.65 0.05 0.35 }	map = hsv { 0.58 0.15 0.6 }		ship = hsv { 0.62 0.25 1.0 } use_as_border_color = no }", #VANILLA
		"dark_grey"		: "{ flag = hsv { 0.65 0.05 0.22 }	map = hsv { 0.6 0.2 0.3 }		ship = hsv { 0.62 0.2 1.0 } use_as_border_color = no }", #VANILLA
		"black"			: "{ flag = hsv { 0.5 0.3 0.05 }	map = hsv { 0.7 0.1 0.18 }		ship = hsv { 0.72 0.2 1.0 } use_as_border_color = no }", #VANILLA
}

#Write disclamers to begining of file
colour_file.write("#this file is reloadable with the filewatcher only\n#This file was generated with colours.py\n\ncolors = {\n")

#Define colours list and populate from colour dictionary while also deifining stellaris colours in colors file
colours = []
for k, v in colour_dict.items():
	colours.append(k)
	colour_file.write("\t\t{} = {}\n".format(k, v))

colour_file.write("}\n\n")

for colour_index, colour in enumerate(colours):
	#Generate every posible random colour combinations for each colour
	#Skip non border colours
	#Note: this causes a glitch where you lose one colour combo at end of list
	if colour in ["white", "dark_grey", "black"]: continue
	colour_file.write("\t\t#{}\n".format(colour.upper()))

	for colour_index2, v in enumerate(colours[colour_index:]):
		#Iterate through every colour starting from colour index from parent for loop
		combo = "\t\trandomizable_combo = {{ {} {} {} }}\n"
		icolour = colours[colour_index+colour_index2]

		#Skip black because black is placed in every combo
		if icolour == "black": continue

		colour_file.write(combo.format(colour, icolour, "black"))
	colour_file.write("\n")