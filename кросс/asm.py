import argparse
import pprint

#Команды для УВМ
def write_const(const: int, addr: int):
	output = 0
	output |= 84
	output |= (const << 8)
	output |= (addr << 31)
	return output.to_bytes(5, 'little')

def read_value(dest_addr: int, source_addr: int):
	output = 0
	output |= 223
	output |= (dest_addr << 8)
	output |= (source_addr << 14)
	return output.to_bytes(5, 'little')

def write_value(dest_addr: int, source_addr: int):
	output = 0
	output |= 9
	output |= (dest_addr << 8)
	output |= (source_addr << 31)
	return output.to_bytes(5, 'little')

def rshift(dest_addr: int, source_addr: int):
	output = 0
	output |= 213
	output |= (dest_addr << 8)
	output |= (source_addr << 14)
	return output.to_bytes(5, 'little')

#Тесты из варианта
def test():
	assert list(write_const(862, 19)) == [0x54, 0x5E, 0x03, 0x80, 0x09], 'ASM ERROR write_const'
	assert list(read_value(43, 11)) == [0xDF, 0xEB, 0x02, 0x00, 0x00], 'ASM ERROR read_value'
	assert list(write_value(955, 60)) == [0x09, 0xBB, 0x03, 0x00, 0x1E], 'ASM ERROR write_value'
	assert list(rshift(36, 48)) == [0xD5, 0x24, 0x0C, 0x00, 0x00], 'ASM ERROR rshift'



def asm(commands):
	bytecode = bytes()
	for i in commands:
		command = i.split(' ')
		if command[0] == 'write_const':
			bytecode += write_const(int(command[1]), int(command[2]))
		elif command[0] == 'read_value':
			bytecode += read_value(int(command[1]), int(command[2]))
		elif command[0] == 'write_value':
			bytecode += write_value(int(command[1]), int(command[2]))
		elif command[0] == 'rshift':
			bytecode += rshift(int(command[1]), int(command[2]))
		else:
			print("SOME STRANGE ASM ERROR, LOOK AT ME")

	return bytecode





def main():
    parser = argparse.ArgumentParser()        
    parser.add_argument('-i', '--input', required=True)      
    parser.add_argument('-o', '--output', required=True)
    parser.add_argument('-t', '--test', required=True)
    args = parser.parse_args()
    


    with open(args.input) as file:
        input_file = file.read()

    #bytecode = asm(list(input_file.split('\n')))
    bytecode = asm(list(input_file.split('\n'))) 

    with open(args.output, 'wb') as output_file:
    	output_file.write(bytecode)

    if args.test == '1':
    	print('ARGUMENTS:')
    	print(args.input, args.output, args.test)
    	print('COMMANDS:')
    	print(list(input_file.split('\n')))
    	print('BYTECODE:')
    	print(*[hex(i) for i in bytecode])


    

if __name__ == "__main__":
    main()
