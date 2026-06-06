from tkinter import *
import random

tictactoe = None
tictactoeRandom = None
tictactoeAdvanced = None

def show_screen(frame):
  frame.tkraise()

def open_tictactoe():
  global tictactoe
  tictactoe = Toplevel(window)
  tictactoe.title("TicTacToe")

  spaces = [" "] * 9

  buttonPressednums = 0

  button_list = [None] * 9

  rows, cols = 3,3

  win_scenarios = [
    [0, 1, 2],  # top row
    [3, 4, 5],  # middle row
    [6, 7, 8],  # bottom row
    [0, 3, 6],  # left column
    [1, 4, 7],  # middle column
    [2, 5, 8],  # right column
    [0, 4, 8],  # diagonal
    [2, 4, 6]   # diagonal
  ]

  win = False

  def button_press(button,message_label,num):
    nonlocal buttonPressednums
    nonlocal spaces
    nonlocal win
    button.config(state=DISABLED)

    if buttonPressednums % 2 == 0:
      message_label.set(f"It's O's turn")
      spaces[num] = "X"
      button.config(text="X", highlightbackground="red", bg = "red", fg="white", font=("Arial", 12, "bold"))
      checkWin("X")
    else:
      message_label.set(f"It's X's turn")
      spaces[num] = "O"
      button.config(text="O", highlightbackground="blue", bg = "blue", fg="white",font=("Arial", 12, "bold"))
      checkWin("O")

    buttonPressednums = buttonPressednums + 1

    if win:
      for child in frame.winfo_children():
        child.config(state=DISABLED)
      message_label.set(f"{spaces[num]} has won the game!")

    if(buttonPressednums==9 and win == False):
      message_label.set("The game has ended in a draw.")


    

  def checkWin(type):
    nonlocal win
    nonlocal win_scenarios
    # if spaces[0] == type and spaces[1] == type and spaces[2] == type or spaces[3] == type and spaces[4] == type and spaces[5] == type or spaces[6] == type and spaces[7] == type and spaces[8] == type or spaces[0] == type and spaces[3] == type and spaces[6] == type or spaces[1] == type and spaces[4] == type and spaces[7] == type or spaces[2] == type and spaces[5] == type and spaces[8] == type or spaces[0] == type and spaces[4] == type and spaces[8] == type or spaces[2] == type and spaces[4] == type and spaces[6] == type:
    #   win = True

    for a,b,c in win_scenarios:
      if spaces[a] != " " and spaces[a] == spaces[b] == spaces[c]:
        win= True

  message_label = StringVar()

  message_label.set("It's X's turn")

  label = Label(tictactoe, textvariable=message_label, width=24, height=2)
  label.pack()

  frame=Frame(tictactoe)

  frame.pack()

  for i in range(len(button_list)):

    row,col = divmod(i, cols)

    button_list[i] = Button(frame,text="",height=4,width=9, font=35, command= lambda i=i: button_press(button_list[i],message_label,i))
    button_list[i].grid(row=row,column=col)

def open_tictactoeRandom():
  global tictactoeRandom
  tictactoeRandom = Toplevel(window)
  tictactoeRandom.title("TicTacToe Random")
  tictactoeRandom.geometry("500x500")


  frame1 = Frame(tictactoeRandom)
  frame1.pack()
  
  Button(frame1, text = "Play as X", command=lambda: play_tictactoeRandom("O","X",frame1)).pack()
  Button(frame1, text = "Play as O", command=lambda: play_tictactoeRandom("X","O",frame1)).pack()


