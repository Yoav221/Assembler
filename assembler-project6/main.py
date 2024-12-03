from assembler import Assembler

input_path = "asm_files/Pong.asm"
output_path = "hack_files/" + input_path.split("/")[-1].split(".")[0] + ".hack"

assembler = Assembler(input_file=input_path, output_file=output_path)
assembler.translate()
