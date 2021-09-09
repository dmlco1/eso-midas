import numpy as np
from matplotlib import colors
from matplotlib._cm_listed import cmaps
from matplotlib.colors import LogNorm
import matplotlib as mpl
from collections import OrderedDict
from matplotlib.colors import ListedColormap

# Set up matplotlib
import matplotlib.pyplot as plt
from astropy.io import fits

cmaps = OrderedDict()


# Only consider a segment of the colormap
def truncate_colormap(cmap, minval=0.0, maxval=1.0, n=100):
    new_cmap = colors.LinearSegmentedColormap.from_list(
        'trunc({n},{a:.2f},{b:.2f})'.format(n=cmap.name, a=minval, b=maxval),
        cmap(np.linspace(minval, maxval, n)))
    return new_cmap


# choose the colormap
cmap = plt.get_cmap('gist_rainbow')

# set the interval for the segment of the colormap
new_cmap = truncate_colormap(cmap, 0.20, 1.0)
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

norm = mpl.colors.Normalize(vmin=0.0, vmax=1.0)

# header_label_input = str(input("Header Label: "))
# header_number_input = int(input("Header number: "))

# allow subplots
fig, ax = plt.subplots(constrained_layout=True)

print(hdu_list[0].header[0])
# cmap=new_cmap if we want to consider a segment of the colormap
# color if we want a default colormap
h_flux = ax.imshow(image_data[50, :, :], origin='lower', cmap=new_cmap, interpolation='nearest',
                   norm=LogNorm())
h_flux_color_bar = plt.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=cmap))
# h_flux_color_bar_legend = plt.legend(handles=[h_flux], loc='upper right')
# Image contour

# stellar_continuum = ax.contour(image_data[0, :, :], colors='black', alpha=0.7)


# plt.contour(stellar_continuum, 200, cmap='RdGy')

# stellar_continuum = ax.contour(image_data[0, :, :], colors='black', alpha=0.7)
# stellar_continuum_color_bar = plt.colorbar(stellar_continuum, shrink=0.25)
# ax.clabel(stellar_continuum, inline=True, fontsize=10)
plt.title("Halhpa Emisson Map")

plt.show()