def play_tictactoeRandom(Character,playerCharacter,frame1):
  frame1.destroy()

  spaces = [" "] * 9

  currentRound = 0

  button_list = [None] * 9

  rows, cols = 3,3

  win = False

  win_scenarios = [
    [0, 1, 2],  # top row
    [3, 4, 5],  # middle row
    [6, 7, 8],  # bottom row
    [0, 3, 6],  # left column
    [1, 4, 7],  # middle column
    [2, 5, 8],  # right column
    [0, 4, 8],  # diagonal
    [2, 4, 6]   # diagonal
  ]

  spacesNumbers = [1,2,3,4,5,6,7,8,9]

  message_label = StringVar()

  message_label.set("You're playing TicTacToe")

  label = Label(tictactoeRandom, textvariable=message_label,width=24, height=2)
  label.pack()

  frame2 = Frame(tictactoeRandom)
  frame2.pack()

  def button_press(button,message_label,num):
    nonlocal currentRound
    nonlocal spaces
    nonlocal win
    button.config(state=DISABLED)
    
    spaces[num] = playerCharacter
    button.config(text=playerCharacter, highlightbackground="red" if playerCharacter == "X" else "blue", bg="red" if playerCharacter == "X" else "blue",fg="white", font=("Arial", 12, "bold"))
    checkWin(playerCharacter)
    spacesNumbers.remove(num+1)
  
    currentRound = currentRound + 1

    playComputer()

    if win:
      for child in frame2.winfo_children():
        child.config(state=DISABLED)
      return

    if(currentRound==9 and win == False):
      message_label.set("The game has ended in a draw.")

  def checkWin(type):
    nonlocal win_scenarios
    nonlocal win
    # if spaces[0] == type and spaces[1] == type and spaces[2] == type or spaces[3] == type and spaces[4] == type and spaces[5] == type or spaces[6] == type and spaces[7] == type and spaces[8] == type or spaces[0] == type and spaces[3] == type and spaces[6] == type or spaces[1] == type and spaces[4] == type and spaces[7] == type or spaces[2] == type and spaces[5] == type and spaces[8] == type or spaces[0] == type and spaces[4] == type and spaces[8] == type or spaces[2] == type and spaces[4] == type and spaces[6] == type:
    #   win = True
    #   message_label.set(f"{type} has won the game!")

    for a,b,c in win_scenarios:
      if spaces[a] != " " and spaces[a] == spaces[b] == spaces[c]:
        win= True
        message_label.set(f"{type} has won the game!")

  def playComputer():
    nonlocal currentRound

    if not win and spacesNumbers:
      randomSpace = random.choice(spacesNumbers)

      spacesNumbers.remove(randomSpace)

      button_list[randomSpace-1].config(text=Character, highlightbackground="red" if Character == "X" else "blue",bg="red" if Character == "X" else "blue", fg="white", font=("Arial", 12, "bold"),state=DISABLED)

      spaces[randomSpace-1] = Character

      currentRound = currentRound + 1

      checkWin(Character)

  for i in range(len(button_list)):

    row,col = divmod(i, cols)

    button_list[i] = Button(frame2,text="",height=4,width=9, font=35, command= lambda i=i: button_press(button_list[i],message_label,i))
    button_list[i].grid(row=row,column=col)

  if Character == "X":
    playComputer()


def open_tictactoeAdvanced():
  global tictactoeAdvanced
  tictactoeAdvanced = Toplevel(window)
  tictactoeAdvanced.title("TicTacToe Advanced")
  tictactoeAdvanced.geometry("500x500")

  frame1 = Frame(tictactoeAdvanced)
  frame1.pack()
  
  Button(frame1, text = "Play as X", command=lambda: play_tictactoeAdvanced("O","X",frame1)).pack()
  Button(frame1, text = "Play as O", command=lambda: play_tictactoeAdvanced("X","O",frame1)).pack()

