from PIL import Image
import math
import os

def slice_and_dice(img_path, output_dir, horizontal_size, vertical_size):
  #set statistics
  total_h_slices = 0
  total_v_slices = 0
  total_s_slices = 0

  filename = os.path.split(img_path)[1]
  img = Image.open(img_path) 
  
  #get image size, and the starting points
  h_width, h_height = img.size 
  h_upper = 0 
  h_left = 0
  
  # get how many horiztonal slices to make
  h_slices = int(math.ceil(h_height/horizontal_size)) 

  #make the horizonal slice
  for row_count in range(1,h_slices+1):
    h_lower = int(row_count * horizontal_size)  
    h_bounding = (h_left, h_upper, h_width, h_lower)
    horizontal_slice = img.crop(h_bounding)
    # increment the upper boundry      
    h_upper += horizontal_size 
    print "Made horizontal slice #"+str(row_count)
    total_h_slices += 1

    # slice the horizontal slice vertically into singles
    v_width, v_height = horizontal_slice.size
    v_upper = 0
    v_left = 0
    v_lower = v_height
    v_slices = int(math.ceil(v_width/vertical_size))

    for column_count in range(1, v_slices+1):
      v_width = int(column_count * vertical_size)      
      v_bounding = (v_left, v_upper, v_width, v_lower)
      single_slice = horizontal_slice.crop(v_bounding)
      v_left += vertical_size
      print "Made vertical slice #" + str(column_count)
      total_v_slices += 1
      
      #save the single slice
      single_slice.save(os.path.join(output_dir, filename +"_row" + str(row_count) +"_column" + str(column_count)+".png"))
      print "Saved slice: " + filename +"_row" + str(row_count) +"_column" + str(column_count)+".png"+ str(column_count)
      total_s_slices += 1

  #print the stats
  print "Total Horizontal Slices Made:", str(total_h_slices)
  print "Total Vertical Slices Made:", str(total_v_slices)
  print "Total Slices Saved:", str(total_s_slices)

slice_and_dice("qrgarden.png", 'output/', 87, 87)