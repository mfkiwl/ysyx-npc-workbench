import random
class IUT:
    def __init__(self, inst_pat, inst_name):
        self.instpat = inst_pat
        self.instname = inst_name
    def gentest(self):
        self.randinst = 0
        power = 31
        for i in range(len(self.instpat) - 1, -1, -1):
            if(self.instpat[i] == "0"):
                #print("Find 0, power is ", 31 - power)
                self.randinst = self.randinst
                power = power - 1
            elif(self.instpat[i] == "1"):
                #print("Find 1, power is ", 31 - power)
                self.randinst = self.randinst + 2 ** (31 - power)
                power = power - 1
            elif(self.instpat[i] == "?"):
                #print("Find ?, power is ", 31 - power)
                self.randinst = self.randinst + random.randint(0, 1) * 2 ** (31 - power)
                power = power - 1
            else:
                #print("Find  , power is ", 31 - power)
                self.randinst = self.randinst
                power = power
        return self.randinst
        #print('%#x'%self.randinst, ",")

rvnemu_dut = []
rvnemu_randinst = []

# Annotated instructions that may alter PC, handle/touch memory

rvnemu_dut.append(IUT("??????? ????? ????? ??? ????? 01101 11", "LUI"))
#rvnemu_dut.append(IUT("??????? ????? ????? ??? ????? 00101 11", "AUIPC"))
#rvnemu_dut.append(IUT("??????? ????? ????? ??? ????? 11011 11", "JAL"))
#rvnemu_dut.append(IUT("??????? ????? ????? 000 ????? 11001 11", "JALR"))
#rvnemu_dut.append(IUT("??????? ????? ????? 000 ????? 11000 11", "BEQ"))
#rvnemu_dut.append(IUT("??????? ????? ????? 001 ????? 11000 11", "BNE"))
#rvnemu_dut.append(IUT("??????? ????? ????? 100 ????? 11000 11", "BLT"))
#rvnemu_dut.append(IUT("??????? ????? ????? 101 ????? 11000 11", "BGE"))
#rvnemu_dut.append(IUT("??????? ????? ????? 110 ????? 11000 11", "BLTU"))
#rvnemu_dut.append(IUT("??????? ????? ????? 111 ????? 11000 11", "BGEU"))
#rvnemu_dut.append(IUT("??????? ????? ????? 000 ????? 00000 11", "LB"))
#rvnemu_dut.append(IUT("??????? ????? ????? 001 ????? 00000 11", "LH"))
#rvnemu_dut.append(IUT("??????? ????? ????? 010 ????? 00000 11", "LW"))
#rvnemu_dut.append(IUT("??????? ????? ????? 100 ????? 00000 11", "LBU"))
#rvnemu_dut.append(IUT("??????? ????? ????? 101 ????? 00000 11", "LHU"))
#rvnemu_dut.append(IUT("??????? ????? ????? 000 ????? 01000 11", "SB"))
#rvnemu_dut.append(IUT("??????? ????? ????? 001 ????? 01000 11", "SH"))
#rvnemu_dut.append(IUT("??????? ????? ????? 010 ????? 01000 11", "SW"))
rvnemu_dut.append(IUT("??????? ????? ????? 000 ????? 00100 11", "ADDI"))
rvnemu_dut.append(IUT("??????? ????? ????? 010 ????? 00100 11", "SLTI"))
rvnemu_dut.append(IUT("??????? ????? ????? 011 ????? 00100 11", "SLTIU"))
rvnemu_dut.append(IUT("??????? ????? ????? 100 ????? 00100 11", "XORI"))
rvnemu_dut.append(IUT("??????? ????? ????? 110 ????? 00100 11", "ORI"))
rvnemu_dut.append(IUT("??????? ????? ????? 111 ????? 00100 11", "ANDI"))
rvnemu_dut.append(IUT("000000? ????? ????? 001 ????? 00100 11", "SLLI"))
rvnemu_dut.append(IUT("000000? ????? ????? 101 ????? 00100 11", "SRLI"))
rvnemu_dut.append(IUT("010000? ????? ????? 101 ????? 00100 11", "SRAI"))
rvnemu_dut.append(IUT("0000000 ????? ????? 000 ????? 01100 11", "ADD"))
rvnemu_dut.append(IUT("0100000 ????? ????? 000 ????? 01100 11", "SUB"))
rvnemu_dut.append(IUT("0000000 ????? ????? 001 ????? 01100 11", "SLL"))
rvnemu_dut.append(IUT("0000000 ????? ????? 010 ????? 01100 11", "SLT"))
rvnemu_dut.append(IUT("0000000 ????? ????? 011 ????? 01100 11", "SLTU"))
rvnemu_dut.append(IUT("0000000 ????? ????? 100 ????? 01100 11", "XOR"))
rvnemu_dut.append(IUT("0000000 ????? ????? 101 ????? 01100 11", "SRL"))
rvnemu_dut.append(IUT("0100000 ????? ????? 101 ????? 01100 11", "SRA"))
rvnemu_dut.append(IUT("0000000 ????? ????? 110 ????? 01100 11", "OR"))
rvnemu_dut.append(IUT("0000000 ????? ????? 111 ????? 01100 11", "AND"))
#rvnemu_dut.append(IUT("0000000 00001 00000 000 00000 11100 11", "EBREAK"))
#rvnemu_dut.append(IUT("??????? ????? ????? 110 ????? 00000 11", "LWU"))
#rvnemu_dut.append(IUT("??????? ????? ????? 011 ????? 00000 11", "LD"))
#rvnemu_dut.append(IUT("??????? ????? ????? 011 ????? 01000 11", "SD"))
rvnemu_dut.append(IUT("??????? ????? ????? 000 ????? 00110 11", "ADDIW"))
rvnemu_dut.append(IUT("0000000 ????? ????? 001 ????? 00110 11", "SLLIW"))
rvnemu_dut.append(IUT("0000000 ????? ????? 101 ????? 00110 11", "SRLIW"))
rvnemu_dut.append(IUT("0100000 ????? ????? 101 ????? 00110 11", "SRAIW"))
rvnemu_dut.append(IUT("0000000 ????? ????? 000 ????? 01110 11", "ADDW"))
rvnemu_dut.append(IUT("0100000 ????? ????? 000 ????? 01110 11", "SUBW"))
rvnemu_dut.append(IUT("0000000 ????? ????? 001 ????? 01110 11", "SLLW"))
rvnemu_dut.append(IUT("0000000 ????? ????? 101 ????? 01110 11", "SRLW"))
rvnemu_dut.append(IUT("0100000 ????? ????? 101 ????? 01110 11", "SRAW"))
rvnemu_dut.append(IUT("0000001 ????? ????? 000 ????? 01100 11", "MUL"))
#rvnemu_dut.append(IUT("0000001 ????? ????? 001 ????? 01100 11", "MULH"))
#rvnemu_dut.append(IUT("0000001 ????? ????? 010 ????? 01100 11", "MULHSU"))
#rvnemu_dut.append(IUT("0000001 ????? ????? 011 ????? 01100 11", "MULHU"))
rvnemu_dut.append(IUT("0000001 ????? ????? 100 ????? 01100 11", "DIV"))
rvnemu_dut.append(IUT("0000001 ????? ????? 101 ????? 01100 11", "DIVU"))
rvnemu_dut.append(IUT("0000001 ????? ????? 110 ????? 01100 11", "REM"))
rvnemu_dut.append(IUT("0000001 ????? ????? 111 ????? 01100 11", "REMU"))
rvnemu_dut.append(IUT("0000001 ????? ????? 000 ????? 01110 11", "MULW"))
rvnemu_dut.append(IUT("0000001 ????? ????? 100 ????? 01110 11", "DIVW"))
rvnemu_dut.append(IUT("0000001 ????? ????? 101 ????? 01110 11", "DIVUW"))
rvnemu_dut.append(IUT("0000001 ????? ????? 110 ????? 01110 11", "REMW"))
rvnemu_dut.append(IUT("0000001 ????? ????? 111 ????? 01110 11", "REMUW"))

for test_number in range(0, 1048576, 1):
    rand_inst = rvnemu_dut[random.randint(0, len(rvnemu_dut) - 1)].gentest()
    print('%#x'%rand_inst)
    rvnemu_randinst.append(rand_inst)

print()
print()
print(rvnemu_randinst)