import pyfiglet
import random

banner = "Happy New Year!"

fonts = ['standard', 'banner3', 'digital', 'slant', 'smscript']
colors = ['red', 'green', 'blue', 'magenta', 'cyan']

selected_font = random.choice(fonts)
selected_colors = random.choice(colors)

message = pyfiglet.figlet_format(banner, font='slant')

#print(f"\033[1; {colors.index(selected_colors)+31}m{message}\033[0m")
print(message)