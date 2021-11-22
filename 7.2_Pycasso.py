'''
PYCASSO PROJECT
---------------
Your job is to make a cool picture.
You must use multiple colors.
You must have a coherent picture. No abstract art with random shapes.
You must use multiple types of graphic functions (e.g. circles, rectangles, lines, etc.)
Somewhere you must include a WHILE or FOR loop to create a repeating pattern.
Do not just redraw the same thing in the same location 10 times. 
You can contain multiple drawing commands in a loop, so you can draw multiple train cars for example.
Please use comments and blank lines to make it easy to follow your program. 
If you have 5 lines that draw a robot, group them together with blank lines above and below. 
Then add a comment at the top telling the reader what you are drawing.
IN THE WINDOW TITLE PLEASE PUT YOUR NAME.
When you are finished Pull Request your file to your instructor.

import arcade
SW = 600
SH = 400
arcade.open_window(SW, SH, "Art that I tried to make", False, False)
arcade.set_background_color(arcade.color.LIGHT_BLUE)
arcade.start_render()

#all the beautiful code
arcade.draw_lrtb_rectangle_filled(200, 400, 300, 200, arcade.color.BLACK)
arcade.draw_rectangle_filled(300,200,50,50, (255,0,0,50),45)
arcade.draw_rectangle_filled(300,300,50,50, (255,0,0,50),45)
arcade.draw_rectangle_filled(100, 60, 1000, 150, arcade.color.WHITE_SMOKE)
#arcade.draw_triangle_filled(100, 60, 50, 50, arcade.color.GRAY, 45)
arcade.draw_triangle_filled(250, 500, 400, 30, 100, 30, arcade.color.GRAY)





#arcade.draw_point(300, 300,(0,0,0),5)
#arcade.draw_line(20,30,100,200,arcade.color.BLUE,3)

arcade.finish_render()
arcade.run()
'''
import arcade

arcade.open_window(600, 600, "Drawing")

arcade.set_background_color(arcade.csscolor.SKY_BLUE)

arcade.start_render()

arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.color.WHITE_SMOKE)

#Tree trunk
arcade.draw_rectangle_filled(100, 320, 20, 60, arcade.color.SIENNA)
#Tree top
arcade.draw_circle_filled(100, 350, 30, arcade.color.DARK_GREEN)

#Another tree
arcade.draw_rectangle_filled(200, 320, 20, 60, arcade.color.SIENNA)
arcade.draw_ellipse_filled(200, 370, 60, 80, arcade.color.DARK_GREEN)

#Another tree
arcade.draw_rectangle_filled(300, 320, 20, 60, arcade.color.SIENNA)
arcade.draw_arc_filled(300, 340, 60, 100, arcade.color.DARK_GREEN, 0, 180)

arcade.draw_rectangle_filled(400, 320, 20, 60, arcade.color.SIENNA)
arcade.draw_triangle_filled(400, 400, 370, 320, 430, 320, arcade.color.DARK_GREEN)
arcade.draw_rectangle_filled(500, 320, 20, 60, arcade.color.BLACK)
#arcade.draw_rectangle_filled(500, 320, 10, 30, arcade.color.RED)
arcade.draw_circle_filled(500, 320, 15, arcade.color.RED)

arcade.draw_polygon_filled(((500, 400),
 (480, 360),
 (470, 320),
 (530, 320),
 (520, 360)), arcade.color.GRAY)

arcade.draw_circle_filled(150, 600, 40, arcade.color.GRAY)
arcade.draw_circle_filled(150, 600, 20, arcade.color.RED)

#arcade.draw_circle_filled(500, 550, 20, arcade.color.GRAY)
arcade.draw_circle_filled(500, 550, 40, arcade.color.YELLOW)
arcade.draw_line(500, 550, 400, 550, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 600, 550, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 500, 450, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 500, 650, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 550, 600, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 550, 500, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 450, 600, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 450, 500, arcade.color.YELLOW, 3)
arcade.draw_circle_filled(500, 550, 10, arcade.color.GRAY)
arcade.draw_circle_filled(500, 550, 5, arcade.color.RED)


arcade.draw_text("They are amung us.",
150, 230,
arcade.color.BLACK, 24)

arcade.finish_render()
arcade.run()

