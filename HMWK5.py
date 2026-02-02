hi = "Hello"
who = "World"
print(hi + " " + who)
#Hello World
print(hi + who[:3] + who[4:])
print(hi + " " + who + who[:3] + who[4:])
#HelloWorld
#>>> hi + " " + who[:3] + who[4:]
#Hello World
print((hi + who).upper())
#HELLOWORLD
print("racecar"[::-1])
#racecar
print((3 * (hi + " ") + 5 * (who + ",")).replace(","," ").split(" "))
print(['Hello', 'Hello', 'Hello', 'World', 'World', 'World', 'World', 'World', ''])
print("Yo, banana boy"[::-1].replace(" ,", " ").replace(" ","").lower())
#Yo, banana boy!
print("A nut for a jar of tuna."[::-1].replace(" ,", " ").replace(" ","").replace(".","").lower())
# #“A nut for a jar of tuna.”