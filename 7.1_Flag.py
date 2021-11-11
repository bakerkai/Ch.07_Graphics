'''
FLAG PROJECT
---------------
Make your flag 260 pixels tall
Use the scaling image on the website to determine other dimensions
The hexadecimal colors for the official flag are red:#BF0A30 and blue:#002868
Title the window, "The Stars and Stripes"
I used a draw_text command and used 20 pt. asterisks for the stars.
We will have a competition to see who can make this flag in the least lines of code.
The record is 16! You will have to use some loops to achieve this.
'''
import arcade
bruh = 130
SW = 494
redline = 10 + 40
arcade.open_window(494, 260, "Art that I tried to make", True)
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()
arcade.draw_rectangle_filled(99, 190, 198, 140, arcade.color.DARK_BLUE)
arcade.draw_rectangle_filled(247, 10, SW, 20, arcade.color.RED)
arcade.draw_rectangle_filled(247, 50, SW, 20, arcade.color.RED)
arcade.draw_rectangle_filled(247, 90, SW, 20, arcade.color.RED)
arcade.draw_rectangle_filled(398, 130, 400, 20, arcade.color.RED)
arcade.draw_rectangle_filled(398, 170, 400, 20, arcade.color.RED)
arcade.draw_rectangle_filled(398, 210, 400, 20, arcade.color.RED)
arcade.draw_rectangle_filled(398, 250, 400, 20, arcade.color.RED)
for a in range(120, 250, 25):
    arcade.draw_text("*", 10, a, arcade.color.WHITE, 20)
for b in range(130, 237, 27):
    arcade.draw_text("*", 31, b, arcade.color.WHITE, 20)
for c in range(120, 250, 25):
    arcade.draw_text("*", 52, c, arcade.color.WHITE, 20)
for d in range(130, 237, 27):
    arcade.draw_text("*", 73, d, arcade.color.WHITE, 20)
for e in range(120, 250, 25):
    arcade.draw_text("*", 94, e, arcade.color.WHITE, 20)
for f in range(130, 237, 27):
    arcade.draw_text("*", 115, f, arcade.color.WHITE, 20)
for g in range(120, 250, 25):
    arcade.draw_text("*", 136, g, arcade.color.WHITE, 20)
for h in range(130,237, 27):
    arcade.draw_text("*", 157, h, arcade.color.WHITE, 20)
for i in range(120, 250, 25):
    arcade.draw_text("*", 178, i, arcade.color.WHITE, 20)











arcade.finish_render()
arcade.run()