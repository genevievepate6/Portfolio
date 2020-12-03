import java.util.Scanner;
/**
 * Runs the game with a human player and contains code needed to read inputs.
 *
 */
public class HumanPlayer {
    /* x coordinate of player */
    private int x;
    /* y coordinate of player */
    private int y;
    /* gold owned by player */
    private int goldOwned = 0;
    /* has player been captured by bot */
    private boolean captured = false;
    /* has player collected all god required and input exit while on the exit tile */
    private boolean won = false;
    /* Creates scanner to take user input */
    public Scanner input = new Scanner(System.in);

    /**
     * Constructor for player.
     *
     * @param x : x coordinate of player.
     * @param y : y coordinate of player.
     */
    public HumanPlayer(int x, int y){
        this.x = x;
        this.y = y;
    }

    /**
     * Gets player's x coordinate.
     *
     * @return x : x coordinate
     */
    public int getX(){
        return x;
    }

    /**
     * Gets player's y coordinate.
     *
     * @return x : y coordinate
     */

    public int getY(){
        return y;
    }

    /**
     * Sets player's x coordinate.
     * @param newX : the new x coordinate
     */
    public void setX(int newX) {
        x = newX;
    }

    /**
     * Sets player's y coordinate.
     * @param newY : the new x coordinate
     */

    public void setY(int newY) {
        y = newY;
    }

    /**
     *  Sets won to true if player has won.
     *
     * @param state : true if player has won.
     */
    public void setWon(boolean state){
        won = state;
    }

    /**
     * Checks if player has won.
     *
     * @return won : to check if player has won.
     */
    public boolean getWon(){
        return won;
    }

    /**
     * Checks if player has been captured.
     *
     * @return captured
     */
    public boolean getStatus() {
        return captured;
    }

    /**
     * Sets captured to true if the player has been captured.
     *
     * @return String
     */
    public String capture() {
        captured = true;
        return "LOSE";
    }

    /**
     * Gets gold owned by player.
     *
     * @return goldOwned.
     */
    public int getGoldOwned() {
        return goldOwned;
    }

    /**
     * Updates how much gold he player has collected.
     */
    public void updateGoldOwned() {
        goldOwned += 1;
    }
    /**
     * Reads player's input from the console.
     * <p>
     * return : A string containing the input the player entered.
     */
    protected String getInputFromConsole() {
        String command = input.nextLine();
        return command;
    }
}