//Program to find all Prime numbers between 1 and 100

//import java.util.Scanner;
import java.util.ArrayList;

public class Q14 {

public static void main (String[] args){
  //  Scanner sc = new Scanner(System.in);
    
   
    
    ArrayList<Integer> primes = new ArrayList<Integer>(); 
    var lenPrimes = 0;

    
    for (int i=2; i<101; i++) {
        int factors = 0;
        for(int j=2; i>j; j++){            
            if (i != j){
                if ((i % j) == 0 ){
                    factors++;
                }    
            }    
        }    

    if (i>2 && factors == 0) {   // i is a prime number

            primes.add(i);       
        
                    /*int [] tempPrimes = new int [lenPrimes+1];
                    if (lenPrimes > 0) {
                        tempPrimes = primes;                        
                    } else {

                    }

                    tempPrimes [lenPrimes] = i;
                    primes = tempPrimes;
                    lenPrimes++;
                    */
            
        }
 

    }



    

//Print prime numbers
for (int i=0; i<primes.size(); i++){
    System.out.println(primes.get(i));
    
}


}

}