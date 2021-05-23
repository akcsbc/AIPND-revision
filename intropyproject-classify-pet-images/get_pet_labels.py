#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Szymon Strzoda
# DATE CREATED: 22.05.2021  
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir
import os.path
import re 

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """

    # Defines mask for image files we take into account 
    image_file_re = re.compile(".*\.(jpg)$")
    # Creates list of image files in directory
    image_files = [f for f in listdir(image_dir) if os.path.isfile(os.path.join(image_dir,f)) and image_file_re.match(f)]  
    # Creates list of labels 
    pet_labels = map(
      #create table of all words in the file name, join using space and remove extension (last word in the list)
      lambda i: [' '.join(re.findall('[a-zA-Z]+',i.lower())[:-1])],
      image_files)
    # Creates zip dict from two list  
    results = dict(zip(image_files, pet_labels))

    return results