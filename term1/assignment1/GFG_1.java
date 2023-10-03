public class GFG_1 {

public static void main(String[] args)
    {
        // declares an Array of integers.
        int[] arr;
 
        // allocating memory for 5 integers.
        arr = new int[0];
        int count = 0;
        // initialize the first elements of the array
        int i = 10;
        count ++;

        int [] tempArr = new int [count];
        tempArr [count-1] = i;
        arr = tempArr;
 
        // initialize the second elements of the array
        i = 20;
 
        count ++;

        tempArr = new int [count];
        tempArr = arr;
        tempArr [count-1] = i;
        arr = tempArr;

        
        i = 30;
        
        count ++;

        tempArr = new int [count];
        tempArr = arr;
        tempArr [count-1] = i;
        arr = tempArr;
        
        
        i = 40;
        
        count ++;

        tempArr = new int [count];
        tempArr = arr;
        tempArr [count-1] = i;
        arr = tempArr;
        
        
        i = 50;

        count ++;

        tempArr = new int [count];
        tempArr = arr;
        tempArr [count-1] = i;
        arr = tempArr;

 
        // accessing the elements of the specified array
        for (int j = 0; j < arr.length; j++)
            System.out.println("Element at index " + j
                               + " : " + arr[j]);
    }

}