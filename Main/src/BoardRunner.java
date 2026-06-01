import java.util.Arrays;

public class BoardRunner {

    public static void main(String[] args) {
        PlayBoard board = new PlayBoard(10);
        int[][] boardDisplay = board.generateBoard();

        for (int r = 0; r < boardDisplay.length; r++) {
            for (int c = 0; c < boardDisplay[r].length; c++) {
                System.out.printf("%3d ", boardDisplay[r][c]);
            }
            System.out.println();
        }
    }
}
