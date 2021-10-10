# importing pycairo
import cairo

# creating a SVG surface
# here geek95 is file name & 700, 700 is dimension
def textToSvg(text,fontSize=40):
    with cairo.SVGSurface("converted.svg", 600, 600) as surface:

        Context = cairo.Context(surface)
        Context.set_source_rgb(0, 0, 0)
        Context.set_font_size(fontSize)
        Context.select_font_face(
            "Open Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)

        yPos=-150

        for i in range(len(text)):
            Context.move_to(30, 30)
            Context.text_path(text[i])
            Context.set_line_width(1)
            Context.transform(cairo.Matrix(xx=1.0, yx=0.0, xy=0.0, yy=-1.0, x0=0.0, y0=0.0))
            Context.scale(1.5, 1)
            Context.translate(0, yPos)
            Context.stroke()

            yPos+=(fontSize+2)

    # printing message when file is saved
    print("Saved Text To SVG")