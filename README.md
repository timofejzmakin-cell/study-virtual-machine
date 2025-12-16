# LVM Learning-VM

## Команды языка:
1) write_const B C

Как это работает : registers[C] = B
```
write_const 38 10

```
2) read B C
Как это работает : registers[B] = memory[registers[C]]
```
read 12 8

```
3) write_value B C
Как это работает : memory[B] = registers[C]
```
write_value 10 6

```
4) rshift B C
Как это работает : registers[B] = ROR(B, memory[registers[C]])
```
rshift 38 11

```
