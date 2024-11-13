import java.util.Scanner;

public class FlightReservationSystem {

    private static final int ROWS = 5;
    private static final int COLS = 4;
    private static String[][] seats = new String[ROWS][COLS];

    public static void initializeSeats() {
        for (int i = 0; i < ROWS; i++) {
            for (int j = 0; j < COLS; j++) {
                seats[i][j] = "O";
            }
        }
    }

    public static void displaySeats() {
        for (String[] row : seats) {
            for (String seat : row) {
                System.out.print(seat + " ");
            }
            System.out.println();
        }
    }

    public static void bookSeat(int row, int col) {
        if (seats[row][col].equals("O")) {
            seats[row][col] = "X";
            System.out.println("The place is reserved.");
        } else {
            System.out.println("The seat's already taken.");
        }
    }

    public static void cancelReservation(int row, int col) {
        if (seats[row][col].equals("X")) {
            seats[row][col] = "O";
            System.out.println("Reservation canceled.");
        } else {
            System.out.println("This place was not booked.");
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        initializeSeats();

        while (true) {
            System.out.println("\nCurrent venues:");
            displaySeats();
            System.out.print("Enter 'book' to book, 'cancel' to cancel or 'exit' to exit: ");
            String action = scanner.next();

            if (action.equals("book")) {
                System.out.print("Enter the seat number (1-5): ");
                int row = scanner.nextInt() - 1;
                System.out.print("Enter the seat number (1-4): ");
                int col = scanner.nextInt() - 1;
                bookSeat(row, col);
            } else if (action.equals("cancel")) {
                System.out.print("Enter the number  of seat to cancel (1-5):");
                int row = scanner.nextInt() - 1;
                System.out.print("Enter the number of the seat to cancel (1-4): ");
                int col = scanner.nextInt() - 1;
                cancelReservation(row, col);
            } else if (action.equals("exit")) {
                break;
            } else {
                System.out.println("Incorrect command.");
            }
        }

        scanner.close();
    }
}
