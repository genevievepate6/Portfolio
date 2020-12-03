import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
/**
 * Reads and contains in memory the map of the game.
 *
 */
public class Map {

    /* Representation of the map */
    private char[][] map;
    /* Map name */
    private String mapName;
    /* Number of rows in map */
    private int rows;
    /* Number of columns in map */
    private int columns;
    /* Gold required for the human player to win */
    private int goldRequired;

    /**
     * Default constructor, creates the default map.
     */
    public Map (int rows, int columns) {
        this.rows = rows;
        this.columns = columns;
        goldRequired = 2;
        map = new char[][]{
                {'#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#'},
                {'#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#'},
                {'#','.','.','.','.','.','.','G','.','.','.','.','.','.','.','.','.','E','.','#'},
                {'#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#'},
                {'#','.','.','E','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#'},
                {'#','.','.','.','.','.','.','.','.','.','.','.','G','.','.','.','.','.','.','#'},
                {'#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#'},
                {'#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#'},
                {'#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#'}
        };
    }

    /**
     * @return : Gold required to exit the current map.
     */
    protected int getGoldRequired() {
        return goldRequired;
    }
    /**
     * @return : The map as stored in memory.
     */
    protected char[][] getMap() {
        return map;
    }
    /**
     * @return : The name of the current map.
     */
    protected String getMapName() {
        return mapName;
    }

    /**
     * Changes a tile to an empty tile.
     *
     * @param toChange : what tile is being changed.
     * @param y : the y coordinate of that tile
     * @param x : the x coordinate f that tile
     */

    public void updateMap(char toChange, int y, int x){
        if (toChange == 'G'){
            map[y][x] = '.';
        }
    }
}
