"""Tile.py: Find all solutions available to build a rectangle wall with
given bricks and show the turtle graph of the solution selected by the user.

__author__ = "Wang Yuzhe"
__pkuid__  = "1800011828"
__email__  = "1800011828@pku.edu.cn"
"""


import turtle
import sys
sys.setrecursionlimit(100000000)


def x_available(lst, i, a, b, m, n):
    """Judge if the brick can be installed horizontally."""
    if (i % m+a) <= m and (i//m+b) <= n:
        test_lst = [lst[j] for k in range(0, b) for j in range(i+k*m, i+k*m+a)]
        if 0 in test_lst and 1 not in test_lst:
            return True
        else:
            return False
    else:
        return False


def y_available(lst, i, a, b, m, n):
    """Judge if the brick can be installed vertically."""
    return x_available(lst, i, b, a, m, n)


def next_brick(lst, print_lst, i, a, b, m, n, all_lst):
    """Install the  bricks using recursion."""
    if a == b and m % a == 0 and n % a == 0:  # The length of the brick equals to the width.
        for j in range(0, int(n/a)):
            for k in range(0, int(m/a)):
                print_lst.append(tuple([r for s in range(0, a) for r
                                        in range(j*m*a+k*a + s * m, j*m*a+k*a + s * m + a)]))
        all_lst = [print_lst]
    else:
        if i <= (m*n):  # Reach the end .
            if 1 in lst and 0 not in lst:  # The solution is available.
                all_lst.append(print_lst)
            else:  # Try to install the next brick.
                if x_available(lst, i, a, b, m, n):
                    lst_copy = lst[:]
                    print_lst_copy = print_lst[:]
                    print_lst.append(tuple([j for k in range(0, b) for j in range(i + k * m, i + k * m + a)]))
                    for k in range(0, b):
                        for j in range(i + k * m, i + k * m + a):
                            lst[j] = 1
                    next_brick(lst, print_lst, i + 1, a, b, m, n, all_lst)
                    lst = lst_copy[:]
                    print_lst = print_lst_copy[:]
                if y_available(lst, i, a, b, m, n):
                    lst_copy = lst[:]
                    print_lst_copy = print_lst[:]
                    print_lst.append(tuple([j for k in range(0, a) for j in range(i + k * m, i + k * m + b)]))
                    for k in range(0, a):
                        for j in range(i + k * m, i + k * m + b):
                            lst[j] = 1
                    next_brick(lst, print_lst, i + 1, a, b, m, n, all_lst)
                    lst = lst_copy[:]
                    print_lst = print_lst_copy[:]
                else:
                    next_brick(lst, print_lst, i+1, a, b, m, n, all_lst)
    return all_lst


def turtle_draw_base(alex, m, n, color, pensize):
    """Draw the wall itself and label the number."""
    alex.color(color)
    alex.pensize(pensize)
    alex.speed(0)
    delta_x = -(30 * m) / 2
    delta_y = (30 * n) / 2  # Adjust the position of the wall to the center of the screen.
    epsilon = 12/m  # Adjust the size of the wall.
    alex.penup()
    for p in range(0, n+1):
        alex.goto(epsilon*(0+delta_x), epsilon*(-30 * p+delta_y))
        alex.pendown()
        alex.forward(epsilon*(30 * m))
        alex.penup()
    alex.right(90)
    for q in range(0, m+1):
        alex.goto(epsilon*(30 * q+delta_x), epsilon*(0+delta_y))
        alex.pendown()
        alex.forward(epsilon*(30 * n))
        alex.penup()
    for p in range(0, n):
        for q in range(0, m):  # Label the number.
            c = str(m * p+q)
            alex.goto(epsilon*(q*30+15+delta_x), epsilon*(-p*30-27+delta_y))
            alex.write(c, False, 'center', ('Arial', int(epsilon*15)+1, 'normal'))
    alex.hideturtle()


def turtle_draw_bricks(alex, solution_selected, m, n):
    """Draw the bricks according to the solution selected."""
    alex.color('black')
    alex.pensize(5)
    alex.speed(0)
    delta_x = -(30 * m) / 2
    delta_y = (30 * n) / 2
    epsilon = 12/m
    for brick in solution_selected:
        p = brick[0]
        q = brick[-1]
        alex.penup()
        alex.goto(epsilon*((p % m)*30+delta_x), epsilon*(-(p//m)*30+delta_y))
        alex.pendown()
        alex.goto(epsilon*(((q % m)+1)*30+delta_x), epsilon*(-(p//m)*30+delta_y))
        alex.goto(epsilon*(((q % m)+1)*30+delta_x), epsilon*(-((q//m)+1)*30+delta_y))
        alex.goto(epsilon*((p % m)*30+delta_x), epsilon*(-((q//m)+1)*30+delta_y))
        alex.goto(epsilon*((p % m) * 30+delta_x), epsilon*(-(p // m) * 30+delta_y))
    alex.hideturtle()


def main():
    """Main module."""
    m = int(input('Please type in the length of the wall: '))
    n = int(input('Please type in the width of the wall: '))
    a = int(input('Please type in the length of the brick: '))
    b = int(input('Please type in the width of the brick: '))
    lst = [0]*(m*n)  # Save the status of the wall.
    print_lst = []
    all_lst = []  # Save all the solutions available.
    all_lst = next_brick(lst, print_lst, 0, a, b, m, n, all_lst)
    p = len(all_lst)
    if p == 0:  # No solution available.
        print('Sorry,no solution available to build the wall.')
    elif a == b == 1:  # The length of the brick equals to the width.Only one solution available.
        print('Solution :', [q[0] for q in all_lst[0]])
        print('There is', 1, 'solution available to build the wall.')
        query = input('Show the solution now? (type in Yes/No): ')
        if query == 'Yes':
            alex = turtle.Turtle()
            wn = turtle.Screen()
            wn.title('Selected solution to build the wall :) ')
            turtle_draw_base(alex, m, n, 'black', 5)
            wn.exitonclick()
    elif p == 1 or a == b:  # Only one solution available.
        print('Solution :', all_lst[0])
        print('There is', 1, 'solution available to build the wall.')
        query = input('Show the solution now? (type in Yes/No): ')
        if query == 'Yes':
            solution_selected = all_lst[0]
            alex = turtle.Turtle()
            wn = turtle.Screen()
            wn.title('Selected solution to build the wall :) ')
            turtle_draw_base(alex, m, n, 'sea green', 2)
            turtle_draw_bricks(alex, solution_selected, m, n)
            wn.exitonclick()
    else:
        for i in range(1, p+1):
            print('Solution', i, ':', all_lst[i-1])
        print('There are', p, 'solutions available to build the wall.')
        t = int(input('Please type in the solution number to select one of the solutions to build the wall: '))
        solution_selected = all_lst[t-1]
        alex = turtle.Turtle()
        wn = turtle.Screen()
        wn.title('Selected solution to build the wall :) ')
        turtle_draw_base(alex, m, n, 'sea green', 2)
        turtle_draw_bricks(alex, solution_selected, m, n)
        wn.exitonclick()


if __name__ == '__main__':
    main()
