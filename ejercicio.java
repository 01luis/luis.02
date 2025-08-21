
import java. io. BufferedReader; ..
import java. IOException
import java.nio.charset.StandardCharsets
import java.nio.Files.Files
import java.nio.Files.Path
import java.nio.Paths

public class F {
public void read(){
Path ruta = Paths.get(first:"note.txt");
try (BufferedReader br = Files.newBufferedReader(ruta, StandardCharsets.UTF_8)) {
String linea;
while ((linea = br.readLine()) != null) {
System.out.println(linea);
}
 catch (IOException e) {
e.printStackTrace();
}
}
}}
Run | Debug
public static void main(String[] args) {
F f =new F();
f.read();

}