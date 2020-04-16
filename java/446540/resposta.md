Assim como o @Maniero já falou, o problema está na divisão de inteiros.

Uma outra possibilidade, é converter o valor durante a divisão:

    numHarmonico += Double.valueOf(dividendo)/i;

Ou

    numHarmonico += (double)dividendo/i;

Isso é apenas um exemplo, tenha em mente que a cada iteração você fará um cast.


----------

O código completo ficaria mais ou menos da seguinte forma:

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
                // Outro exemplo de conversão
                // numHarmonico += Double.valueOf(dividendo)/i;
                numHarmonico += (double)dividendo/i;
            }
    
            System.out.printf("%.2f", numHarmonico);
            scan.close();
        }
    }

> Veja online: https://repl.it/repls/WorthlessBleakScientist
