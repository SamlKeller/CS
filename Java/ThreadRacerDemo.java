import edu.fcps.karel2.Display;
import edu.fcps.karel2.Robot;

public class ThreadRacerDemo
{
   public static void main(String[] args)
   {
      Display.openWorld("maps/shuttle.map");
      Display.setSize(10,10);
      Display.setSpeed(8);
      Runnable tr1 = new ThreadRacer(1);
      Runnable tr2 = new ThreadRacer(4);
      Runnable tr3 = new ThreadRacer(7);
      Thread t1 = new Thread(tr1);
      Thread t2 = new Thread(tr2);
      Thread t3 = new Thread(tr3);
      t1.start();
      t2.start();
      t3.start();
   }
}