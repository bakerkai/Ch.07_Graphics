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

SW = 600
SH = 400
arcade.open_window(SW, SH, "Art that I tried to make", False, False)
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()
arcade.draw_line(100, 200, 120, 260, lk)
arcade.finish_render()
arcade.run()