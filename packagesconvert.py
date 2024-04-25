packages = open("./Packages",'r', encoding='utf-8').read()
import bz2
newcontent = bz2.compress(packages.encode())
f = open("Packages.bz2", "wb")
f.write(newcontent)
f.close()

import gzip

with open("./Packages", 'rb') as orig_file:
    with gzip.open("./Packages.gz", 'wb') as zipped_file:
        zipped_file.writelines(orig_file)

print('Converted Packages to Packages.bz2 successfully.')
from time import sleep
