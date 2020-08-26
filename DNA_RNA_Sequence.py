'''
Adenine (A), Thymine (T), Cytosine (C), Guanine (G), Uracil (U)
 
DNA complementary base pairing rule
 A -> T
 C -> G
 G -> C
 T -> A

 RNA complementary base pairing rule
 A -> U
 C -> G
 G -> C
 T -> A
 '''


import tkinter
import tkinter.filedialog  
# Hides the TK interface main windows      
root = tkinter.Tk()
root.attributes('-alpha',0.3)
root.withdraw

temp_DNA = ''           # One line of Template DNA Sequence
comp_RNA = ''           # One line of Complementary RNA Sequence
covid_cDNA = ''         # Complete coronavirus cDNA
covid_RNA = ''          # Complete coronavirus RNA


# Using 'w' in the mode option open file for write, and create it if not exists
output_file = open('C:\\Users\\Romit\\Downloads\\DNA_RNA_Sequence_Python\\covid_sequence.txt', 'w')

file_path = tkinter.filedialog.askopenfilename(parent=root)
# Destroy the TK interface after we finish using it.
root.destroy()

# The 'r' option to open the file for read.
with open(file_path,'r') as input_data:
    header = input_data.readline().strip()    
    output_file.write(header + ' RNA sequence')
    for line in input_data:
        temp_DNA = line.strip()
        covid_cDNA = covid_cDNA + temp_DNA 
        comp_RNA = ""
        for base in temp_DNA:
            if base == "A":
                  comp_RNA = comp_RNA + 'U'
            elif base == "C":
                comp_RNA = comp_RNA + 'G'
            elif base == "G":
                comp_RNA = comp_RNA + 'C'
            elif base == "T":
                comp_RNA = comp_RNA + 'A'
            else:
                comp_RNA = comp_RNA + '?'
                
        covid_RNA = covid_RNA + comp_RNA
		# The "\n" will add carriage retrun before each line.
        output_file.write("\n" + comp_RNA)
		# Using flush() to force Python to write to the file.
        output_file.flush()
        print(temp_DNA)        
        print(comp_RNA)
        print("===================================================")

       
input_data.close()
output_file.close()

