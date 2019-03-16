theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
   print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
   print('-+-+-')
   print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
   print('-+-+-')
   print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def checkWinnerRow(row,turn):
   if ( theBoard[row+'-L'] == turn and theBoard[row+'-L'] == theBoard[row+"-M"] and  theBoard[row+'-L'] == theBoard[row+"-R"] ):
       print("The winner is: " + turn)
       return True
   else:
       return False

def checkWinnerColumn(column,turn):
   if ( theBoard['top-'+column] == turn and theBoard['top-'+column] == theBoard['mid-'+column] and  theBoard['top-'+column] == theBoard['low-'+column] ):
       print("The winner is: " + turn)
       return True
   else:
       return False
def validInput():
    move = ' '
    try:
        move = input()
        ## print("Current value is: " + theBoard[move])
        while theBoard[move] != ' ':
            ## print(theBoard[move])
            move = input("Input valid move: ")
        theBoard[move] = turn
    except:
        print("Valid inputs are: " )
        print(theBoard.keys())
        validInput()
        
turn = 'X'
for i in range(9):
  printBoard(theBoard)
  print('Turn for ' + turn + '. Move on which space?')
  ## move = input()
  ## theBoard[move] = turn
  validInput()
  if checkWinnerRow('top',turn):
      break
  if checkWinnerRow('mid',turn):
      break
  if checkWinnerRow('low',turn):
      break
  if checkWinnerColumn("L",turn):
      break
  if checkWinnerColumn("M",turn):
      break
  if checkWinnerColumn("R",turn):
      break

  if ( theBoard['top-L'] == turn and theBoard['mid-M'] == theBoard['top-L'] and  theBoard['top-L'] == theBoard['low-R'] ):
       print("The winner is: " + turn)
       break
  if ( theBoard['top-R'] == turn and theBoard['mid-M'] == theBoard['top-R'] and  theBoard['top-R'] == theBoard['low-L'] ):
       print("The winner is: " + turn)
       break
    
  if turn == 'X':
     turn = 'O'
  else:
     turn = 'X'
printBoard(theBoard)
