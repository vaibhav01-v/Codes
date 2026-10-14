dict={"name":"Marks",
      "vaibhav":92,
      "Rahul":82,
      "Sumit":78,
      "Kunal":93.5}

dict.update({"Sumit":82})
print(dict)
print(dict.keys(),dict.values())
print(dict.get("sumit"))

dict.pop("name")
print(dict.popitem())

print(dict.copy()) 
print(dict.__len__())
print(dict.clear())
print(dict)