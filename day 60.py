
import json
WeekDay = ("Satrday","Sunday","Monday","Tueday","Wedsday","Thuday","Friday")
print('The Day of Week  : ',WeekDay)

convert = json.dumps(WeekDay)
print("String:",convert)


import re
X = "date is the new oil"
seachData = re.search("data",X)
if seachData:
   print("There is MATCH: ",seachData)
else:
   print("Not Found!")
  
