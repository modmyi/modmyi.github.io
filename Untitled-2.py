input_string = "cn.tinyapps.location360pro cn.tinyapps.location360proex cn.tinyapps.location360 cn.tinyapps.XGPSPro cn.tinyapps.XGPSLite cn.tinyapps.XGPSFree"
output_string = ""

i = 0
while i < len(input_string):
    # If the character is not a space, add it to the output string
    if input_string[i] != " ":
        output_string += input_string[i]
        i += 1
    else:
        # If the next character is a letter or an opening parenthesis, and the previous character is not a comma, add a comma
        if i + 1 < len(input_string) and (input_string[i + 1].isalpha() or input_string[i + 1] == "(") and (i == 0 or input_string[i - 1] != ","):
            output_string += ","
        i += 1

print(output_string)

import re

input_string = output_string
output_string = re.sub(r',(?=\([^)]+\))', '', input_string)

print(output_string)