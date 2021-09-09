import numpy as np
from matplotlib import colors
from matplotlib.colors import LogNorm
import matplotlib as mpl
from matplotlib.colors import ListedColormap

# Set up matplotlib
import matplotlib.pyplot as plt
from astropy.io import fits


# Only consider a segment of the colormap
def truncate_colormap(cmap, minval=0.0, maxval=1.0, n=100):
    new_cmap = colors.LinearSegmentedColormap.from_list(
        'trunc({n},{a:.2f},{b:.2f})'.format(n=cmap.name, a=minval, b=maxval),
        cmap(np.linspace(minval, maxval, n)))
    return new_cmap


# choose the colormap
cmap = plt.get_cmap('hot').reversed()

# set the interval for the segment of the colormap
new_cmap = truncate_colormap(cmap, 0.15, 1.0)
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
color = plt.cm.get_cmap('hot').reversed()
# cmap = mpl.cm.turbo.reversed()

norm = mpl.colors.Normalize(vmin=0.0, vmax=10.0)

# allow subplots
fig, ax = plt.subplots(constrained_layout=True)

# cmap=new_cmap if we want to consider a segment of the colormap
# color if we want a default colormap
h_flux = ax.imshow(image_data[50, :, :], origin='lower', cmap=color, interpolation='nearest',
                   norm=LogNorm())
h_flux_color_bar = plt.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=color))

# Image contour
stellar_continuum = ax.contour(image_data[0, :, :], levels=400, colors='gray', alpha=0.50)

plt.title("Halpha flux w/ contour of stellar continuum")

plt.show()

# other
# stellar_continuum = ax.contour(image_data[0, :, :], colors='black', alpha=0.7)
# stellar_continuum_color_bar = plt.colorbar(stellar_continuum, shrink=0.25)
# ax.clabel(stellar_continuum, inline=True, fontsize=10)
