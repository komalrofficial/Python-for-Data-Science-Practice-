
#check wether the character is upper case or lower case
chr=str(input("enter a alphabet:"));
def upper_case_or_lower_case(chr):
    if chr >= "A" and chr <= "Z" :
       print("alphabet is upper case");
    elif chr >= "a" and chr <= "z":
       print("alphabet is lower case");
    else:
       print("not a alphabet");
upper_case_or_lower_case(chr)