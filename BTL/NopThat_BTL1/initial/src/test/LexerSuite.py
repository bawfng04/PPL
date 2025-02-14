import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    def test_float_literal(self):
        """test float literals"""
        self.assertTrue(TestLexer.checkLexeme("1.23","1.23,<EOF>",1))
    def test_array_declaration(self):
        """test array declaration"""
        self.assertTrue(TestLexer.checkLexeme("[2][3]int","[,2,],[,3,],int,<EOF>",2))
    def test_operators(self):
        """test operators"""
        self.assertTrue(TestLexer.checkLexeme("a += b *= c /= d","a,+=,b,*=,c,/=,d,<EOF>",3))
    def test_struct_declaration(self):
        """test struct declaration"""
        self.assertTrue(TestLexer.checkLexeme("type Point struct { x int }","type,Point,struct,{,x,int,},<EOF>",4))
    def test_interface_declaration(self):
        """test interface declaration"""
        self.assertTrue(TestLexer.checkLexeme("type Shape interface { area() float }","type,Shape,interface,{,area,(,),float,},<EOF>",5))
    def test_for_range(self):
        """test for range statement"""
        self.assertTrue(TestLexer.checkLexeme("for i := range nums","for,i,:=,range,nums,<EOF>",6))
    def test_logical_operators(self):
        """test logical operators"""
        self.assertTrue(TestLexer.checkLexeme("a && b || !c","a,&&,b,||,!,c,<EOF>",7))
    def test_logical_operators(self):
        """test logical operators"""
        self.assertTrue(TestLexer.checkLexeme("a && b || !c","a,&&,b,||,!,c,<EOF>",8))
    def test_multiple_operators(self):
        """test multiple operators in sequence"""
        self.assertTrue(TestLexer.checkLexeme("1 + 2 * 3 / 4","1,+,2,*,3,/,4,<EOF>",9))

    def test_comparison_operators(self):
        """test comparison operators"""
        self.assertTrue(TestLexer.checkLexeme("a <= b >= c == d","a,<=,b,>=,c,==,d,<EOF>",10))

    def test_nested_blocks(self):
        """test nested block structures"""
        self.assertTrue(TestLexer.checkLexeme("{ { } }","{,{,},},<EOF>",11))

    def test_multi_declarations(self):
        """test multiple variable declarations"""
        self.assertTrue(TestLexer.checkLexeme("var x, y, z int","var,x,,,y,,,z,int,<EOF>",12))

    def test_function_params(self):
        """test function with parameters"""
        self.assertTrue(TestLexer.checkLexeme("func add(x int, y float)","func,add,(,x,int,,,y,float,),<EOF>",13))

    def test_array_access(self):
        """test array access"""
        self.assertTrue(TestLexer.checkLexeme("arr[i][j]","arr,[,i,],[,j,],<EOF>",14))

    def test_struct_method(self):
        """test struct method declaration"""
        self.assertTrue(TestLexer.checkLexeme("func (p Point) distance()","func,(,p,Point,),distance,(,),<EOF>",15))

    def test_bool_literals(self):
        """test boolean literals"""
        self.assertTrue(TestLexer.checkLexeme("true false","true,false,<EOF>",16))

    def test_nil_literal(self):
        """test nil literal"""
        self.assertTrue(TestLexer.checkLexeme("nil","nil,<EOF>",17))

    def test_complex_expression(self):
        """test complex expression"""
        self.assertTrue(TestLexer.checkLexeme("a + b * (c - d)","a,+,b,*,(,c,-,d,),<EOF>",18))

    def test_multi_statements(self):
        """test multiple statements"""
        self.assertTrue(TestLexer.checkLexeme("x = 1; y = 2;","x,=,1,;,y,=,2,;,<EOF>",19))

    def test_comments(self):
        """test comments handling"""
        self.assertTrue(TestLexer.checkLexeme("x = 1 // this is comment","x,=,1,<EOF>",20))

    def test_mixed_expressions(self):
        """test mixed type expressions"""
        self.assertTrue(TestLexer.checkLexeme("1 + 2.5","1,+,2.5,<EOF>",21))
    def test_mixed_expressions(self):
        """test mixed type expressions"""
        self.assertTrue(TestLexer.checkLexeme("1 + 2.5","1,+,2.5,<EOF>",22))
    def test_interface_method(self):
        """test interface method declaration"""
        self.assertTrue(TestLexer.checkLexeme("draw() int","draw,(,),int,<EOF>",23))

    def test_range_loop(self):
        """test range-based loop"""
        self.assertTrue(TestLexer.checkLexeme("for _, val := range arr","for,_,,,val,:=,range,arr,<EOF>",24))

    def test_multiple_assigns(self):
        """test multiple assignments"""
        self.assertTrue(TestLexer.checkLexeme("a, b = 1, 2","a,,,b,=,1,,,2,<EOF>",25))
    def test_hex_literal(self):
        """test hexadecimal literals"""
        self.assertTrue(TestLexer.checkLexeme("0xFF","0xFF,<EOF>",26))

    def test_octal_literal(self):
        """test octal literals"""
        self.assertTrue(TestLexer.checkLexeme("0o77","0o77,<EOF>",27))

    def test_binary_literal(self):
        """test binary literals"""
        self.assertTrue(TestLexer.checkLexeme("0b1010","0b1010,<EOF>",28))

    def test_float_exponent(self):
        """test float with exponent"""
        self.assertTrue(TestLexer.checkLexeme("1.23e-4","1.23e-4,<EOF>",29))

    def test_empty_block(self):
        """test empty block"""
        self.assertTrue(TestLexer.checkLexeme("{}","{,},<EOF>",30))

    def test_multiline_comment(self):
        """test multiline comment"""
        self.assertTrue(TestLexer.checkLexeme("/* This is\na comment */","<EOF>",31))

    def test_increment_assign(self):
        """test increment assignment"""
        self.assertTrue(TestLexer.checkLexeme("count += 1","count,+=,1,<EOF>",32))

    def test_array_literal(self):
        """test array literal"""
        self.assertTrue(TestLexer.checkLexeme("[1,2,3]","[,1,,,2,,,3,],<EOF>",33))

    def test_struct_literal(self):
        """test struct literal"""
        self.assertTrue(TestLexer.checkLexeme("Point{x: 1, y: 2}","Point,{,x,:,1,,,y,:,2,},<EOF>",34))

    def test_slice_operation(self):
        """test slice operation"""
        self.assertTrue(TestLexer.checkLexeme("arr[1:5]","arr,[,1,:,5,],<EOF>",35))

    def test_semicolon_separation(self):
        """test semicolon separation"""
        self.assertTrue(TestLexer.checkLexeme("a;b;c","a,;,b,;,c,<EOF>",36))

    def test_type_conversion(self):
        """test type conversion"""
        self.assertTrue(TestLexer.checkLexeme("float(x)","float,(,x,),<EOF>",37))

    def test_interface_empty(self):
        """test empty interface"""
        self.assertTrue(TestLexer.checkLexeme("interface {}","interface,{,},<EOF>",38))

    def test_interface_empty(self):
        """test empty interface"""
        self.assertTrue(TestLexer.checkLexeme("interface {}","interface,{,},<EOF>",39))
    def test_interface_empty(self):
        """test empty interface"""
        self.assertTrue(TestLexer.checkLexeme("interface {}","interface,{,},<EOF>",40))




    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))
    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme("ab?sVN","ab,ErrorToken ?",102))
    def test_keyword_var(self):
        """test keyword var"""
        self.assertTrue(TestLexer.checkLexeme("var abc int ;","var,abc,int,;,<EOF>",103))
    def test_keyword_func(self):
        """test keyword func"""
        self.assertTrue(TestLexer.checkLexeme("""func abc ( ) ""","""func,abc,(,),<EOF>""",104))
    def test_keyword_return(self):
        """test keyword return"""
        self.assertTrue(TestLexer.checkLexeme("return 1 ;","return,1,;,<EOF>",105))

