# import numpy as np
from matplotlib.colors import LogNorm
import matplotlib as mpl
from matplotlib.colors import ListedColormap

# Set up matplotlib
import matplotlib.pyplot as plt
from astropy.io import fits

# image path in laptop - Find by using terminal and then pwd
image_file = "/Users/DuarteCasaleiro/desktop/red_um461_3D_SLres_VBIN001.fits"

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

header_label_input = str(input("Header Label: "))
header_number_input = int(input("Header number: "))

print(hdu_list[0].header[header_label_input])
plt.imshow(image_data[header_number_input, :, :], origin='lower', cmap=color, interpolation='nearest', norm=LogNorm())
plt.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=color))
plt.show()