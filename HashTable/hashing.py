import pandas as pd
dictionary = {"Employee":{"dave":{'id':1,'branch':'backend','gender':',male'}},
              "dave":{'id':2,'branch':'frontend','gender':',female'}} 


dictionar=pd.DataFrame(dictionary['Employee'])
print(dictionar)
