# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    process_input.py                                   :+:    :+:             #
#                                                      +:+                     #
#    By: npanday <npanday@student.codam.nl>           +#+                      #
#                                                    +#+                       #
#    Created: 2019/10/22 16:06:28 by npanday        #+#    #+#                 #
#    Updated: 2019/10/22 16:06:28 by npanday       ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

from get_machine import machine, args, sys

input = args.input
if not set(input).issubset(set(machine['alphabet'])):
	sys.exit("Error: Invalid character in input")

# print("Alphabet: " + str(machine['alphabet']))
# print("States\t: " + str(machine['states']))
# print("Initial\t: " + machine['initial'])
# print("Finals\t: " + str(machine['finals']))

buffer_size = 30
input += (buffer_size - len(input)) * machine['blank']
state = machine['initial']
i = 0
while state not in machine['finals']:
	string = list(input)
	string[i] = '<' + string[i] + '>'
	left = '[' + "".join(string) + "] (" + state + ", " + input[i] + ")"
	trans = machine['transitions'][state]
	j = 0
	while trans[j]['read'] != input[i]:
		j += 1
		if j == len(trans):
			sys.exit("Error: undefined transition")
	trans = trans[j]
	state = trans['to_state']
	new = list(input)
	new[i] = trans['write']
	input = "".join(new)
	right = "(" + state + ", " + input[i] + ", " + trans['action'] + ")"
	print(left + " -> " + right)
	i += (-1, 1)[trans['action'] == "RIGHT"]
	if i == -1:
		input = machine['blank'] + input
		input += (buffer_size - len(input)) * machine['blank']
		i = 0
	if i == len(input):
		input += machine['blank']