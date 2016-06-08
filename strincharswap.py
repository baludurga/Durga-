x = "our string to be swapped"
result_string = ""
index = 0;
for c in x:
    if(index%2 == 0):
        result_string += c.lower()
    else:
        result_string += c.upper()
    index+=1
print(result_string)
