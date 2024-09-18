GAME: Iteration Of Black And White
************************************************************************************************************************************************************ 
1.Game rules
**Click on any block on the control panel, and the block itself and the four adjacent blocks (above, below, left, and right)
  will change color (from white to black or from black to white).
**You should complete the target pattern through the above-mentioned operation.
**Each level has a limited time. If you exceed the limited time, it will be considered a failure.
**After 5 failed attempts, you will have an opportunity to watch the best solution.

* Here is a basic operation: 
      012                                               012
   
   0  101                                            0  101
   1  000    After clicking (2,2)#(row,column)--->   1  001
   2  101                                            2  110

*Here is an example.
   the initial pattern:             the target pattern:
      01234                              01234

   0  11111                           0  10101
   1  11111                           1  00000
   2  11111                           2  11111
   3  11111                           3  10101
   4  11111                           4  11011

 To complete the target pattern,the best solution is:
 (1,1)(1,3)(2,2)(3,2)#(row,column)
************************************************************************************************************************************************************ 
2.Let's play!
**Attention: Before starting the game
*            Please make your terminal as large as possible to ensure all the pictures are visible. 
*            If you still can't view the full image, try shrinking browser fonts.
*            After entering the game
*            You can press 'q' at any time to get back to the previous interface. 
**Start the game
*            Type a command line in the terminal: python3 final_version5.py
*                notice: The relative path must be the program path.
*            You'll get into the interface of our game. Then click any button to enter.
**Enter the game
*            Please follow the instructions on the game interface.
*
*            First you can see four options**(please choose by using arrow key and Enter key):
*                play: begin to play the game
*                scoreboard: You can view the three shortest time taken of each task.
*                tutorial: check the detailed game rules
*                exit: quit the game
*            
*            If you choose 'tutorial':
*                You will first get to know the basic operation and the rules of our game.
*                If you want to gain a deeper insight into the game, you can click the button 'Click to access an example' 
*                to see the best solution of a task.
*
*            If you choose 'scoreboard':
*                You will see the three shortest time taken arranged in ascending order in a list after the number of each task. 
*                i.e. The first one is the record(the best performance) of the task.
*                You can check the record of each task and see your rank. You can try to break the record or compete with your friends.
*                e.g. 1#the task number       [1,2,3]#the three shortest time taken         #the record of task 1 is 1 second.  
*
*            If you choose 'play':
*                Then you can select the level of difficulty from easy(5*5 board), medium(7*7 board) and hard(9*9 board).
*                Each level contains 15 tasks which you can choose at will.  **(choose the level and the task by using arrow key and Enter key)
*
*                Once the task is selected, the game starts. 
*                Please operate on the left-hand board to complete the pattern on the right-hand side.
*                The remaining time is displayed at the top of the right-hand board.
*                There are four buttons on the right side of the interface:
*                   close (press q): close the game.
*                   reset (press r): reset the board.
*                   best solution (press b): show best solution.(The number of attempts required to view the best solution can be seen below the button.)
*                   withdraw (press w): withdraw the last step.              
*
*                You have two ways to play the game:
*                1.simply click the block with your mouse.
*                2.press the space and then you can input the row index and column index of the block respectively.
*                  (The horizontal and vertical coordinate numbers are displayed at the top and on the left sides of the left-hand panel, respectively.)
*                note: 1)For the best experience, it is recommended to use mouse for gaming whenever possible.
*                      2)You'd better avoid using the touchpad for gaming.
*
*                Each level has a limited time. 
*                If you exceed the limited time, it will be considered a failure.
*                    After each failure, you can decide whether to continue or not. Press 'y' to have another attempt, 'n' to stop trying.
*                    After 5 failed attempts, you will have an opportunity to watch the best solution.
*              
*                If you completed the task but you didn't find the best solution, you will be rewarded by Kit and get back to the menu.
*
*                If you completed the task with the best solution, you can access the wonderful egg we prepared for you.  Congratulations!
************************************************************************************************************************************************************ 
*Wish you have fun!
************************************************************************************************************************************************************           

