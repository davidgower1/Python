#This script will calculate the length of antennas
print("What is the length of a Sky Loop antenna for 80 meters?")
print("Resonant Frequency is 3.5 Mhz")
print("Total length of the Loop is: ", round(float(1005) / float(3.5)) ,"  For uninsolated wire")
print("If the wire is insolated the total length is:  ", round(float(1005) / float(3.5) * float(.96)) )
print("The length is differenet to compensate for the skin loss of the insolation")
