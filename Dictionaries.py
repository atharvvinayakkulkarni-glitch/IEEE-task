#This my list of location,branch and cutoff marks
cutoff=[("pilani","CS",327), ("pilani","Eco",271), ("pilani","chemical",239), ("goa","CS",301), ("goa","Eco",245),("goa","Chemical",213),("Hydrabad","CS",298),("Hydrabaad","Eco",222),("Hydrabad","Chemical",198)]
# my dictionary which stores the final result
result={}
for loc, branch, marks in cutoff:
  if(loc not in result):
    #if loc key wasnt made yet for a certain campus itll make one
    result[loc]= {}
    #assigning marks as value to loc and branch key pair
  result[loc][branch] = marks
print(result)
