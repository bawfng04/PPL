.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static sumAges(LPerson;LPerson;)I
Label0:
.var 0 is p1 LPerson; from Label0 to Label1
.var 1 is p2 LPerson; from Label0 to Label1
Label2:
	aload_0
	getfield Person/age I
	aload_1
	getfield Person/age I
	iadd
	ireturn
Label3:
Label1:
.limit stack 2
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is p1 LPerson; from Label2 to Label3
	new Person
	dup
	ldc "Dan"
	bipush 20
	invokespecial Person/<init>(Ljava/lang/String;I)V
	astore 1
.var 2 is p2 LPerson; from Label2 to Label3
	new Person
	dup
	ldc "Eve"
	bipush 25
	invokespecial Person/<init>(Ljava/lang/String;I)V
	astore 2
.var 3 is total I from Label2 to Label3
	aload_1
	aload_2
	invokestatic MiniGoClass/sumAges(LPerson;LPerson;)I
	istore 3
	iload_3
	invokestatic io/putIntLn(I)V
Label3:
Label1:
	return
.limit stack 5
.limit locals 4
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
Label3:
Label1:
	return
.limit stack 0
.limit locals 0
.end method
