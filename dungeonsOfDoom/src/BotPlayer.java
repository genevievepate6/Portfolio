/**
 * Class for bot that chases player.
 */
public class BotPlayer {

    /* x coordinate of bot */
    private int x;
    /* y coordinate of bot */
    private int y;

    /**
     * Constructor for bot.
     *
     * @param x : x coordinate of bot.
     * @param y : y coordinate of bot.
     */
    public BotPlayer(int x, int y) {
        this.x = x;
        this.y = y;
    }

    /**
     * Gets x coordinate of bot.
     *
     * @return x
     */
    public int getX() {
        return x;
    }

    /**
     * Gets y coordinate of bot.
     *
     * @return y
     */
    public int getY() {
        return y;
    }

    /**
     * Sets new x coordinate of bot.
     *
     * @param newX
     */
    public void setX(int newX) {
        x = newX;
    }

    /**
     * Sets new y coordinate of bot.
     *
     * @param newY
     */
    public void setY(int newY) {
        y = newY;
    }

    /**
     * Calculates bot's move towards player based on player's coordinates compared to bot's.
     *
     * @param playerX : player's x coordinate
     * @param playerY : player's y coordinate
     */
    public void generateMove(int playerX, int playerY) {
        if (x > playerX) {
            setX(x - 1);
        } else if (x < playerX) {
            setX(x + 1);
        } else if (y < playerY) {
            setY(y + 1);
        } else if (y > playerY) {
            setY(y - 1);
        }
    }
}
