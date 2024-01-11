import edu.fcps.karel2.Display;
import edu.fcps.karel2.Robot;

public class Stacker extends Athlete
{
   //fields
   private int size;
   
   //constructor
   public Stacker(int x, int y, int givenSize)
   {
      super(x, y, Display.EAST, Display.INFINITY);
      size = givenSize;
   }
   
   //instance methods
   public void makeStack()
   {
      for(int i = 0; i < size; i++)
      {
         putBeeper();
      }
   }
   
   public void makeStacks(int num)
   {
      for(int i = 0; i < num; i++)
      {
         makeStack();
         move();
      }
   }
   
   public void fixStack()
   {
      //No matter what size of beeper stack this intersection currently has,
      //correct it so that it is of the size stored in the size field.
   }
   
   public void fixStacks(int num)
   {
      //Starting on the current space, fix the next num different stacks forward
      //from here.
   }
}