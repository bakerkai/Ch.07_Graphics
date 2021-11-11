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
'''
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
arcade.draw_rectangle_filled(arcade.draw_rectangle_filled(247, 90, SW, 20, arcade.color.WHITE)
)


#arcade.draw_point(300, 300,(0,0,0),5)
#arcade.draw_line(20,30,100,200,arcade.color.BLUE,3)

arcade.finish_render()
arcade.run()

