cutoff=[("pilani","CS",327), ("pilani","Eco",271), ("pilani","chemical",239), ("goa","CS",301), ("goa","Eco",245),("goa","Chemical",213),("Hydrabad","CS",298),("Hydrabaad","Eco",222),("Hydrabad","Chemical",198)]
result={}
for loc, branch, marks in cutoff:
  if(loc not in result):
    result[loc]= {}
  result[loc][branch] = marks
print(result)
