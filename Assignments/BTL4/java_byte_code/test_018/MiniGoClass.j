.source MiniGoClass.java
.class public MiniGoClass
.super java/lang/Object

.method public static <clinit>()V
Label0:
Label1:
	return
.limit stack 0
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

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is a LPPL3; from Label2 to Label3
	new PPL3
	dup
	invokespecial PPL3/<init>()V
	dup
	iconst_1
	putfield PPL3/number I
	astore_1
	aload_1
	invokevirtual PPL3/study()V
	aload_1
	invokevirtual PPL3/play()V
Label3:
Label1:
	return
.limit stack 3
.limit locals 2
.end method
