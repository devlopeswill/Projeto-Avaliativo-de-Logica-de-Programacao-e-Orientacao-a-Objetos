public class Ex {
    public static void main(String[] args){

        try{
            int[] vetor = new int [10];
            System.out;
            vetor[11] = 10;
            System.out.println("error");
        } catch(ArrayIndexOutOfBoundsException exception){
            System.out.println("indice vetor não existe");
        }
        
    }
}
