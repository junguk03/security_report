text = "flag.txt"

result = ""
for i in text:
    result += f"chr({ord(i)})+"

print(f"open({result}).read()")
