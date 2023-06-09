#Colored Output in Python
import simple_colors
text = "Welcome to Python"

# Colored text
colored = simple_colors.blue(text)
print('Colored:', colored)

# Colored and Bold text
bold_colored = simple_colors.green(text,'bold')
print('BOLD:', bold_colored)

# Colored, Bold and Underlined text
attributes = ['bold','underlined']
bold_underlined = simple_colors.red(text, attributes)
print('BOLD and Underlined: ', bold_underlined)
