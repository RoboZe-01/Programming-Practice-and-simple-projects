




# this is a problem about removing similar letter from the string 


def remove_dupli ():
    words = input(" Enter the word for duplicated to be removed : ")
    for char in words :
        without_dupli = ""
        if char not in without_dupli :
            without_dupli+=char
    return without_dupli


print(remove_dupli())   