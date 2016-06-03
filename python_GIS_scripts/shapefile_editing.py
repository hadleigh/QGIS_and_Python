"""
trial for shape file editing using "Canada" folder, 
which is a polygon compliation of canadian provinces

Hadleigh Thompson
June 2016
"""

import shapefile as sf
r = sf.Reader("~/home/Hadleigh/Canada/Canada")
print(r)