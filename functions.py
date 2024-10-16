import cairo

def create_surface(width, height, background_color):
    surface = cairo.ImageSurface(cairo.FORMAT_RGB24, width, height)
    context = cairo.Context(surface)
    context.set_source_rgb(*background_color)
    context.paint()
    return surface, context

def create_house( context, x, y, width, height,a,b,c,d):
    context.move_to(x, y)
    context.line_to()

def create_windows():

def create_door():

def create_dome():

def create_moon():

