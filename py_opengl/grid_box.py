#!/usr/bin/python

# This is statement is required by the build system to query build info
if __name__ == '__build__':
    raise Exception


import sys

try:
    from OpenGL.GLUT import *
    from OpenGL.GL import *
    from OpenGL.GLU import *
except:
    print '''
ERROR: PyOpenGL not installed properly.  
        '''


def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glShadeModel(GL_FLAT)

def drawOneLine(x1, y1,z1, x2, y2,z2):
    glBegin(GL_LINES)
    glVertex3f(x1, y1, z1)
    glVertex3f(x2, y2, z2)
    glEnd()


def plot_lines(x_min,x_max,y_min,y_max,z_min,z_max,split_range=1):
    glLineStipple(1, 0x1C47)  # dashed
    x_range = range(x_min,x_max+1,split_range)
    z_range = range(z_min,z_max+1,split_range)
    y_range = range(y_min,y_max+1,split_range)
    for tmp_y in y_range:
        # draw on xz for diff y
        for tmp_x in x_range:
            drawOneLine(tmp_x, tmp_y, z_min, tmp_x, tmp_y, z_max)
        for tmp_z in z_range:
            drawOneLine(x_min, tmp_y, tmp_z, x_max, tmp_y, tmp_z)
    #drawOneLine(0,0,0,0,5,0)


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    glLoadIdentity()  # clear the matrix
    glEnable(GL_LINE_STIPPLE)
    # viewing transformation
    gluLookAt(10, 10.0, 10, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    #glScalef(1.0, 2.0, 1.0)  # modeling transformation
    #glutWireCube(5.0)
    # glBegin(GL_LINES)
    # drawlinefor x axis
    # glColor3f(1.0, 0.0, 0.0)
    # glVertex3f(0.0, 0.0, 0.0)
    # glVertex3f(10.0, 0.0, 0.0)
    # # draw line for y axis
    # glColor3f(0.0, 1.0, 0.0)
    # glVertex3f(0.0, 0.0, 0.0)
    # glVertex3f(0.0, 10.0, 0.0)
    # # draw line for Z axis
    # glColor3f(0.0, 0.0, 1.0)
    # glVertex3f(0.0, 0.0, 0.0)
    # glVertex3f(0.0, 0.0, 10.0)
    # glEnd()
    # draw grid lines, select white for all lines
    glColor3f(1.0, 1.0, 1.0)
    plot_lines(-2, 2, -3, 4, -5, 5)
    glFlush()


def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glFrustum(-1.0, 1.0, -1.0, 1.0, 1.5, 20.0)
    glMatrixMode(GL_MODELVIEW)


def keyboard(key, x, y):
    if key == chr(27):
        import sys
        sys.exit(0)


glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutInitWindowPosition(100, 100)
glutCreateWindow('grid_box')
init()
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutKeyboardFunc(keyboard)
glutMainLoop()

