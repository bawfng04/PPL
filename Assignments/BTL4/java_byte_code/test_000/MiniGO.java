//! lệnh dịch sang .class -> javac MiniGO
//! lệnh dịch .class sang .j -> java -jar ../classfileanalyzer.jar -file MiniGO.class
//! lệnh dịch print kết quả -> java -cp ../_io:. MiniGO
//! lệnh dịch từ .j sang .class -> java  -jar ../jasmin.jar MiniGO.j

public class MiniGO {
    public static void main(String[] args) {
        io.putIntLn("apple".compareTo("banana"));
    }
}
