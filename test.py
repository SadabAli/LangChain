line = 'HumanMessage(content="Hello World!")'
if line.startswith("HumanMessage"):
    content = line[len('HumanMessage(content="'):-2]
    print(content)  # Output: Hello World!
