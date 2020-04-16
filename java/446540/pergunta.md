Meu algoritmo em todos os testes de `println`, está funcionando e na lógica também porém, os números após a vírgula ele não demonstra

    public class Exe27 {
    
    	public static void main(String[] args) {
    		// TODO Auto-generated method stub
    
    		Scanner scan = new Scanner (System.in);
    		
    		int dividendo = 1;
    		int numero = 0;
    		double numHarmonico = 0;
    		
    		System.out.println("Sistema Harmônico");
    		System.out.println("Digite em até que número a série irá");
    		numero =scan.nextInt();
    		
    		for(int i = 1;i <= numero; i++) {
    			
    			numHarmonico += dividendo/i;
    		}
    		
    		System.out.printf("%.2f", numHarmonico);
    		scan.close();
    	}
       
    }

