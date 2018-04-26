#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Python-Fuを使用して[DIR]内のxcfファイルを[DIR/out/*.png]にエクスポートするプラグイン
'''
from gimpfu import *
import itertools, math, os, glob

def do_posout_batch(dirname):

  if os.path.exists(dirname):
    fnames = glob.glob(dirname+"/*.xcf")
   
    for fname in fnames:
      fbasename = os.path.basename(fname).split(".")[0]
      # pdb.gimp_message("Open: %s" %(fbasename))
      new_filename = dirname+"/out/" + fbasename + ".png"
      img = pdb.gimp_file_load(fname, ' ')
      drawable = pdb.gimp_image_merge_visible_layers(img,0)
      pdb.file_png_save_defaults(img, drawable, new_filename, new_filename)
      del(img)
      del(drawable)



    pdb.gimp_message("Finished writing to: %s" %(new_filename))
  else:
    pdb.gimp_message("No such directory: %s" %(dirname))

register(
  "Batch_Export",
  "Batch Export as png",
  "Batch Export as png",
  "Hiroyasu Inoko",
  "Hiroyasu Inoko",
  "2018",
  "Batch Export",
  "*",
  [(PF_DIRNAME, "targetDirectory",  "Target Directory", ".")],
  [],
  do_posout_batch, menu="<Image>/File")

main()
