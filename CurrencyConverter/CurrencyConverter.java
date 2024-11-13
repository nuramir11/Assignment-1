import java.util.Scanner;

public class CurrencyConverter {

    public static double convertCurrency(double amount, double rate) {
        return amount * rate;
    }

    public static void displayConversion(double amount, double converted, String currency) {
        System.out.printf("%.2f in %s is %.2f%n", amount, currency, converted);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the amount: ");
        double amount = scanner.nextDouble();
        System.out.print("Enter the target currency (e.g. USD, EUR): ");
        String currency = scanner.next();
        System.out.print("Enter the course for " + currency + ": ");
        double rate = scanner.nextDouble();
        double converted = convertCurrency(amount, rate);
        displayConversion(amount, converted, currency);
        scanner.close();
    }
}
