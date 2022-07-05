#!/usr/bin/env python
#
# Example code for calling the analysis functions.

from SEM_Image_Analysis_Milled_Line_Detect import sem_image_analysis_milled_line_detect
from SEM_Image_Analysis_Depo_Line_Detect import sem_image_analysis_depo_line_detect


# Deposition example

filename = "10kvwdep_068.tif"

sem_image_analysis_depo_line_detect(verbose=True,
                                    filename=filename,         # filename
                                    img_width=7.5,             # Real image width in microns
                                    crop_top=50,               # pixels to crop from the top
                                    crop_bottom=150,           # pixels to crop from the bottom
                                    crop_left=100,             # pixels to crop from the left
                                    crop_right=10,             # pixels to crop from the right
                                    total_width_cols=1500,     # image width about centre to use for horizontal line
                                    peak_width_max = 80,       # peak sharpness filter 
                                    peak_dist_max = 1000)      # max distance of peaks from crop lines



# Milled example
filename = "40Cup.tif"

sem_image_analysis_milled_line_detect(verbose=True,
                                      filename=filename,       # filename
                                      img_width=17.0,          # Real image width in microns
                                      crop_top=400,            # pixels to crop from the top
                                      crop_bottom=500,         # pixels to crop from the bottom
                                      crop_left=500,           # pixels to crop from the left
                                      crop_right=100,          # pixels to crop from the right
                                      total_width_cols=1500,   # image width about centre to use for horizontal line
                                      peak_width_max = 400,     # peak sharpness filter 
                                      peak_dist_max = 1000)    # max distance of peaks from crop lines
                                      
                                     

