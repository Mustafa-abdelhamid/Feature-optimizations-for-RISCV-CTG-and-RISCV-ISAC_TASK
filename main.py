#############################################################
# Applicant name : Mostafa mohamed
# Applicant Gmail: moostafamohamedd@gmail.com
# LFX profile link : https://mentorship.lfx.linuxfoundation.org/mentee/4e03d9b8-a755-4d1d-86fd-6b27b8453d02
############################################################# 
# main.py
import sys

################## FUNCTIONS DEFINITIONS #############################
def get_xlen(riscv_string):
	if ('32' in riscv_string):
		XLEN='32'
	elif ('64' in riscv_string):
		XLEN='64'
	else:
		XLEN='128'
	return(XLEN)
#####################################################################
if __name__ == "__main__":
	assert len(sys.argv) == 2 , "Only one input argument is required"
	riscv_string=sys.argv[1] 
####################################################################
	XLEN=get_xlen(riscv_string)
	print('XLEN :',XLEN)
	extensions=riscv_string.split(str(XLEN))[1::]
	#print('supported extensions: ',extensions)    
# Check if riscv_string has undescoe between Extensions
	underscores_splits=str(extensions).split('_')
	supported_isa=[]
	if(len(underscores_splits)==1): # doesn't contain underscores
		print("DOESN'T CONTAIN UNDERSCORES")
		for x in underscores_splits[0]:
			supported_isa.append(x)
		supported_isa=supported_isa[2:-2]
	else:
    		print("CONTAINS UNDERSCORES")
    		for x in underscores_splits:
    			supported_isa.append(x)
    		supported_isa[0]=supported_isa[0][2]
    		supported_isa[-1]=supported_isa[-1][0]
		
	
	print(supported_isa)
	
	
	f = open("cgf.yaml", "w")
	f.close()	
	f = open("cgf.yaml", "a")
	##XLEN RELATED CHECKS ( BASE FIELD )
	f.write("# XLEN RELATED CHECKS \n")
	if (int(XLEN)==32): 
		f.write("#for XLEN= 32 ** Check base field = 1 \n")
		f.write("misa && 0x40000000 == 0x40000000 \n")
	if(int(XLEN)==64):
		f.write("#for XLEN= 64 ** Check base field = 2 \n")
		f.write("misa && 0x80000000 == 0x80000000 \n")
	if(int(XLEN)==128):
		f.write("#for XLEN= 128 **Check base field = 3 \n")
		f.write("misa && 0xc0000000 == 0xc0000000 \n")
	f.write("######################################################### \n #Base integer RELATED CHECKS \n")
	if (('I' in supported_isa[0]) or ('i' in supported_isa[1::])): 
		f.write("#for integer base  Check bit at index 8  = 1 \n")
		f.write("misa && 0x00000100 == 0x00000100 \n")
	if (('E' in supported_isa[0]) or ('e' in supported_isa[1::]) ):
		f.write("#for embedded integer base Check bit at index 4  = 1 \n")
		f.write("misa && 0x00000010 == 0x00000010 \n")
	f.write("######################################################### \n #RATIFIED EXTENSIONS RELATED CHECKS \n")
	if ( ('M' in supported_isa[1::]) or ('m' in supported_isa[1::]) ): 
		f.write("#for M extension  Check bit at index 12  = 1 \n")
		f.write("misa && 0x00001000 == 0x00001000 \n")
	if ( ('F' in supported_isa[1::]) or ('f' in supported_isa[1::])):
		f.write("#for F extension  Check bit at index 5  = 1 \n")
		f.write("misa && 0x00000020 == 0x00000020 \n")
	if ( ('D' in supported_isa[1::]) or ('d' in supported_isa[1::])):
		f.write("#for D extension  Check bit at index 3  = 1 \n")
		f.write("misa && 0x00000008 == 0x00000008 \n")
		f.write("#for D extension  F is implied Check bit at index 5  = 1 \n")
		f.write("misa && 0x00000020 == 0x00000020 \n")
	if ( ('Q' in supported_isa[1::]) or ('q' in supported_isa[1::])):
		f.write("#for Q extension  Check bit at index 16  = 1 \n")
		f.write("misa && 0x00010000 == 0x00010000 \n")
		f.write("#for Q extension  F and D are implied  \n")
		f.write("misa && 0x00000028 == 0x00000028 \n")
	if (('C' in supported_isa[1::]) or ('c' in supported_isa[1::])):
		f.write("#for C extension  Check bit at index 2  = 1 \n")
		f.write("misa && 0x00000004 == 0x00000004 \n")
	f.close()
	
	
    
