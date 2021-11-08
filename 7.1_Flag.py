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
SW = 494
redline = 10 + 40
arcade.open_window(494, 260, "Art that I tried to make", True)
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()
arcade.draw_rectangle_filled(99, 190, 198, 140, arcade.color.BLUE)
arcade.draw_rectangle_filled(247, 10, SW, 20, arcade.color.RED)
arcade.draw_rectangle_filled(247, 50, SW, 20, arcade.color.RED)
arcade.draw_rectangle_filled(247, 90, SW, 20, arcade.color.RED)
arcade.draw_rectangle_filled(398, 130, 400, 20, arcade.color.RED)
arcade.draw_rectangle_filled(398, 170, 400, 20, arcade.color.RED)
arcade.draw_rectangle_filled(398, 210, 400, 20, arcade.color.RED)
arcade.draw_rectangle_filled(398, 250, 400, 20, arcade.color.RED)




arcade.finish_render()
arcade.run()