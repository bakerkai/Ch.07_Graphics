import arcade
SW = 600
SH = 400

arcade.open_window(SW, SH, "Star Wars Art", False, False)
arcade.set_background_color(arcade.color.KOBE)
arcade.start_render()
arcade.draw_lrtb_rectangle_filled(200, 400, 300, 200, arcade.color.AFRICAN_VIOLET)
arcade.draw_rectangle_filled(300,200,50,50, (255,255,0,50),45)
arcade.draw_point(300, 300,(0,0,0),5)
arcade.draw_line(20,30,100,200,arcade.color.BLUE,3)

arcade.draw_circle_filled(400,100,20,arcade.color.GREEN)
#arcade.draw_text("May the force be with you",100,100,100, arcade.color.ALICE_BLUE, 14, 300, "center","Papyrus", True)
for x in range(0,SW+1,20):
    arcade.draw_rectangle_filled(x,20,10,30,arcade.color.WHITE)
arcade.draw_rectangle_filled(300,20,SW,5, arcade.color.WHITE)
arcade.draw_rectangle_filled(300,10,SW,5, arcade.color.WHITE)


arcade.finish_render()
arcade.run()
