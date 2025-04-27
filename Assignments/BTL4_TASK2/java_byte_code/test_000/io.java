// Source code is decompiled from a .class file using FernFlower decompiler.
import java.util.Scanner;

public class io {
   private static final Scanner scanner;

   public io() {
   }

   public static int getInt() {
      return scanner.nextInt();
   }

   public static void putInt(int var0) {
      System.out.print(var0);
   }

   public static void putIntLn(int var0) {
      System.out.println(var0);
   }

   public static float getFloat() {
      return scanner.nextFloat();
   }

   public static void putFloat(float var0) {
      System.out.print(var0);
   }

   public static void putFloatLn(float var0) {
      System.out.println(var0);
   }

   public static boolean getBool() {
      return scanner.nextBoolean();
   }

   public static void putBool(boolean var0) {
      System.out.print(var0);
   }

   public static void putBoolLn(boolean var0) {
      System.out.println(var0);
   }

   public static String getString() {
      return scanner.next();
   }

   public static void putString(String var0) {
      System.out.print(var0);
   }

   public static void putStringLn(String var0) {
      System.out.println(var0);
   }

   public static void putLn() {
      System.out.println();
   }

   static {
      scanner = new Scanner(System.in);
   }
}
