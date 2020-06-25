import json
from difflib import get_close_matches

data = json.load(open("Application1_Dictionary/data.json"))
def meaning (w):
    #w.lower() - this is to show that w.lower() needs to be stored in w 
    #print (w)
    w = w.lower()
    #if w == data.keys():
    if w in data.keys():
        #a1 = data[w]
        #print (*a, sep = '\n')
        return data[w]

    elif w.title() in data.keys():
        return data[w.title()]

    elif w.upper() in data.keys():
        return data[w.upper()]
   
    elif len(get_close_matches(w, data.keys())) > 0:
        user = input (f"Did you mean {get_close_matches(w, data.keys())[0]}? \n Y or N: ")
        
        if user.upper() == "Y":
            #a2 = data[get_close_matches(w, data.keys())[0]]
            #print (*a2, sep = '\n')
            return data[get_close_matches(w, data.keys())[0]]

        
        elif len(get_close_matches(w, data.keys())) > 1:
            user2 = input (f"Did you mean {get_close_matches(w, data.keys())[1]}? \n Y or N: ")
    
            if user2.upper() == "Y":
                #a3 = data[get_close_matches(w, data.keys())[1]]
                #print (*a3, sep = '\n')
                return data[get_close_matches(w, data.keys())[1]]
            else:
                return("We did not understand your query, please try again.")
                  
    else:
        return ("Word did not found")


word = input ("Enter a word whose meaning you want to find: ")
output = meaning (word)

#if type (output) == list:
if isinstance (output, list):
    for i in output:
        print (i)
else:
    print (output)