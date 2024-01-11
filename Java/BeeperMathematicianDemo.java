import edu.fcps.karel2.Display;
import edu.fcps.karel2.Robot;
import javax.swing.JOptionPane;

public class BeeperMathematicianDemo
{
   public static void main(String[] args)
   {
      String filename = JOptionPane.showInputDialog("What robot world?");
      Display.openWorld("maps/" + filename + ".map");
      Display.setSize(10, 10);
      Display.setSpeed(10);
      
      //Instantiate a BeeperMathematician in row 1.
      //Report the size of the current beeper pile and move off of it.
      BeeperMathematician one = new BeeperMathematician();
      int oneSize = one.getPileSize();
      one.move();
      System.out.println("Row one beeper pile has size: " + oneSize);
      
      //Instantiate a BeeperMathematician in row 2 using 1-arg constructor.
      //Report whether or not the current beeper pile has odd size and move off of it.
      BeeperMathematician two = new BeeperMathematician(2);
      boolean twoOdd = two.isOddPile();
      two.move();
      if(twoOdd)
      {
         System.out.println("Row two beeper pile has an odd number of beepers.");
      }
      else
      {
         System.out.println("Row two beeper pile has an even number of beepers.");
      }
      
   //Instantiate a BeeperMathematician in row 3 using a 1-arg constructor.
   //Find the average size of the next 3 piles and print the average to the console.
   //Code this challenge here:
      
      
      
   //Instantiate a BeeperMathematician in row 4 using a 1-arg constructor.
   //Instantiate an array of booleans.  Fill the array by calling oddsAndEvensInRow(6)
   //Then print the values in the array, separated by a space.  
      BeeperMathematician four = new BeeperMathematician(4);
      boolean[] isOddPile = four.oddsAndEvensInRow(6);
      System.out.print("Row 4: is each pile odd? ");
      for(int i=0; i<isOddPile.length; i++)
      {
         System.out.print(isOddPile[i] + " ");
      }
      System.out.println();
      
   //Instantiate a BeeperMathematician in row 5 using a 1-arg constructor.
   //Instantiate another one in row 6 using a 1-arg constructor.
   //Use getPileSizes and placePiles to recreate the first six piles on row 5 in row 6.
   //Code this challenge here:
      
      
      
   //Instantiate a BeeperMathematician in row 7 using a 1-arg constructor.
   //Instantiate another one in row 8 using a 1-arg constructor.
   //The first pile in row 7 is a multiplier.  The next three piles are values.
   //In row 8, create 3 new piles of beepers that are scaled up according to the multiplier.
   //For example, if row 7 had the following beeper piles: 3, 6, 1, 2
   //...then row 8 should get these piles: 18, 3, 6
   //Code this challenge here:
      
      
   }
}