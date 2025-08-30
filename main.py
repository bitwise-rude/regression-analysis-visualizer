import pygame
from constants import *
from data import *
import math

# initializing stuff
pygame.init()
pygame.display.init()

# font stuff
pygame.font.init()
label_scatter = pygame.font.SysFont('Times New Roman',15)
error_shower = pygame.font.SysFont("Algerian",18)



# making screen and componennts
pygame.display.set_caption("Regression Analysis Simulator and Visualizer")
screen = pygame.display.set_mode((SCREEN_WIDHT,SCREEN_HEIGHT))

 

# some functions
def update_grid():
    ''' This functions makes and updates the grid like a graph paper '''
    # x axis
    pygame.draw.line(screen,RED,(10,SCREEN_HEIGHT-10),(SCREEN_WIDHT-10,SCREEN_HEIGHT-10),width=5)
    # y axis
    pygame.draw.line(screen,RED,(10,SCREEN_HEIGHT-10),(10,10),width=5)

def convert_to_plot(coords):
    ''' Scales and modifies the data to be actually place on the grid (the cordinate system is changed here)'''

    x = coords[0]
    y = coords[1]
    x *= ((SCREEN_WIDHT - 10) // X_SCALE)
    y *=  ((SCREEN_HEIGHT- 10) // Y_SCALE)

    newX = x + 10
    newY = SCREEN_HEIGHT - (y + 10)
    return newX,newY



def scatter_data():
    ''' This function scatters data on the graph '''
    for x,y in zip(X,Y):
        pygame.draw.circle(screen,WHITE,convert_to_plot((x,y)),SCATTER_RADIUS)

        label = label_scatter.render(f'({x},{y})',True,GREEN)
        screen.blit(label,(convert_to_plot((x,y-1))))


def best_fit_line_coords(x,y):
    """
    Given two lists x and y, returns:
    1. The start and end coordinates of the best fit line segment (for plotting).
    2. The line function f(x) as a lambda.
    
    Output: ((x_min, y_start), (x_max, y_end)), f
    """
    if len(x) != len(y):
        raise ValueError("x and y must have the same length")
    n = len(x)
    
    mean_x = sum(x) / n
    mean_y = sum(y) / n

    num = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
    den = sum((x[i] - mean_x) ** 2 for i in range(n))
    m = num / den

    b = mean_y - m * mean_x

    x_min, x_max = min(x), max(x)

    y_min = m * x_min + b
    y_max = m * x_max + b

    line_func = lambda X: m * X + b

    return ( (x_min, y_min), (x_max, y_max) ), line_func


def plot_best_fit_line():
    pygame.draw.line(screen,BLUE,convert_to_plot(fit_line[0]),convert_to_plot(fit_line[1]),width=2)

def add_error_lines():
    ''' This functions adds the error lines on the graph'''
    for x,y in zip(X,Y):
        error = round(math.dist((x,y),(x,fit_line_eq(x))),2)
        pygame.draw.line(screen,COLOR_ERROR_LINE,convert_to_plot((x,y)),convert_to_plot((x,fit_line_eq(x))),width=2)
        screen.blit(error_shower.render(str(error),True,YELLOW),convert_to_plot((x,y)))



# claculating stuff
fit_line, fit_line_eq= best_fit_line_coords(X,Y)




# loop properties
running = True

while running:
    screen.fill(BLACK)

    # events polling
    for evs in pygame.event.get():
        if evs.type == pygame.QUIT:
            running = False
    
    update_grid()
    scatter_data()
    plot_best_fit_line()
    add_error_lines()

    pygame.display.update()

# clean up 
pygame.display.quit()
pygame.quit()