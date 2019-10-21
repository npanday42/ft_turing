from get_machine import machine, args, sys

input = args.input
if not set(input).issubset(set(machine['alphabet'])):
	sys.exit("Error: Invalid character in input")

print("Alphabet: " + str(machine['alphabet']))
print("States\t: " + str(machine['states']))
print("Initial\t: " + machine['initial'])
print("Finals\t: " + str(machine['finals']))

buffer_size = 30
input += (buffer_size - len(input)) * '.'
state = machine['initial']
i = 0
while state not in machine['finals']:
	trans = machine['transitions'][state]
	string = list(input)
	string[i] = '<' + string[i] + '>'
	left = '[' + "".join(string) + "] (" + state + ", " + input[i] + ")"
	j = 0
	while trans[j]['read'] != input[i]:
		j += 1
	trans = trans[j]
	state = trans['to_state']
	new = list(input)
	new[i] = trans['write']
	input = "".join(new)
	right = "(" + state + ", " + input[i] + ", " + trans['action'] + ")"
	print(left + " -> " + right)
	i += (-1, 1)[trans['action'] == "RIGHT"]