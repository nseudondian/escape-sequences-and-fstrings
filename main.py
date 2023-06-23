# Newline character (\n) : starts a new line. 

print("hello \n world")

print("hello \n everyone! \n welcome to Learn-In ")
# Tab character (\t): The tab character, when used within a string,  creates horizontal whitespace or indentation.

print("Name: \t NSE")
print("Age: \t 18")
print("City: \t Abuja")


# Double quote (\"): used to include a double quote within a string that is already enclosed in double quotes. 

greeting = "Learn-in say \"hello\" " 
print(greeting)


#  single quote character - (\'):  used include a single quote within a string that is already enclosed in single quotes

message = 'He said, \'Hello!\' ' 
print(message)

message = 'He said, "Hello!" ' 
print(message)

message = "He said, 'Hello!' "
print(message)

message = "Learn-In is NSE's YouTube channel"
print(message)








# Backslash character: \\

path = "C:\\Users\\Username\\Documents"
print(path)

# \t, \n, \"





#  format() method is used to format strings by substituting placeholders with corresponding values


name = "NSE"
age = 18

greeting = "Hello, {}. You are {} years old.".format(name, age)

greeting = "Hello, {1}. You are {0} years old."

formatted_greeting = greeting.format(name, age)

print(formatted_greeting)

print(greeting.format(name, age))





# You can also specify the positions of the placeholders using indices within the format() method:

name = "NSE"
age = 12
greeting = "Hello, {0}. You are {1} years old.".format(name, age)


#  Literal String Interpolation or F-strings (f"")

# str.format()

name = "NSE"
age = 18
greeting = f"Hello, {name}! You are {age} years old."
print(greeting)
x = 10
y = 5
result = f"The sum of {x} and {y} is {x + y}. The product is {x * y}."
print(result)


