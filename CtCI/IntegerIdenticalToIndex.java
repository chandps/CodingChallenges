/**
 * Problem: Integers in an array are unique and increasingly sorted. Please write a function/method to find an integer from the array who equals to its index. For example, in the array {-3, -1, 1, 3, 5}, the number 3 equals its index 3.
 */
public class IntegerIdenticalToIndex{
    public static void main(){
    public static void main(String[] args)
    {
        int[] a = {-3,-2,2,4};
        System.out.println(getNumberSameAsIndex(a));
    }

    public static int getNumberSameAsIndex(int[] numbers){
        if(numbers.length == 0 || numbers == null) return -1;

        int left = 0;
        int right = numbers.length - 1;
        int middle;
        while(left <= right){
        middle = left + ((right - left) / 2);

        if(numbers[middle] == middle) return middle;
        if(numbers[middle] > middle) right = middle-1 ;
        else left = middle+1;
    }
    return -1;
    }
}
