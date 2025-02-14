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
    def test_interface_empty2(self):
        """test empty interface"""
        self.assertTrue(TestLexer.checkLexeme("interface {}","interface,{,},<EOF>",41))

    def test_float_literal_42(self):
        """test float literals"""
        self.assertTrue(TestLexer.checkLexeme("1.23","1.23,<EOF>",42))

    def test_array_declaration_43(self):
        """test array declaration"""
        self.assertTrue(TestLexer.checkLexeme("[2][3]int","[,2,],[,3,],int,<EOF>",43))

    def test_operators_44(self):
        """test operators"""
        self.assertTrue(TestLexer.checkLexeme("a += b *= c /= d","a,+=,b,*=,c,/=,d,<EOF>",44))

    def test_struct_declaration_45(self):
        """test struct declaration"""
        self.assertTrue(TestLexer.checkLexeme("type Point struct { x int }","type,Point,struct,{,x,int,},<EOF>",45))

    def test_interface_declaration_46(self):
        """test interface declaration"""
        self.assertTrue(TestLexer.checkLexeme("type Shape interface { area() float }","type,Shape,interface,{,area,(,),float,},<EOF>",46))

    def test_for_range_47(self):
        """test for range statement"""
        self.assertTrue(TestLexer.checkLexeme("for i := range nums","for,i,:=,range,nums,<EOF>",47))

    def test_logical_operators_48(self):
        """test logical operators"""
        self.assertTrue(TestLexer.checkLexeme("a && b || !c","a,&&,b,||,!,c,<EOF>",48))

    def test_multiple_operators_49(self):
        """test multiple operators in sequence"""
        self.assertTrue(TestLexer.checkLexeme("1 + 2 * 3 / 4","1,+,2,*,3,/,4,<EOF>",49))

    def test_comparison_operators_50(self):
        """test comparison operators"""
        self.assertTrue(TestLexer.checkLexeme("a <= b >= c == d","a,<=,b,>=,c,==,d,<EOF>",50))

    def test_nested_blocks_51(self):
        """test nested block structures"""
        self.assertTrue(TestLexer.checkLexeme("{ { } }","{,{,},},<EOF>",51))

    def test_multi_declarations_52(self):
        """test multiple variable declarations"""
        self.assertTrue(TestLexer.checkLexeme("var x, y, z int","var,x,,,y,,,z,int,<EOF>",52))

    def test_function_params_53(self):
        """test function with parameters"""
        self.assertTrue(TestLexer.checkLexeme("func add(x int, y float)","func,add,(,x,int,,,y,float,),<EOF>",53))

    def test_array_access_54(self):
        """test array access"""
        self.assertTrue(TestLexer.checkLexeme("arr[i][j]","arr,[,i,],[,j,],<EOF>",54))

    def test_struct_method_55(self):
        """test struct method declaration"""
        self.assertTrue(TestLexer.checkLexeme("func (p Point) distance()","func,(,p,Point,),distance,(,),<EOF>",55))

    def test_bool_literals_56(self):
        """test boolean literals"""
        self.assertTrue(TestLexer.checkLexeme("true false","true,false,<EOF>",56))

    def test_nil_literal_57(self):
        """test nil literal"""
        self.assertTrue(TestLexer.checkLexeme("nil","nil,<EOF>",57))

    def test_complex_expression_58(self):
        """test complex expression"""
        self.assertTrue(TestLexer.checkLexeme("a + b * (c - d)","a,+,b,*,(,c,-,d,),<EOF>",58))

    def test_multi_statements_59(self):
        """test multiple statements"""
        self.assertTrue(TestLexer.checkLexeme("x = 1; y = 2;","x,=,1,;,y,=,2,;,<EOF>",59))

    def test_comments_60(self):
        """test comments handling"""
        self.assertTrue(TestLexer.checkLexeme("x = 1 // this is comment","x,=,1,<EOF>",60))

    def test_mixed_expressions_61(self):
        """test mixed type expressions"""
        self.assertTrue(TestLexer.checkLexeme("1 + 2.5","1,+,2.5,<EOF>",61))

    def test_interface_method_62(self):
        """test interface method declaration"""
        self.assertTrue(TestLexer.checkLexeme("draw() int","draw,(,),int,<EOF>",62))

    def test_range_loop_63(self):
        """test range-based loop"""
        self.assertTrue(TestLexer.checkLexeme("for _, val := range arr","for,_,,,val,:=,range,arr,<EOF>",63))

    def test_multiple_assigns_64(self):
        """test multiple assignments"""
        self.assertTrue(TestLexer.checkLexeme("a, b = 1, 2","a,,,b,=,1,,,2,<EOF>",64))

    def test_hex_literal_65(self):
        """test hexadecimal literals"""
        self.assertTrue(TestLexer.checkLexeme("0xFF","0xFF,<EOF>",65))

    def test_octal_literal_66(self):
        """test octal literals"""
        self.assertTrue(TestLexer.checkLexeme("0o77","0o77,<EOF>",66))

    def test_binary_literal_67(self):
        """test binary literals"""
        self.assertTrue(TestLexer.checkLexeme("0b1010","0b1010,<EOF>",67))

    def test_float_exponent_68(self):
        """test float with exponent"""
        self.assertTrue(TestLexer.checkLexeme("1.23e-4","1.23e-4,<EOF>",68))

    def test_empty_block_69(self):
        """test empty block"""
        self.assertTrue(TestLexer.checkLexeme("{}","{,},<EOF>",69))

    def test_multiline_comment_70(self):
        """test multiline comment"""
        self.assertTrue(TestLexer.checkLexeme("/* This is\na comment */","<EOF>",70))

    def test_increment_assign_71(self):
        """test increment assignment"""
        self.assertTrue(TestLexer.checkLexeme("count += 1","count,+=,1,<EOF>",71))

    def test_array_literal_72(self):
        """test array literal"""
        self.assertTrue(TestLexer.checkLexeme("[1,2,3]","[,1,,,2,,,3,],<EOF>",72))

    def test_struct_literal_73(self):
        """test struct literal"""
        self.assertTrue(TestLexer.checkLexeme("Point{x: 1, y: 2}","Point,{,x,:,1,,,y,:,2,},<EOF>",73))

    def test_slice_operation_74(self):
        """test slice operation"""
        self.assertTrue(TestLexer.checkLexeme("arr[1:5]","arr,[,1,:,5,],<EOF>",74))

    def test_semicolon_separation_75(self):
        """test semicolon separation"""
        self.assertTrue(TestLexer.checkLexeme("a;b;c","a,;,b,;,c,<EOF>",75))

    def test_type_conversion_76(self):
        """test type conversion"""
        self.assertTrue(TestLexer.checkLexeme("float(x)","float,(,x,),<EOF>",76))

    def test_interface_empty_77(self):
        """test empty interface"""
        self.assertTrue(TestLexer.checkLexeme("interface {}","interface,{,},<EOF>",77))

    def test_lower_identifier_78(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",78))

    def test_wrong_token_79(self):
        self.assertTrue(TestLexer.checkLexeme("ab?sVN","ab,ErrorToken ?",79))

    def test_keyword_var_80(self):
        """test keyword var"""
        self.assertTrue(TestLexer.checkLexeme("var abc int ;","var,abc,int,;,<EOF>",80))

    def test_keyword_func_81(self):
        """test keyword func"""
        self.assertTrue(TestLexer.checkLexeme("""func abc ( ) ""","""func,abc,(,),<EOF>""",81))

    def test_keyword_return_82(self):
        """test keyword return"""
        self.assertTrue(TestLexer.checkLexeme("return 1 ;","return,1,;,<EOF>",82))

    def test_float_literal_83(self):
        """test float literals"""
        self.assertTrue(TestLexer.checkLexeme("1.23","1.23,<EOF>",83))

    def test_array_declaration_84(self):
        """test array declaration"""
        self.assertTrue(TestLexer.checkLexeme("[2][3]int","[,2,],[,3,],int,<EOF>",84))

    def test_operators_85(self):
        """test operators"""
        self.assertTrue(TestLexer.checkLexeme("a += b *= c /= d","a,+=,b,*=,c,/=,d,<EOF>",85))

    def test_struct_declaration_86(self):
        """test struct declaration"""
        self.assertTrue(TestLexer.checkLexeme("type Point struct { x int }","type,Point,struct,{,x,int,},<EOF>",86))

    def test_interface_declaration_87(self):
        """test interface declaration"""
        self.assertTrue(TestLexer.checkLexeme("type Shape interface { area() float }","type,Shape,interface,{,area,(,),float,},<EOF>",87))

    def test_for_range_88(self):
        """test for range statement"""
        self.assertTrue(TestLexer.checkLexeme("for i := range nums","for,i,:=,range,nums,<EOF>",88))

    def test_logical_operators_89(self):
        """test logical operators"""
        self.assertTrue(TestLexer.checkLexeme("a && b || !c","a,&&,b,||,!,c,<EOF>",89))

    def test_multiple_operators_90(self):
        """test multiple operators in sequence"""
        self.assertTrue(TestLexer.checkLexeme("1 + 2 * 3 / 4","1,+,2,*,3,/,4,<EOF>",90))

    def test_comparison_operators_91(self):
        """test comparison operators"""
        self.assertTrue(TestLexer.checkLexeme("a <= b >= c == d","a,<=,b,>=,c,==,d,<EOF>",91))

    def test_nested_blocks_92(self):
        """test nested block structures"""
        self.assertTrue(TestLexer.checkLexeme("{ { } }","{,{,},},<EOF>",92))

    def test_multi_declarations_93(self):
        """test multiple variable declarations"""
        self.assertTrue(TestLexer.checkLexeme("var x, y, z int","var,x,,,y,,,z,int,<EOF>",93))

    def test_function_params_94(self):
        """test function with parameters"""
        self.assertTrue(TestLexer.checkLexeme("func add(x int, y float)","func,add,(,x,int,,,y,float,),<EOF>",94))

    def test_array_access_95(self):
        """test array access"""
        self.assertTrue(TestLexer.checkLexeme("arr[i][j]","arr,[,i,],[,j,],<EOF>",95))

    def test_struct_method_96(self):
        """test struct method declaration"""
        self.assertTrue(TestLexer.checkLexeme("func (p Point) distance()","func,(,p,Point,),distance,(,),<EOF>",96))

    def test_bool_literals_97(self):
        """test boolean literals"""
        self.assertTrue(TestLexer.checkLexeme("true false","true,false,<EOF>",97))

    def test_nil_literal_98(self):
        """test nil literal"""
        self.assertTrue(TestLexer.checkLexeme("nil","nil,<EOF>",98))

    def test_complex_expression_99(self):
        """test complex expression"""
        self.assertTrue(TestLexer.checkLexeme("a + b * (c - d)","a,+,b,*,(,c,-,d,),<EOF>",99))

    def test_multi_statements_100(self):
        """test multiple statements"""
        self.assertTrue(TestLexer.checkLexeme("x = 1; y = 2;","x,=,1,;,y,=,2,;,<EOF>",100))

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