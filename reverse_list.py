#Kai Geller
#GitHub Username: KaiGeller
#5/11/2022
#The code in this project will take a list of values and reverse the order of the list
def reverse_list(vals):
    """This function will take a list of values and reverse it"""
    store_vals=[]
    for i in range(len(vals)):
        store_vals.append(vals[len(vals)-i-1])
    for i in range(len(vals)):
        vals[i] = store_vals[i]
