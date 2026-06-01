import java.awt.*;
import java.util.HashSet;
import java.util.Set;

public class PlayBoard {
    private int[][] board;
    private int size;
    private int NUM_BOMBS;

    public PlayBoard(int size) {
        this.size = size;
        this.NUM_BOMBS = size * 4;
    }

    public int[][] generateBoard() {
        this.board = new int[size][size];

        // set bombs
        Set<Point> bombList = getBombList();
        for (int r = 0; r < size; r++) {
            for (int c = 0; c < size; c++) {
                // if location is in bombList, place a bomb (-1)
                Point temp = new Point(r, c);
                if (bombList.contains(temp)) {
                    board[r][c] = -1;
                }
            }
        }

        // count number of nearby bombs
        for (int r = 0; r < size; r++) {
            for (int c = 0; c < size; c++) {
                if (board[r][c] != -1) {
                    int nearbyBombs = 0;
                    // check up
                    if (r - 1 >= 0 && board[r - 1][c] == -1) {
                        nearbyBombs++;
                    }
                    // check down
                    if (r + 1 < size && board[r + 1][c] == -1) {
                        nearbyBombs++;
                    }
                    // check left
                    if (c - 1 >= 0 && board[r][c - 1] == -1) {
                        nearbyBombs++;
                    }
                    // check right
                    if (c + 1 < size && board[r][c + 1] == -1) {
                        nearbyBombs++;
                    }
                    // check top left
                    if (r - 1 >= 0 && c - 1 >= 0 && board[r - 1][c - 1] == -1) {
                        nearbyBombs++;
                    }
                    // check top right
                    if (r - 1 >= 0 && c + 1 < size && board[r - 1][c + 1] == -1) {
                        nearbyBombs++;
                    }
                    // check bottom left
                    if (r + 1 < size && c - 1 >= 0 && board[r + 1][c - 1] == -1) {
                        nearbyBombs++;
                    }
                    // check bottom right
                    if (r + 1 < size && c + 1 < size && board[r + 1][c + 1] == -1) {
                        nearbyBombs++;
                    }
                    board[r][c] = nearbyBombs;
                }
            }
        }
        return board;
    }

    // get the locations of the bombs
    public Set<Point> getBombList(){
        Set<Point> list = new HashSet<>(size);

        // add NUM_BOMBS points to set
        for (int x = 0; x < NUM_BOMBS; x++) {
            Point p = getBomb();
            // if the set already contains point (duplicate), deprecate x
            if (!list.add(p)) {
                x--;
            }
        }

        return list;
    }

    // return one point representing a bomb on the board
    public Point getBomb() {
        int x = (int) (Math.random() * size);
        int y = (int) (Math.random() * size);
        return new Point(x, y);
    }
}