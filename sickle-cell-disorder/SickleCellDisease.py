# ***** start program *****         A program that translate a given DNA sequence to the corresponding amino acid using the SLC table. Please consult the README.txt file on the current directory for more information.
import math

def translate():        # a function for determining the DNA sequences stored in a textfile to translate to the corresponding amino acids

    mutate()        # mutate() function for editing a given DNA sequnce from a textfile

    print("\nNow displaying the Normal DNA after edit.")
    print("  -  "*30)
    fileNormal = open("normalDNA.txt", "r+", encoding = "utf-8-sig")
    seq = sequencer(fileNormal.read())      # get the DNA sequnce to operate on from a textfile
    fileNormal.close()
    data = amino(seq)       # get the corresponding amino acids formed from function amino(...)
    display(data)

    print("\nNow displaying the Mutated DNA after edit.")
    print("  -  "*30)
    fileMutated = open("mutatedDNA.txt", "r+", encoding = "utf-8-sig")
    seq = sequencer(fileMutated.read())         # get the DNA sequnce to operate on from a textfile
    fileMutated.close()
    data = amino(seq)       # get the corresponding amino acids formed from function amino(...)
    display(data)


def sequencer(sequence):        # this function formats a given sequnce in groups of 3's onto a list

        sequence = sequence.upper()       # capitalize user input in case the user enters lower cases
        listedSequence = list()
        hold = ""
    
        for char in sequence:
            hold += char        # a variable to hold the three base pairs currently working on
            if len(hold) == 3:
                listedSequence.append(hold)         # put the entered dna by the user into a list where each index has at most 3 characters
                sequence = sequence[3:]         # remove a dna sequence from then users input after its appended in the list
                hold = ""

            if len(sequence) < 3 and len(sequence) != 0:      # check if the remaining base-pair characters on the string sequence are less than 3
                if len(sequence) == 2:
                    hold = sequence + "X"       # concatinate an 'X' on the remnaining base-pair sequence
                    listedSequence.append(hold)     # add the invented base-pair into the list
                    sequence = ""         # remove a dna sequence from then users input after its appended in the list
                    
                    break       # force the program to break out of the for-loop
                else:
                    hold = sequence + "XX"      # concatinate an 'XX' on the remnaining base-pair sequence ifs just one letter
                    listedSequence.append(hold)         # add the invented base-pair into the list
                    sequence = ""        # remove a dna sequence from then users input after its appended in the list

                    break       # force the program to break out of the for-loop
    
        return listedSequence       # return the list of the grouped DNA sequence
    
    
def display(data):      # a function for printing results on to the print stream
    
        for slc in data[0]:         # print the SLC codons codes
            print(slc, end = "")
        
        finalSeq = ""
        for acid in data[1]:
            finalSeq += acid + ","      # have the list of amino acids as a single string

        print(" (representing: " + finalSeq[:len(finalSeq)-1] + ")")        # print the coresponding amino acids
    

def amino(sequence):        # a function to determine amino acids formed with given dna sequence

    slcCodons = list()
    aminoAcid = list()
    
    
    for dna in sequence:
        file = ""
        file = open("slc.txt", "r+")
        for line in file:
            line = line.replace("\n", "")       # remove newline placeholders from the read data from textfile
            line = line.split(":")      # split read data from textfile by ':'
            line[1] = line[1].replace(" ", "")      # remove swhitespaces around SLC read data from textfile
            line[2] = line[2].replace(" ", "")      # remove swhitespaces around amino base pairs read data from textfile
            nucleotides = line[2].split(",")        # create a list of base pairs
            

            if dna in nucleotides:      # search if dna sequence  appears in the nucleotides list
                slcCodons.append(line[1])       # store the SLC code to list
                aminoAcid.append(line[0])       # store amino acid name to list
                file = open("slc.txt", "r+")
                line = ""
                dna = ""
                break       # jump out of inner-most for-loop
            elif dna.find("X") != -1:       # operate on base pair that are not length = 3 initialy, but concatinated with 'X', and form base pairs that are not on the SLC range
                slcCodons.append("X")       # store the representing character for a non-existing base pair into the SLC-code list variable
                aminoAcid.append("Not in range")       # store amino acid name to list
                break
            elif line[1] == "Stop":     # this elif-statement handles base pairs that do not form existing amino acids
                slcCodons.append("X")       # store the SLC code to list
                aminoAcid.append("Non-existing")       # store amino acid name to list
                break
                
    file.close()

    return slcCodons, aminoAcid

def mutate():       # a function for editing a given textfile and write result to a different textfile

    file = open("DNA.txt", "r+", encoding = "utf-8-sig")
    line = file.read()      # store the DNA.txt content in the variable 'line'
    file.close()

    ind = line.find("a")
    if ind != -1:
            line = line[:ind] + "A" + line[ind:]      # replace the 'a' with 'A'
            fileNormal = open("normalDNA.txt", "w+")        # write to a new textfile called normalDNA.txt
            fileNormal.write(line)
            fileNormal.close()
            
            line = line[:ind] + "T" + line[ind:]      # replace the 'a' with 'T'
            fileMutated = open("mutatedDNA.txt", "w+")      # write to a new textfile called mutatedDNA.txt
            fileMutated.write(line)
            fileMutated.close()

def directTranslate():      # this function allows the user to enter a sequence of base-pairs they want to translate

    sequence = input("Enter DNA sequence you want translated: ")
    seq = sequencer(sequence)       # call the sequenceer(...) function format the DNA sequence in groups of three's
    data = amino(seq)        # call the amino(...) function which determines the amino acid formed per given sequnce
    display(data)       # the display function is for printing and formating result on to the print stream

def txtTranslate():         # a function responsible to hangle user-decision making when running program

    choice = input("Would you like to translate a sequence from input or from textfile (Input | Textfile): ")       # give the user the option to enter a sequence from keyboard input or read a sequence from a textfile

    if choice[0].lower() == "i":        # slice the users entry to avoid spelling mistakes that could prevent program from procceding
        directTranslate()       # call the directTranslate() function to execute
    elif choice[0].lower() == "t":
        translate()         # call the translate() function to execute
    else:
        print("Invalid input request. Try again.")

txtTranslate()


# ***** end program *****
