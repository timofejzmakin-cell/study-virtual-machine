import argparse

def mask(n):
    return ((2**n)-1)


def execute(bytecode):

	memory = [0] * 32
	registers = [0] * 16
	
	
	for i in range(0, len(bytecode), 5):
		command = bytecode[i:i+5]
		command = int.from_bytes(command, 'little')
		op = command & 0B1111_1111
		if op == 84:
			const = (command >> 8) & mask(23)
			dest_register = (command >> 31) & mask(6)
			registers[dest_register] = const

		if op == 223:
			dest_register = (command >> 8) & mask(6)
			source_memory_addr = (command >> 14) & mask(6)
			registers[dest_register] = memory[registers[source_memory_addr]]
		if op == 9:
			dest_memory = (command >> 8) & mask(23)
			source_register = (command >> 31) & mask(6)
			memory[dest_memory] = registers[source_register]			
		if op == 213:
			dest_register = (command >> 8) & mask(6)
			shift_memory_register = (command >> 14) & mask(6)

			b = registers[dest_register]
			c = memory[registers[shift_memory_register]] 
			result = (b >> c) | ((b & mask(c)) << (6-c))
			registers[dest_register] = result
	return memory, registers

def main():
	parser = argparse.ArgumentParser()        
	parser.add_argument('-i', '--input', required=True)      
	parser.add_argument('-o', '--output', required=True)
	args = parser.parse_args()



	with open(args.input, 'rb') as file:
		bytecode = file.read()

	memory, registers = execute(bytecode)
	print(memory)
	print(registers)

if __name__ == "__main__":
    main()
