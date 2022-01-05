import java.util.Queue;
import java.util.LinkedList;

public class RequestQueue {
    private final Queue<Request> queue = new LinkedList<Request>();

    public synchronized Request getRequest() {
        // 确认队列是否为空
        while (queue.peek() == null) {
            try {
                wait();
            } catch (InterruptedException e) {
            }
        }
        // 将队列中的第一个/头部对象取出
        return queue.remove();
    }

    public synchronized void putRequest(Request request) {
        // 向队列尾部中添加request
        queue.offer(request);
        notifyAll();
    }
}
