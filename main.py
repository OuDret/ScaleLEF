import os

input_lef = "SK_stdcell.lef"
output_lef = "out.lef"
scale_factor = 0.1

os.remove(output_lef)
with open(input_lef, 'r') as file:
    for line in file:
        words=line.split(" ")

        if words[0] != "VERSION":
            line = ""
            for word in words:
                if (len(word) > 0):
                    if word[0].isdigit():
                        word = str(round(float(word)*scale_factor,4))
                line += word + " "
        
        with open(output_lef, 'a') as f:
            # Write to the file
            f.write(line)