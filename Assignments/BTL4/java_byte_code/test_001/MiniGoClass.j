.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static global I

.method public static fvoid()V
Label0:
Label2:
	ldc "VoTien"
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label3:
Label1:
	return
.limit stack 1
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
	invokestatic MiniGoClass/fvoid()V
	getstatic MiniGoClass/global I
	i2f
	fconst_2
	fadd
	invokestatic io/putFloatLn(F)V
.var 1 is local Ljava/lang/String; from Label2 to Label3
	ldc "a"
	astore_1
	aload_1
	ldc "b"
	invokevirtual java/lang/String/compareTo(Ljava/lang/String;)I
	iconst_0
	if_icmpgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	invokestatic io/putBoolLn(Z)V
	aload_1
	ldc "c"
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	astore_1
	aload_1
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label3:
Label1:
	return
.limit stack 4
.limit locals 2
.end method

.method public static fint()I
Label0:
Label2:
	iconst_1
	ireturn
Label3:
Label1:
.limit stack 1
.limit locals 0
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
	invokestatic MiniGoClass/fint()I
	putstatic MiniGoClass/global I
Label3:
Label1:
	return
.limit stack 1
.limit locals 0
.end method
