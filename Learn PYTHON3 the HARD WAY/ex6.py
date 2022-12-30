type_of_people = 10              #设置变量
x =f"There are {type_of_people} types of people."  #x 赋值。 

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}"

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))   #另一种方式{}字符串赋值

w = "This is the left side of ..."
e ="a string with a right side."

print(w + e)