def play_tictactoeAdvanced(Character,playerCharacter,frame1):
  frame1.destroy()

  spaces = [" "] * 9

  currentRound = 0

  button_list = [None] * 9

  rows, cols = 3,3

  win = False

  corner = [0,2,6,8]

  win_scenarios = [
    [0, 1, 2],  # top row
    [3, 4, 5],  # middle row
    [6, 7, 8],  # bottom row
    [0, 3, 6],  # left column``
    [1, 4, 7],  # middle column
    [2, 5, 8],  # right column
    [0, 4, 8],  # diagonal
    [2, 4, 6]   # diagonal
  ]

  spacesNumbers = [0,1,2,3,4,5,6,7,8]

  message_label = StringVar()

  message_label.set("You're playing TicTacToe")

  label = Label(tictactoeAdvanced, textvariable=message_label,width=24, height=2)
  label.pack()

  frame2 = Frame(tictactoeAdvanced)
  frame2.pack()

  def button_press(button,message_label,num):
    nonlocal currentRound
    nonlocal spaces
    nonlocal win
    button.config(state=DISABLED)
    
    spaces[num] = playerCharacter
    button.config(text=playerCharacter, highlightbackground="red" if playerCharacter == "X" else "blue", bg="red" if playerCharacter == "X" else "blue", fg="white", font=("Arial", 12, "bold"))
    checkWin(playerCharacter)
    spacesNumbers.remove(num)
  
    currentRound = currentRound + 1

    playComputer()

    if win:
      for child in frame2.winfo_children():
        child.config(state=DISABLED)
      return

    if(currentRound==9 and win == False):
      message_label.set("The game has ended in a draw.")

  def checkWin(type):
    nonlocal win_scenarios
    nonlocal win
    # if spaces[0] == type and spaces[1] == type and spaces[2] == type or spaces[3] == type and spaces[4] == type and spaces[5] == type or spaces[6] == type and spaces[7] == type and spaces[8] == type or spaces[0] == type and spaces[3] == type and spaces[6] == type or spaces[1] == type and spaces[4] == type and spaces[7] == type or spaces[2] == type and spaces[5] == type and spaces[8] == type or spaces[0] == type and spaces[4] == type and spaces[8] == type or spaces[2] == type and spaces[4] == type and spaces[6] == type:
    #   win = True
    #   message_label.set(f"{type} has won the game!")

    for a,b,c in win_scenarios:
      if spaces[a] != " " and spaces[a] == spaces[b] == spaces[c]:
        win= True
        message_label.set(f"{type} has won the game!")

  def playComputer():
    nonlocal currentRound
    nonlocal win_scenarios
    # winningMove = None
    # blockMove = None
    BetterMoveMade = False
    move = 0
    non_occupied_corners = [i for i in corner if spaces[i]==" "] # collect i, for each i in corner, if that corner is empty
    


    if not win and spacesNumbers:
      if currentRound>=0:
        for a,b,c in win_scenarios:
          line  = [spaces[a], spaces[b], spaces[c]]
          if line.count(Character)==2 and line.count(" ") == 1:
            BetterMoveMade = True
            if spaces[a] == " ":  
              move = a
            elif spaces[b] == " ": 
              move = b
            elif spaces[c] == " ": 
              move = c
            break
          
        if BetterMoveMade == False:
          for a,b,c in win_scenarios:
            line  = [spaces[a], spaces[b], spaces[c]]
            if line.count(playerCharacter)==2 and line.count(" ") == 1:
              BetterMoveMade = True
              if spaces[a] == " ":
                move = a
              elif spaces[b] == " ": 
                move = b
              elif spaces[c] == " ": 
                move = c
              break

        if BetterMoveMade == False:
          if spaces[4] == " ":
            BetterMoveMade = True
            move = 4
          elif non_occupied_corners:
            BetterMoveMade = True
            move = random.choice(non_occupied_corners)
          else:
            move = random.choice(spacesNumbers)


      spacesNumbers.remove(move)

      button_list[move].config(text=Character, highlightbackground="red" if Character == "X" else "blue", fg="white", bg="red" if Character == "X" else "blue", font=("Arial", 12, "bold"),state=DISABLED)

      spaces[move] = Character

      currentRound = currentRound + 1

      checkWin(Character)
 
  for i in range(len(button_list)):

    row,col = divmod(i, cols)

    button_list[i] = Button(frame2,text="",height=4,width=9, font=35, command= lambda i=i: button_press(button_list[i],message_label,i))
    button_list[i].grid(row=row,column=col)

  if Character == "X":
    playComputer()


  


  












window = Tk()
window.title("TicTacToe")
window.geometry("500x500")

Button(window, text = "Tictactoe", command =  open_tictactoe).pack()
Button(window, text ="TicTacToe Random", command = open_tictactoeRandom).pack()
Button(window,text = "TicTacToe Advanced", command = open_tictactoeAdvanced).pack()

window.mainloop()
