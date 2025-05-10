.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static a I
.field static c I

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is b [[I from Label2 to Label3
	aload_1
	iconst_0
	aaload
	iconst_0
	iaload
	invokestatic io/putInt(I)V
	aload_1
	iconst_0
	aaload
	iconst_0
	bipush 20
	iastore
	aload_1
	iconst_0
	aaload
	iconst_0
	iaload
	invokestatic io/putInt(I)V
Label3:
Label1:
	return
.limit stack 4
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LMiniGoClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static <clinit>()V
Label0:
Label2:
	iconst_1
	iconst_1
	iadd
	putstatic MiniGoClass/a I
	iconst_5
	getstatic MiniGoClass/a I
	isub
	putstatic MiniGoClass/c I
Label3:
Label1:
	return
.limit stack 3
.limit locals 0
.end method
