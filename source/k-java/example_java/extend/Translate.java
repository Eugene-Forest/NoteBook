
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;

public class Translate {

	/**
	 * 对象转换为字节数组形式，实现对向的序列化
	 * @param obj 为待转换对象
	 * @return 字节数组
	 */
	public static byte [] ObjectToByte(Object obj) {
		byte[] buffer=null;
		
		try {
			//字节数组输出流
			ByteArrayOutputStream bo=new ByteArrayOutputStream();
			//对象输出流
			ObjectOutputStream oo=new ObjectOutputStream(bo);
			oo.writeObject(obj);
			buffer=bo.toByteArray();
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		
		return buffer;
	}
}
