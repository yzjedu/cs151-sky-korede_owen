#Initialize the constant variables
#Normal
normal_height = 46
normal_pm = 2
normal_par = 90

#Large
large_height = 70
large_pm = 1.9
large_par = 120

#Important variables that will be updated later in the program
speed = 0

#User Prompt and Opening message
print("Ski Jump Success Calculator!")
hillType = str(input("Enter the size of the hill you plan to ski on (please input either Large or Normal): "))

if(hillType.lower == "normal"):
    speed = int(input("Enter your speed: "))
