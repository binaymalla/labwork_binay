# Write a Python program to convert temperatures to and from celsius, fahrenheit.
# Celsius to Fahrenheit	° F = 9/5 ( ° C) + 32
# Fahrenheit to Celsius	° C = 5/9 (° F - 32)
# Celsius to Kelvin	K = ° C + 273
# Kelvin to Celsius	° C = K - 273
# Fahrenheit to Kelvin	K = 5/9 (° F - 32) + 273


f  = float(input ("enter a temperature in celsius\t"))
c = float(input ("enter a temperature in farenheit\t"))
k = float (input ("enter a temperature in kelvin\t"))
print("celsius to another")
CF = (9/5)*(c+32)
CK = (c+273)
print ("CF=\t",CF)
print ("CK=\t",CK)

print ("farenheit to others")
FC = (5/9)*(f-32)
FK = (5/9)*(f-32)+273
print ("FC=\t",FC)
print ("FK=\t",FK)


print ("Now Kelvin to Others")
KC = k-273
KF = k - (273.15) * (9/5) + 32

print ("KC=\t",KC)
print ("KF=\t",KF)