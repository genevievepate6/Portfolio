import java.util.Random; //To randomly generate starting coordinates for player and bot
/**
 * Contains the main logic part of the game, as it processes.
 *
 */
public class GameLogic {

    private Map map;
    private HumanPlayer player;
    private BotPlayer bot;
    Random rand = new Random();

    /**
     * Constructor that instantiates the player and bot objects, goving them loctions on the map.
     */
    public GameLogic() {
        int randPlayerX = rand.nextInt(19) + 1;
        int randPlayerY = rand.nextInt(8) + 1;
        int randBotX = 0;
        int randBotY = 0;
        int notEqual = 0;
        while (notEqual == 0){ // Checks that both bot and player do not start on the same tile.
            randBotX = rand.nextInt(19) + 1;
            randBotY = rand.nextInt(8) + 1;
            if (randBotX != randPlayerX && randBotY != randPlayerY){
                notEqual = 1;
            }
        }
        // Creates instance of bot and player.
        player = new HumanPlayer(randPlayerX, randPlayerY);
        bot = new BotPlayer(randBotX, randBotY);
    }

    /**
     * Method that takes user input and processes the command and moves the bot
     * If the bot moves onto the player's location, the player has been captured and they lose the game.
     * If the player collect all of the required gold and inputs exit on an exit tile, they win the game.
     */
    public void play(){
        map = new Map(9, 20); // Creates an instance of the map
        while (gameRunning() == true) { // Loops while the player hasn't won or been captured yet.
            bot.generateMove(player.getX(), player.getY());
            if (bot.getX() == player.getX() && bot.getY() == player.getY()){
                System.out.format(player.capture()); // If bot and player coordinates are the same, the player has been captured.
            }
            String command = "";
            if (player.getStatus() == false){
                command = player.getInputFromConsole(); // Takes input from user.
            }
            command = command.toUpperCase();
            // If input was not one of the accepted ones, FAIL is printed.
            if (command.equals("LOOK")) {
                look();
            } else if (command.equals("PICKUP")) {
                System.out.print(pickup());
            } else if (command.equals("HELLO")) {
                System.out.print(hello());
            } else if (command.equals("GOLD")) {
                System.out.print(gold());
            } else if (command.equals("MOVE N")) {
                System.out.print(move('N'));
            } else if (command.equals("MOVE S")) {
                System.out.print(move('S'));
            } else if (command.equals("MOVE E")) {
                System.out.print(move('E'));
            } else if (command.equals("MOVE W")) {
                System.out.print(move('W'));
            } else if (command.equals("QUIT")){
                if (checkWin() == true){ // Checks 2 win conditions
                    player.setWon(true);
                    System.out.println("WIN");
                }
                else{
                    System.out.println("FAIL");
                }
            }

        }
    }

    /**
     * Checks if the game is running
     *
     * @return true if the game is running.
     * @return false if the game should not be running (if player won or lost).
     */
    protected boolean gameRunning() {
        if (player.getStatus() == true) { // Checks if player si captured.
            return false;
        } else if (player.getWon() == true) { // Checks if player has won.
            return false;
        } else {
            return true;
        }
    }

    /**
     * Returns the gold required to win.
     *
     * @return : Gold required to win.
     */
    protected String hello() {
        return ("Gold required: " + map.getGoldRequired());
    }

    /**
     * Returns the gold currently owned by the player.
     *
     * @return : Gold currently owned.
     */
    protected String gold() {
        return ("Gold owned: " + player.getGoldOwned());
    }

    /**
     * Checks if movement is legal and updates player's location on the map.
     *
     * @param direction : The direction of the movement - N, S, E or W.
     * @return : A string, wither fail or success.
     */
    protected String move(char direction) {
        char grid[][] = map.getMap();
        if (direction == 'N') {
            int newY = player.getY() - 1;
            if (newY > 0) { // Checks for out of bounds movement.
                if (grid[newY][player.getX()] != '#') {
                    player.setY(newY);
                    return ("SUCCESS");
                }
                else {
                    return ("FAIL");
                }
            }
            else {
                return ("FAIL");
            }
        }
        else if (direction == 'S') {
            int newY = player.getY() + 1;
            if (newY < 19) {
                if (grid[newY][player.getX()] != '#') {
                    player.setY(newY);
                    return ("SUCCESS");
                }
                else {
                    return ("FAIL");
                }
            }
            else {
                return ("FAIL");
            }
        }
        else if (direction == 'E') {
            int newX = player.getX() + 1;
            if (newX > 0) {
                if (grid[player.getY()][newX] != '#') {
                    player.setX(newX);
                    return ("SUCCESS");
                }
                else {
                    return ("FAIL");
                }
            }
            else {
                return ("FAIL");
            }
        }
        else if (direction == 'W') {
            int newX = player.getX() - 1;
            if (newX < 19) {
                if (grid[player.getY()][newX] != '#') {
                    player.setX(newX);
                    return ("SUCCESS");
                }
                else {
                    return ("FAIL");
                }
            }
            else {
                return ("FAIL");
            }
        }
        else {
            return ("FAIL");
        }
    }

    /**
     * Shows a 5x5 grid of the map around the player, with them in the middle as P.
     * The bot is shown as B, gold as G, exit as E, walls as # and empty tiles as . .
     *
     * @return : A String representation of the game map.
     */
    protected void look() {
        char[][] grid = map.getMap();
        int botX = bot.getX();
        int botY = bot.getY();
        int j = (player.getX());
        int i = (player.getY());
        int k = i;
        int l = j;
        for (i = k-2; i < k+3; i++) {
            for (j = l-2;j < l+3; j++) {
                if (i>0 && i<19 && j>0 && j<19) {
                    if (i == botY && j == botX){
                        System.out.print('B'); // Shows bot location within visible range with look
                    }
                    if (i == k && j ==l){
                        System.out.print("P"); // Shows player location with P.
                    }

                    else{
                        System.out.print(grid[i][j]); // Prints empty tiles as . .
                    }
                }
                else{
                    System.out.print("#"); // Prints walls.
                }
            }
            System.out.print("\n");
        }
    }

    /**
     * Processes the player's pickup command, updating the map and the player's gold amount.
     *
     * @return If the player successfully picked-up gold or not.
     */
    protected String pickup() {
        int x = player.getX();
        int y = player.getY();
        char[][] grid = map.getMap();
        int gold = player.getGoldOwned();
        if (grid[y][x] == ('G')) {
            player.updateGoldOwned();
            map.updateMap('G', y, x);
            return("SUCCESS. Gold Owned: " + (gold+1));
        }
        else{
            return("FAIL. Gold Owned: " + gold);
        }
    }

    /**
     * Checks if the player has won - they have the gold required and they are on an exit tile when they input EXIT.
     */

    protected boolean checkWin() {
        char[][] grid = map.getMap();
        int x = player.getX();
        int y = player.getY();
        if (grid[y][x] == 'E' && player.getGoldOwned() == map.getGoldRequired()) {
            return true;
        }
        else{
            return false;
        }
    }

}

