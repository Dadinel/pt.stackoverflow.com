import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner (System.in);

        int dividendo = 1;
        int numero = 0;
        double numHarmonico = 0;

        System.out.println("Sistema Harmônico");
        System.out.println("Digite em até que número a série irá");
        numero =scan.nextInt();

        for(int i = 1;i <= numero; i++) {
            // Outra forma de conversão...
            // numHarmonico += Double.valueOf(dividendo)/i;
            numHarmonico += (double)dividendo/i;
        }

        System.out.printf("%.2f", numHarmonico);
        scan.close();
    }
}
