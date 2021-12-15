public class Main {
    public static void main(String[] args) {
        RequestQueue requestQueue = new RequestQueue();
        new ServerThread(requestQueue, "Bobby", 6535897L).start();
        new ClientThread(requestQueue, "Alice", 3141592L).start();
    }
}
