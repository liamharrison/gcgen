import math

def generic_setup(safe_height):

  #T1 tool 1
  #G21 mm mode
  #G90 abs Positioning
  #G17 xy plane

  commands = ['T1', 'G21', 'G90', 'G17']
  gcode_out = '\n'.join(commands)
  gcode_out += '\n'
  gcode_out += 'G00 Z' + str(safe_height) + '\n'
	
  return(gcode_out)

def helicut_circle(pos_x, pos_y, diameter, depth, safe_height, helicut_feed_rate, step_thickness = 2):
  
  radius = diameter / 2
  
  gcode_start = 'G00 Z' + str(safe_height) + '\n'
  gcode_start += 'G00 X' + str(pos_x - radius) + ' Y' + str(pos_y) + '\n'
  gcode_start += 'G01 Z0 F' + str(helicut_feed_rate) + '\n'
  
  if abs(depth) < step_thickness:
    step_thickness = abs(depth)
    #print('depth < step')

  iterations = math.ceil(abs(depth) / step_thickness)
  step_height = depth / iterations
  quadrant_height = step_height / 4
  
  # G02 XYZ IJK

  gcode_helix = ''
  for i in range(1, iterations + 1):
    z_depth = step_height * i
    gcode_helix += 'G02 X' + str(pos_x - radius) + ' Y' + str(pos_y) + ' Z' + str(z_depth) + ' I' + str(radius) + ' J0 F' + str(helicut_feed_rate) + '\n'
	
  gcode_bottom = 'G02 X' + str(pos_x - radius) + ' Y' + str(pos_y) + ' I' + str(radius) + ' J0 F' + str(helicut_feed_rate) + '\n'
  gcode_exit = 'G02 X' + str(pos_x - radius) + ' Y' + str(pos_y) + ' Z' + str(safe_height) + ' I' + str(radius) + ' J0 F' + str(helicut_feed_rate) + '\n'

  return(gcode_start + gcode_helix + gcode_bottom + gcode_exit)

def line_primitive(end_x, end_y, feed_rate):

  gcode_line = 'G01 X' + str(end_x) + ' Y' + str(end_y) +' F' + str(feed_rate) + '\n'
  
  return(gcode_line)
  
def rectangle_primitive(start_x, start_y, end_x, end_y, feed_rate):

  gcode_rectangle = 'G01 X' + str(end_x) + ' F' + str(feed_rate) + '\n'
  gcode_rectangle += 'G01 Y' + str(end_y) + ' F' + str(feed_rate) + '\n'
  gcode_rectangle += 'G01 X' + str(start_x) + ' F' + str(feed_rate) + '\n'
  gcode_rectangle += 'G01 Y' + str(start_y) + ' F' + str(feed_rate) + '\n'
  
  return(gcode_rectangle)

def line_intermediate(start_x, start_y, end_x, end_y, feed_rate, drill_feed_rate, safe_height, depths):

  gcode_line = 'G00 Z' + str(safe_height) + '\n'
  gcode_line += 'G00 X' + str(start_x) + ' Y' + str(start_y) + '\n';
  
  direction_counter = 0
  
  for depth in depths:
  
    if direction_counter % 2 == 0:
      #print('END X')
      current_end_x = end_x
      current_end_y = end_y
    else:
      #print('START X')
      current_end_x = start_x
      current_end_y = start_y
	
    gcode_line += 'G01 Z' + str(depth) + ' F' + str(drill_feed_rate) + '\n'
    gcode_line += line_primitive(current_end_x, current_end_y, feed_rate)
	
    direction_counter += 1
	
  return(gcode_line)
  
def rectangle_intermediate(start_x, start_y, end_x, end_y, feed_rate, drill_feed_rate, safe_height, depths):

  gcode_rectangle = 'G00 Z' + str(safe_height) + '\n'
  gcode_rectangle += 'G00 X' + str(start_x) + ' Y' + str(start_y) + '\n';
  
  for depth in depths:
    gcode_rectangle += 'G01 Z' + str(depth) + ' F' + str(drill_feed_rate) + '\n'
    gcode_rectangle += rectangle_primitive(start_x, start_y, end_x, end_y, feed_rate)

  return(gcode_rectangle)

def rectangle_outside(start_x, start_y, end_x, end_y, feed_rate, drill_feed_rate, cutter_diameter, safe_height, depths=[1]):

  cutter_radius = cutter_diameter / 2;
  
  adj_start_x = start_x - cutter_radius
  adj_start_y = start_y - cutter_radius
  adj_end_x = end_x + cutter_radius
  adj_end_y = end_y + cutter_radius
  
  gcode_rectangle = rectangle_intermediate(adj_start_x, adj_start_y, adj_end_x, adj_end_y, feed_rate, drill_feed_rate, safe_height, depths)

  return(gcode_rectangle)

  
def drill(pos_x, pos_y, depth, safe_height, drill_feed_rate):

  gcode_drill = 'G00 Z' + str(safe_height) + '\n'
  gcode_drill += 'G00 X' + str(pos_x) + ' Y' + str(pos_y) + '\n'
  gcode_drill += 'G01 Z' + str(depth) + ' F' + str(drill_feed_rate) + '\n'
  gcode_drill += 'G00 Z' + str(safe_height) + '\n'

  return(gcode_drill)

  
