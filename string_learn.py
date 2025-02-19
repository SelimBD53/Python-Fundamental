# single or double invated comma soho likha or string print korar tackique.

# statement1 = "I Love 'Python'"
# print(statement1)
# statement = "I Love \'Python\'"
# print(statement)

# String Operations
# statement1 = "i love python"
# statement2 = "java and Python"
# print(statement1.lower())
# print(statement1.upper())
# print(statement1.capitalize())       # I love python
# print(statement1.title())            # I Love Python
# print(statement2.count('a'))            
# print(statement2.count('a', 0, 4))            
# print(statement2.replace('a','-'))            
# print(statement2.split()) 

# string concat
# concate = statement1 + " " +statement2
# print(concate)  

# concat = " ".join((statement1, statement2))
# print(concat)         

# y=["Nahid","Zia"]
# r=["Selim","Zia","Naim"]

# s=list(set(y+r))
# print(s)

g=["Nahid","Zia"]
h=["Selim","Zia"]
for value in h:
    if value not in g:
        g.append(value)
print(g)  
    
