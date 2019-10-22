# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    get_machine.py                                     :+:    :+:             #
#                                                      +:+                     #
#    By: npanday <npanday@student.codam.nl>           +#+                      #
#                                                    +#+                       #
#    Created: 2019/10/22 16:06:42 by npanday        #+#    #+#                 #
#    Updated: 2019/10/22 16:06:42 by npanday       ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

import argparse, json, sys

parser = argparse.ArgumentParser()
parser.add_argument('jsonfile', help='json description of machine')
parser.add_argument('input', help='input of the machine')
args = parser.parse_args()

def verify(machine):
	valid_fields = {'name', 'alphabet', 'blank', 'states', 'initial', 'finals', 'transitions'}
	if machine.keys() != valid_fields:
		return "Machine has invalid number of fields"
	for field in machine.keys():
		if field not in valid_fields:
			return field + " is not a valid field"
	for char in machine['alphabet']:
		if len(char) != 1:
			return "character '" + char + "' is too long"
	if machine['blank'] not in machine['alphabet']:
		return "blank character '" + machine['blank'] + "' is not in given alphabet"
	if machine['initial'] not in machine['states']:
		return "Initial state is invalid"
	for final in machine['finals']:
		if final not in machine['states']:
			return "Final-state-set has invalid members"
	if not set(machine['transitions'].keys()).issubset(machine['states']):
		return "Machine has invalid transitions"
	for state in machine['transitions']:
		for trans in machine['transitions'][state]:
			if trans.keys() != {"read", "to_state", "write", "action"}:
				return "Machine has invalid transition descriptions"

def get_machine():
	jsonfile = open(args.jsonfile)
	machine = json.load(jsonfile)
	jsonfile.close()
	return machine

machine = get_machine()
error = verify(machine)
if error:
	sys.exit("Error: " + error)
input = args.input
if not set(input).issubset(set(machine['alphabet'])):
	sys.exit("Error: Invalid character in input")