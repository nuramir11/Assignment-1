import java.util.Scanner;

public class MultiplicationTableGenerator {

    public static void generateTable(int number) {
        for (int i = 1; i <= 10; i++) {
            System.out.println(number + " x " + i + " = " + (number * i));
        }
    }

    public static void displayTables(int start, int end) {
        for (int number = start; number <= end; number++) {
            System.out.println("\nThe multiplication table for " + number + ":");
            generateTable(number);
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the starting number: ");
        int start = scanner.nextInt();
        System.out.print("Enter a finite number: ");
        int end = scanner.nextInt();
        displayTables(start, end);
        scanner.close();
    }
}
