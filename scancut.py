#! /usr/bin/env python
from sys import argv
from PIL import Image,ImageChops
import numpy as np
from optparse import OptionParser

def get_options():
    parser = OptionParser()
    # string options
    parser.add_option("-i", "--infile",    dest="infile",   type="string")
    parser.add_option("-o", "--outfile",   dest="outfile",  type="string")
    # flags
    parser.add_option("-p", "--preview",   dest="preview",   action="store_true", default=False)
    parser.add_option("-v", "--verbose",   dest="verbose",   action="store_true", default=False)
    # create the options object to be returned
    options, args = parser.parse_args()
    # before returning, some sanity checks
    if (options.indir  is None):   raise Exception("The input file must be specified, see --help")
    if (options.outdir is None):   options.outdir = "cutted_" + options.indir
    # 
    return options

def trim_box(im):
    nim = np.array(im)
    bim = (np.mean(nim, axis=2) < 190)
    # top-bottom
    nz = np.nonzero(np.mean(bim, axis=1) > 0.1)
    y1 = nz[0][0] + 2
    y2 = nz[0][-1] - 2
    # left-right
    nz = np.nonzero(np.mean(bim, axis=0) > 0.1)
    x1 = nz[0][0] + 2
    x2 = nz[0][-1] - 2
    print("Found image content in the rectangle from (%d, %d) to (%d, %d) " % (x1,y1,x2,y2))
    return x1, y1, x2, y2
 
    
        


if __name__ == "__main__":
    in_name = argv[1]
    out_name = argv[2]
    im = Image.open(in_name)
    im.crop(trim_box(im)).save(out_name)

    
