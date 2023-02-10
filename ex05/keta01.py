# --------------------------------------------------------------------------------
# : color code
RED = '\033[91m'
GRE = '\033[92m'
YEL = '\033[93m'
BLU = '\033[94m'
MAG = '\033[95m'
CYA = '\033[96m'
RES = '\033[0m'
BOL = '\033[1m'
UND = '\033[4m'

# --------------------------------------------------------------------------------
# : function : keta
def ft_keta01(_dic):
	'''
	Display key-value of the dictionaries.
	  - [paramter] _dic
	'''
	if isinstance(_dic, dict):
		if all(isinstance(_var, str) for _var in _dic) and len(_dic):
			for _key, _val in _dic.items():
				print(
					f"{BLU}{BOL}{UND}[Keta00]{RES}",
					f"{CYA}{BOL}{UND}[{_key}]{RES} was created by",
					f"{CYA}{BOL}{UND}[{_val}]{RES}."
				)
		elif not len(_dic):
			print(
				f"{BLU}{BOL}{UND}[Keta00]{RES}",
				f"{RED}[Failure]{RES}",
				f"The {BOL}{UND}keta{RES} is {YEL}{BOL}empty{RES}."
			)
		else:
			print(
				f"{BLU}{BOL}{UND}[Keta00]{RES}",
				f"{RED}[Failure]{RES}",
				f"The {BOL}{UND}keta{RES} keta's elements contains {YEL}{BOL}non-string value{RES}."
			)
	else:
		print(
			f"{BLU}{BOL}{UND}[Keta00]{RES}",
			f"{RED}[Failure]{RES}",
			f"The {BOL}{UND}keta{RES} is not {YEL}{BOL}dictionary{RES}."
		)


# --------------------------------------------------------------------------------
# : main
# keta variable : dictionary
# default value:
#	'Python': 'Guido van Rossum',
#	'Ruby': 'Yukihiro Matsumoto',
#	'PHP': 'Rasmus Lerdorf',
keta = {
	'Python': 'Guido van Rossum',
	'Ruby': 'Yukihiro Matsumoto',
	'PHP': 'Rasmus Lerdorf',
}

ft_keta01(keta)