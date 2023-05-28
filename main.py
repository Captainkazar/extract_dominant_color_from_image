from colorthief import ColorThief
import matplotlib.pyplot as plt

ct = ColorThief("shirt3.jpg")
dominant_color = ct.get_color(quality=1)

plt.imshow([[dominant_color]])
plt.show()

all_colors = ct.get_palette(color_count=5)
plt.imshow([[all_colors[i] for i in range(5)]])
plt.show()
