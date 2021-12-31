public class ValueMain {
    public static void main(String[] args) {
        int number=10;
        int num=count(number);
        System.out.printf("num is %d%n", num);
        System.out.printf("number is %d%n", number);
        //这里的%n是换行的格式字符串
        String message="message";
        String message2=concat(message);
        System.out.println(message);
        System.out.println(message2);
    }

    public static int count(int number){
        for (int i=0;i<10;i++){
            number++;
        }
        return number;
    }
    /** code running result :
     * num is 20
     * number is 10
     */

    public static String concat(String message){
        message+=" concat ";
        return message;
    }
    /** code running result :
     * message
     * message concat
     */
}
