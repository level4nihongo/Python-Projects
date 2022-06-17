import curses, random #import statements

#setup window
curses.initscr()
window = curses.newwin(20,60,0,0) #y,x!!
window.keypad(1)
curses.noecho()
curses.curs_set(0)
window.border(0)
window.nodelay(1)

#snek and food
snek = [(4,10),(4,9),(4,8)]
food = (10,20)


#game logic
score = 0
ESC = 27
key = curses.KEY_RIGHT

while key != ESC:
    window.addstr(0,2,'Score: ' + str(score) +" ") #shows score
    window.timeout(150-(len(snek))//5 + len(snek)//10%120)
    prev_key = key #defines old key
    event = window.getch() #gets next key
    key = event if event != -1 else prev_key #sets new key as key unless not
    if key not in [curses.KEY_RIGHT,curses.KEY_LEFT,curses.KEY_UP,curses.KEY_DOWN, ESC]: #check arrow keys
        key = prev_key

    #calculate next coordinates and insert them
    y = snek[0][0]
    x = snek[0][1]

    if key == curses.KEY_DOWN:
        y += 1
    if key == curses.KEY_UP:
        y -= 1
    if key == curses.KEY_LEFT:
        x -= 1
    if key == curses.KEY_RIGHT:
        x += 1

    snek.insert(0, (y, x))

    #check collision
    if y == 0 : break
    if x == 0 : break
    if y == 19 : break
    if x == 59 : break
    if snek[0] in snek[1:]: break

    if snek[0] == food:
        #eat food
        score += 1
        food = ()
        #create food and check if in snake
        while food == ():
            food = (random.randint(1,18), random.randint(1,58))
            if food in snek:
                food = ()
        window.addch(food[0],food[1], 'O')
    else:
        #move the snake
        last = snek.pop()
        window.addch(last[0], last[1], " ")

    #render the snake and food spawns
    window.addch(snek[0][0], snek[0][1], ">")
    for x in snek[1:(len(snek)-1)]:
        window.addch(x[0],x[1],"O")
    window.addch(food[0], food[1], "O")

curses.endwin()
print(f"Score = {score}")
