//! lệnh dịch .java sang .class -> javac VoTien.java
//! lệnh dịch .class sang .j -> java -jar ../external/classfileanalyzer.jar -file VoTien.class
//! lệnh dịch print kết quả -> java VoTien
//! lệnh dịch từ .j sang .class -> java  -jar ../external/jasmin.jar VoTien.j

public class VoTien {
    public static void main(String[] args) {
        System.err.println("VoTien");
    }
}