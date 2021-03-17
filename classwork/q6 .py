#solve each of the following problems using python scripts. make sure you use appropriate variable names and comments.
#when there is a final answerhave python print it to the screen.
# A person's body mass index (BMI) IS defined as:
#    BMI=mass in kg /(height in m)**2
mass = float(input("enter the mass of person in kg: "))
height =float(input("enter the height of a person in meter: "))
BMI = (mass/(height*height))
print(f"the BMI index of a person is {BMI}")