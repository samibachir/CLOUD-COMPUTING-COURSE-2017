from random import randint

bound = 20
random_number = randint(1,bound) # nombre choisi par l'ordinateur
number  = 0 # nombre proposé par le joueur
print("choose a number between 1 and",bound)

while number != random_number :
     number = int(input("Your number : "))
     if number < random_number:
         print("Too low")
     elif number > random_number:
         print("Too high")
     else:
         print("Bravo ! Vous avez trouvé",random_number)