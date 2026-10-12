# Week 1.2, Session 2: Task 6



oper = int(input("Enter the machine's operational status (0 or 1): "))

if oper == 1:
    temp = int(input("Enter the machine's temperature in degrees Celsius: "))

    if temp > 80: 
        print("The temperature is too high! Shut down the machine!!!!")
    elif temp < 50:
        print("Machine temperature is low, no action needed.")
    else:
        print("Machine temperature is within safe limits.")


    psi = int(input("Enter the machine's pressure in PSI: "))
  
    if psi > 100: 
        print("The pressure is too high! Maintenance required!!!!")
    elif psi < 70:
        print("Machine pressure is low, no action needed.")
    else:
        print("Machine pressure is stable.")


elif oper == 0:
      print("Machine is shut down. No immediate action necessary. ")


with open("machine_log.txt", 'a') as file:
    file.write("Temperature: {temp}