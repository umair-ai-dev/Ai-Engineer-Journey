# Dictionary programs

# Program-01

# Store following word meaning in a python dict:
# -table: "a piece of furniture ,"list of facts and figures".
# -cat: "a small animal"

dictionary= {
    "cat" : " a small animal",
    "table" :  ["a piece of furniture", "list of facts and figures"]
}
print(dictionary)


# Program-02
# WAP to taking input of three subjects and store in list.

marks = {}
x = int(input("enter phy:"))
marks.update({"phy" : x})
x = int(input("enter math:"))
marks.update({"math" : x})
x = int(input("enter chem:"))
marks.update({"chem" : x})

print(marks)