public class SetZeroMatrix{
    public static void main(){
    public static void main(String[] args)
    {
        int[] a = {-3,-2,2,4};
        System.out.println(getNumberSameAsIndex(a));
    }

    public static void zeroMatrix(int[][] numbers){
        boolean[] zeroX = new boolean[numbers.length];
        boolean[] zeroY = new boolean[numbers.length];

        /** check every zeros in the matrix */
        for (int Y = 0; Y < numbers.length ; Y++) {
            for (int X = 0; X < numbers.length ; X++) {
                if (numbers[X][Y]) {
                    zeroX[X] = true;
                    zeroX[Y] = true;
                }
            }
        }

        /** Update the matrix into zeros */
        for (int Y = 0; Y < numbers.length ; Y++) {
            for (int X = 0; X < numbers.length ; X++) {
                if (zeroX[X]||zeroY[Y]) {
                    numbers[X][Y] = true;
                }
            }
        }
    }
}
