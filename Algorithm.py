# import numpy as np
from matplotlib.colors import LogNorm
import matplotlib as mpl
from matplotlib.colors import ListedColormap

# Set up matplotlib
import matplotlib.pyplot as plt
from astropy.io import fits

# image path in laptop - Find by using terminal and then pwd
image_file = "/Users/DuarteCasaleiro/desktop/red_n1705_3D_SLres_VBIN014.fits"

# open fits image using hdu
hdu_list = fits.open(image_file)
hdu_list.info()

# Image information. Located in the PRIMARY block
# header 1 from eso-midas = header 32 from astropy
image_data = hdu_list[0].data

print(repr(hdu_list[0].header))

# Close the FITS image
# We have everything we need in the variable image_data
hdu_list.close()

# cmap='YlGnBu'
# .reversed() if we want to invert color scheme
color = plt.cm.get_cmap('gist_rainbow')

# cmap = mpl.cm.turbo.reversed()

norm = mpl.colors.Normalize(vmin=-9999.0, vmax=46412.2)

running = True


def study(number_midas):
    plt.imshow(image_data[number_midas, :, :], origin='lower', cmap="Reds", interpolation='nearest', norm=LogNorm())
    plt.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=color))
    plt.show()


while running:
    print("-> Image: ", image_file)
    # menu
    print("\n", "1: Flux",
          "\n", "2: Stellar Velocity",
          "\n", "3: Ionized Gas",
          "\n", "4: Other"
          "\n\n", "5: Quit")
    # input
    option = int(input("Enter your option: "))

    # check selected option
    if 1 > option or option > 5:
        print("Invalid option")
        continue
    elif option == 1:
        study(50)
        running = False

    elif option == 2:
        study(6)
        running = False

    elif option == 3:
        study(72)
        running = False

    elif option == 4:
        option_number_midas = int(input("Enter the header number: "))
        study(option_number_midas)
        running = False

    elif option == 5:
        running = False