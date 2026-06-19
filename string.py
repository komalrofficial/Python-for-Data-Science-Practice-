# string methods
str=("electrical engineer")

#upper()
print(str.upper())
# lower()
print(str.lower())

#capitalize()
print(str.capitalize())

#title
print(str.title())

#strip
str="   string   "
print(str.strip())
print(str.lstrip())
print(str.rstrip())

#replace
str=("electrical engineer")
print(str.replace("cal","eer"))

#split
str="i am a electrical engineer"
print(str.split())

str="i_am_a_electrical_engineer"
print(str.split())

#join
str="i am a electrical engineer"
print(str.join([""," with 7+ experience"]))

#find
print(str.find("m"))
print(str.find("m")+1)
#index
print(str.index("m"))
print(str.index("m")+1)
print(str.startswith("i"))
print(str.endswith("r"))
#count
print(str.count("am",2))
print(len(str))
str="89hjgt"
print(str.isalnum())


#reverse the given string
str="computer"
print(str[::-1])

#reverse individual string
str="software developer"
print(str.split())

print(str[::-1])












