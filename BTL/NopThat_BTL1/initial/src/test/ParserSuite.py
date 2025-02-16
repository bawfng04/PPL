import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: void main() {} """
        input = """func main() {};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))

    def test_more_complex_program(self):
        """More complex program"""
        input = """func foo () {
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))

    def test_wrong_miss_close(self):
        """Miss ) void main( {}"""
        input = """func main({};"""
        expect = "Error on line 1 col 11: {"
        self.assertTrue(TestParser.checkParser(input,expect,203))
    def test_wrong_variable(self):
        input = """var int;"""
        expect = "Error on line 1 col 5: int"
        self.assertTrue(TestParser.checkParser(input,expect,204))
    def test_wrong_index(self):
        input = """var i ;"""
        expect = "Error on line 1 col 7: ;"
        self.assertTrue(TestParser.checkParser(input,expect,205))


    def test_variable_declaration(self):
        """Test variable declaration"""
        input = """var x int;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,206))

    def test_multiple_declarations(self):
        """Test multiple variable declarations"""
        input = """
        var a, b int;
        var c float;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,207))

    def test_function_with_return(self):
        """Test function with return statement"""
        input = """
        func add(a int, b int) int {
            return a + b;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,208))

    # def test_simple_if_statement(self):
    #     """Test if statement"""
    #     input = """
    #     func main() {
    #         if x > 0 {
    #             return x;
    #         }
    #     }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input,expect,209))

    # def test_wrong_function_declaration(self):
    #     """Test wrong function declaration"""
    #     input = """func) main() {}"""
    #     expect = "Error on line 1 col 4: )"
    #     self.assertTrue(TestParser.checkParser(input,expect,210))

    # def test_missing_semicolon(self):
    #     """Test missing semicolon"""
    #     input = """var x int"""
    #     expect = "Error on line 1 col 8: <EOF>"
    #     self.assertTrue(TestParser.checkParser(input,expect,211))

    def test_array_declaration(self):
        """Test array declaration"""
        input = """var arr [5]int;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,212))

    def test_simple_for_loop(self):
        """Test for loop"""
        input = """
        func main() {
            for i := 0; i < 5; i = i + 1 {
                continue;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,213))

    def test_array_declaration_214(self):
        """Test array declaration"""
        input = """var arr [5]int;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,214))

    def test_function_with_return_215(self):
        """Test function with return statement"""
        input = """
        func add(a int, b int) int {
            return a + b;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,215))

    def test_simple_for_loop_216(self):
        """Test for loop"""
        input = """
        func main() {
            for i := 0; i < 5; i = i + 1 {
                continue;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,216))

    def test_multiple_declarations_217(self):
        """Test multiple variable declarations"""
        input = """
        var a, b int;
        var c float;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,217))

    def test_wrong_variable_218(self):
        input = """var int;"""
        expect = "Error on line 1 col 5: int"
        self.assertTrue(TestParser.checkParser(input,expect,218))

    def test_variable_declaration_219(self):
        """Test variable declaration"""
        input = """var x int;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,219))

    def test_function_with_return_220(self):
        """Test function with return statement"""
        input = """
        func add(a int, b int) int {
            return a + b;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,220))

    def test_simple_for_loop_221(self):
        """Test for loop"""
        input = """
        func main() {
            for i := 0; i < 5; i = i + 1 {
                continue;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,221))

    def test_multiple_declarations_222(self):
        """Test multiple variable declarations"""
        input = """
        var a, b int;
        var c float;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,222))

    def test_wrong_variable_223(self):
        input = """var int;"""
        expect = "Error on line 1 col 5: int"
        self.assertTrue(TestParser.checkParser(input,expect,223))

    def test_variable_declaration_224(self):
        """Test variable declaration"""
        input = """var x int;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,224))

    def test_function_with_return_225(self):
        """Test function with return statement"""
        input = """
        func add(a int, b int) int {
            return a + b;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,225))

    def test_simple_for_loop_226(self):
        """Test for loop"""
        input = """
        func main() {
            for i := 0; i < 5; i = i + 1 {
                continue;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,226))

    def test_multiple_declarations_227(self):
        """Test multiple variable declarations"""
        input = """
        var a, b int;
        var c float;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,227))

    def test_wrong_variable_228(self):
        input = """var int;"""
        expect = "Error on line 1 col 5: int"
        self.assertTrue(TestParser.checkParser(input,expect,228))

    def test_variable_declaration_229(self):
        """Test variable declaration"""
        input = """var x int;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,229))

    def test_function_with_return_230(self):
        """Test function with return statement"""
        input = """
        func add(a int, b int) int {
            return a + b;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,230))

    def test_simple_for_loop_231(self):
        """Test for loop"""
        input = """
        func main() {
            for i := 0; i < 5; i = i + 1 {
                continue;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,231))

    def test_multiple_declarations_232(self):
        """Test multiple variable declarations"""
        input = """
        var a, b int;
        var c float;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,232))

    def test_wrong_variable_233(self):
        input = """var int;"""
        expect = "Error on line 1 col 5: int"
        self.assertTrue(TestParser.checkParser(input,expect,233))

    def test_variable_declaration_234(self):
        """Test variable declaration"""
        input = """var x int;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,234))

    def test_function_with_return_235(self):
        """Test function with return statement"""
        input = """
        func add(a int, b int) int {
            return a + b;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,235))

    def test_simple_for_loop_236(self):
        """Test for loop"""
        input = """
        func main() {
            for i := 0; i < 5; i = i + 1 {
                continue;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,236))

    def test_multiple_declarations_237(self):
        """Test multiple variable declarations"""
        input = """
        var a, b int;
        var c float;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,237))

    def test_wrong_variable_238(self):
        input = """var int;"""
        expect = "Error on line 1 col 5: int"
        self.assertTrue(TestParser.checkParser(input,expect,238))

    def test_variable_declaration_239(self):
        """Test variable declaration"""
        input = """var x int;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,239))

    def test_function_with_return_240(self):
        """Test function with return statement"""
        input = """
        func add(a int, b int) int {
            return a + b;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,240))

    def test_simple_for_loop_241(self):
        """Test for loop"""
        input = """
        func main() {
            for i := 0; i < 5; i = i + 1 {
                continue;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,241))

    def test_multiple_declarations_242(self):
        """Test multiple variable declarations"""
        input = """
        var a, b int;
        var c float;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,242))

    def test_wrong_variable_243(self):
        input = """var int;"""
        expect = "Error on line 1 col 5: int"
        self.assertTrue(TestParser.checkParser(input,expect,243))

    def test_variable_declaration_244(self):
        """Test variable declaration"""
        input = """var x int;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,244))

    def test_function_with_return_245(self):
        """Test function with return statement"""
        input = """
        func add(a int, b int) int {
            return a + b;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,245))

    def test_simple_for_loop_246(self):
        """Test for loop"""
        input = """
        func main() {
            for i := 0; i < 5; i = i + 1 {
                continue;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,246))

    def test_multiple_declarations_247(self):
        """Test multiple variable declarations"""
        input = """
        var a, b int;
        var c float;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,247))

    def test_wrong_variable_248(self):
        input = """var int;"""
        expect = "Error on line 1 col 5: int"
        self.assertTrue(TestParser.checkParser(input,expect,248))

    def test_variable_declaration_249(self):
        """Test variable declaration"""
        input = """var x int;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,249))

    def test_function_with_return_250(self):
        """Test function with return statement"""
        input = """
        func add(a int, b int) int {
            return a + b;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,250))

    def test_simple_for_loop_251(self):
        """Test for loop"""
        input = """
        func main() {
            for i := 0; i < 5; i = i + 1 {
                continue;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,251))

    def test_multiple_declarations_252(self):
        """Test multiple variable declarations"""
        input = """
        var a, b int;
        var c float;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,252))

    def test_wrong_variable_253(self):
        input = """var int;"""
        expect = "Error on line 1 col 5: int"
        self.assertTrue(TestParser.checkParser(input,expect,253))

    def test_variable_declaration_254(self):
        """Test variable declaration"""
        input = """var x int;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,254))

    def test_function_with_return_255(self):
        """Test function with return statement"""
        input = """
        func add(a int, b int) int {
            return a + b;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,255))

    def test_simple_for_loop_256(self):
        """Test for loop"""
        input = """
        func main() {
            for i := 0; i < 5; i = i + 1 {
                continue;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,256))

    def test_multiple_declarations_257(self):
        """Test multiple variable declarations"""
        input = """
        var a, b int;
        var c float;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,257))

    def test_wrong_variable_258(self):
        input = """var int;"""
        expect = "Error on line 1 col 5: int"
        self.assertTrue(TestParser.checkParser(input,expect,258))

    def test_variable_declaration_259(self):
        """Test variable declaration"""
        input = """var x int;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,259))

    def test_function_with_return_260(self):
        """Test function with return statement"""
        input = """
        func add(a int, b int) int {
            return a + b;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,260))

    def test_simple_for_loop_261(self):
        """Test for loop"""
        input = """
        func main() {
            for i := 0; i < 5; i = i + 1 {
                continue;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,261))

    def test_multiple_declarations_262(self):
        """Test multiple variable declarations"""
        input = """
        var a, b int;
        var c float;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,262))

    def test_wrong_variable_263(self):
        input = """var int;"""
        expect = "Error on line 1 col 5: int"
        self.assertTrue(TestParser.checkParser(input,expect,263))

    def test_variable_declaration_264(self):
        """Test variable declaration"""
        input = """var x int;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,264))

    def test_function_with_return_265(self):
        """Test function with return statement"""
        input = """
        func add(a int, b int) int {
            return a + b;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,265))

    def test_simple_for_loop_266(self):
        """Test for loop"""
        input = """
        func main() {
            for i := 0; i < 5; i = i + 1 {
                continue;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,266))

    def test_multiple_declarations_267(self):
        """Test multiple variable declarations"""
        input = """
        var a, b int;
        var c float;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,267))

    def test_wrong_variable_268(self):
        input = """var int;"""
        expect = "Error on line 1 col 5: int"
        self.assertTrue(TestParser.checkParser(input,expect,268))

    def test_variable_declaration_269(self):
        """Test variable declaration"""
        input = """var x int;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,269))

    def test_function_with_return_270(self):
        """Test function with return statement"""
        input = """
        func add(a int, b int) int {
            return a + b;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,270))

    def test_simple_for_loop_271(self):
        """Test for loop"""
        input = """
        func main() {
            for i := 0; i < 5; i = i + 1 {
                continue;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,271))

    def test_multiple_declarations_272(self):
        """Test multiple variable declarations"""
        input = """
        var a, b int;
        var c float;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,272))

    def test_wrong_variable_273(self):
        input = """var int;"""
        expect = "Error on line 1 col 5: int"
        self.assertTrue(TestParser.checkParser(input,expect,273))

    def test_variable_declaration_274(self):
        """Test variable declaration"""
        input = """var x int;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,274))

    def test_function_with_return_275(self):
        """Test function with return statement"""
        input = """
        func add(a int, b int) int {
            return a + b;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,275))

    def test_simple_for_loop_276(self):
        """Test for loop"""
        input = """
        func main() {
            for i := 0; i < 5; i = i + 1 {
                continue;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,276))

    def test_multiple_declarations_277(self):
        """Test multiple variable declarations"""
        input = """
        var a, b int;
        var c float;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,277))

    def test_wrong_variable_278(self):
        input = """var int;"""
        expect = "Error on line 1 col 5: int"
        self.assertTrue(TestParser.checkParser(input,expect,278))

    def test_variable_declaration_279(self):
        """Test variable declaration"""
        input = """var x int;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,279))

    def test_function_with_return_280(self):
        """Test function with return statement"""
        input = """
        func add(a int, b int) int {
            return a + b;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,280))

    def test_simple_for_loop_281(self):
        """Test for loop"""
        input = """
        func main() {
            for i := 0; i < 5; i = i + 1 {
                continue;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,281))

    def test_multiple_declarations_282(self):
        """Test multiple variable declarations"""
        input = """
        var a, b int;
        var c float;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,282))

    def test_wrong_variable_283(self):
        input = """var int;"""
        expect = "Error on line 1 col 5: int"
        self.assertTrue(TestParser.checkParser(input,expect,283))

    def test_variable_declaration_284(self):
        """Test variable declaration"""
        input = """var x int;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,284))

    def test_function_with_return_285(self):
        """Test function with return statement"""
        input = """
        func add(a int, b int) int {
            return a + b;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,285))

    def test_simple_for_loop_286(self):
        """Test for loop"""
        input = """
        func main() {
            for i := 0; i < 5; i = i + 1 {
                continue;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,286))

    def test_multiple_declarations_287(self):
        """Test multiple variable declarations"""
        input = """
        var a, b int;
        var c float;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,287))

    def test_wrong_variable_288(self):
        input = """var int;"""
        expect = "Error on line 1 col 5: int"
        self.assertTrue(TestParser.checkParser(input,expect,288))

    def test_variable_declaration_289(self):
        """Test variable declaration"""
        input = """var x int;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,289))

    def test_function_with_return_290(self):
        """Test function with return statement"""
        input = """
        func add(a int, b int) int {
            return a + b;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,290))

    def test_simple_for_loop_291(self):
        """Test for loop"""
        input = """
        func main() {
            for i := 0; i < 5; i = i + 1 {
                continue;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,291))

    def test_multiple_declarations_292(self):
        """Test multiple variable declarations"""
        input = """
        var a, b int;
        var c float;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,292))

    def test_wrong_variable_293(self):
        input = """var int;"""
        expect = "Error on line 1 col 5: int"
        self.assertTrue(TestParser.checkParser(input,expect,293))

    def test_variable_declaration_294(self):
        """Test variable declaration"""
        input = """var x int;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,294))

    def test_function_with_return_295(self):
        """Test function with return statement"""
        input = """
        func add(a int, b int) int {
            return a + b;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,295))

    def test_simple_for_loop_296(self):
        """Test for loop"""
        input = """
        func main() {
            for i := 0; i < 5; i = i + 1 {
                continue;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,296))

    def test_multiple_declarations_297(self):
        """Test multiple variable declarations"""
        input = """
        var a, b int;
        var c float;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,297))

    def test_wrong_variable_298(self):
        input = """var int;"""
        expect = "Error on line 1 col 5: int"
        self.assertTrue(TestParser.checkParser(input,expect,298))

    def test_variable_declaration_299(self):
        """Test variable declaration"""
        input = """var x int;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,299))

    def test_function_with_return_300(self):
        """Test function with return statement"""
        input = """
        func add(a int, b int) int {
            return a + b;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,300))

    def test_simple_for_loop_301(self):
        """Test for loop"""
        input = """
        func main() {
            for i := 0; i < 5; i = i + 1 {
                continue;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,301))

    def test_multiple_declarations_302(self):
        """Test multiple variable declarations"""
        input = """
        var a, b int;
        var c float;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,302))

    def test_wrong_variable_303(self):
        input = """var int;"""
        expect = "Error on line 1 col 5: int"
        self.assertTrue(TestParser.checkParser(input,expect,303))

    def test_variable_declaration_304(self):
        """Test variable declaration"""
        input = """var x int;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,304))

    def test_function_with_return_305(self):
        """Test function with return statement"""
        input = """
        func add(a int, b int) int {
            return a + b;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,305))

    def test_simple_for_loop_306(self):
        """Test for loop"""
        input = """
        func main() {
            for i := 0; i < 5; i = i + 1 {
                continue;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,306))

    def test_multiple_declarations_307(self):
        """Test multiple variable declarations"""
        input = """
        var a, b int;
        var c float;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,307))

    def test_wrong_variable_308(self):
        input = """var int;"""
        expect = "Error on line 1 col 5: int"
        self.assertTrue(TestParser.checkParser(input,expect,308))

    def test_variable_declaration_309(self):
        """Test variable declaration"""
        input = """var x int;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,309))

    def test_function_with_return_310(self):
        """Test function with return statement"""
        input = """
        func add(a int, b int) int {
            return a + b;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,310))

    def test_simple_for_loop_311(self):
        """Test for loop"""
        input = """
        func main() {
            for i := 0; i < 5; i = i + 1 {
                continue;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,311))

    def test_multiple_declarations_312(self):
        """Test multiple variable declarations"""
        input = """
        var a, b int;
        var c float;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,312))

    def test_wrong_variable_313(self):
        input = """var int;"""
        expect = "Error on line 1 col 5: int"
        self.assertTrue(TestParser.checkParser(input,expect,313))