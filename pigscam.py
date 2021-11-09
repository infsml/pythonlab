import pyglet
window = pyglet.window.Window()
window.set_size(640,480)


@window.event
def on_draw():
    window.clear()
    pyglet.graphics.draw(4, pyglet.gl.GL_QUADS,
                         ('v2i',(0,0,640,0,640,480,0,480)),
                         ('c3B',[255]*4*3)
                          )
    pyglet.graphics.draw(3, pyglet.gl.GL_LINE_STRIP,
                         ('v2i', (10, 15, 30, 35,70,50)),
                         ('c3B',[0]*3*3)
                         )

pyglet.app.run()
