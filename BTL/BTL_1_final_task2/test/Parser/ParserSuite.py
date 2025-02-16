"""
 * Initial code for Assignment 1, 2
 * Programming Language Principles
 * Author: Võ Tiến
 * Link FB : https://www.facebook.com/Shiba.Vo.Tien
 * Link Group : https://www.facebook.com/groups/khmt.ktmt.cse.bku
 * Date: 07.01.2025
"""

import unittest
from TestUtils import TestParser
import inspect

class ParserSuite(unittest.TestCase):
    def test_001(self):
        """Literal"""
        self.assertTrue(TestParser.test("const Votien = 1;","successful", inspect.stack()[0].function))

    def test_002(self):
        """Literal"""
        self.assertTrue(TestParser.test("const Votien = true;","successful", inspect.stack()[0].function))

    def test_003(self):
        """Literal"""
        self.assertTrue(TestParser.test("const Votien = [5][0]string{1, \"string\"};","successful", inspect.stack()[0].function))

    def test_004(self):
        """Literal"""
        self.assertTrue(TestParser.test("const Votien = [1.]ID{1, 3};","Error on line 1 col 16: 1.", inspect.stack()[0].function))

    def test_005(self):
        """Literal"""
        self.assertTrue(TestParser.test("const Votien = Person{name: \"Alice\", age: 30};","successful", inspect.stack()[0].function))

    def test_006(self):
        """expression"""
        self.assertTrue(TestParser.test("const Votien = 1 || 2 && c + 3 / 2 - -1;","successful", inspect.stack()[0].function))

    def test_007(self):
        """expression"""
        self.assertTrue(TestParser.test("const Votien = 1[2] + foo()[2] + ID[2].b.b;","successful", inspect.stack()[0].function))

    def test_008(self):
        """expression"""
        self.assertTrue(TestParser.test("const Votien = ca.foo(132) + b.c[2];","successful", inspect.stack()[0].function))

    def test_009(self):
        """expression"""
        self.assertTrue(TestParser.test("const Votien = a.a.foo();","successful", inspect.stack()[0].function))

    def test_010(self):
        """declared variables"""
        self.assertTrue(TestParser.test("""
            var x int = foo() + 3 / 4;
            var y = "Hello" / 4;
            var z str;
        ""","successful", inspect.stack()[0].function))

    def test_011(self):
        """declared constants"""
        self.assertTrue(TestParser.test("""
            const VoTien = a.b() + 2;
        ""","successful", inspect.stack()[0].function))

    def test_012(self):
        """declared function"""
        self.assertTrue(TestParser.test("""
            func VoTien(x int, y int) int {return;}
            func VoTien1() [2][3] ID {return;};
            func VoTien2() {return;}
        ""","successful", inspect.stack()[0].function))

    def test_013(self):
        """declared method"""
        self.assertTrue(TestParser.test("""
            func (c Calculator) VoTien(x int) int {return;};
            func (c Calculator) VoTien() ID {return;}
            func (c Calculator) VoTien(x int, y [2]VoTien) {return;}
        ""","successful", inspect.stack()[0].function))

    def test_014(self):
        """declared struct"""
        self.assertTrue(TestParser.test("""
            type VoTien struct {
                VoTien string ;
                VoTien [1][3]VoTien ;
            }
        ""","successful", inspect.stack()[0].function))

    def test_015(self):
        """declared Interface"""
        self.assertTrue(TestParser.test("""
            type VoTien struct {}
        ""","Error on line 2 col 32: }", inspect.stack()[0].function))

    def test_016(self):
        """declared Interface"""
        self.assertTrue(TestParser.test("""
            type Calculator interface {

                Add(x, y int) int;
                Subtract(a, b float, c int) [3]ID;
                Reset()

                SayHello(name string);

            }
            type VoTien interface {}
        ""","Error on line 11 col 35: }", inspect.stack()[0].function))

    def test_017(self):
        """declared_statement"""
        self.assertTrue(TestParser.test("""
            func VoTien() {
                var x int = foo() + 3 / 4;
                var y = "Hello" / 4;
                var z str;

                const VoTien = a.b() + 2;
            }
        ""","successful", inspect.stack()[0].function))


    def test_018(self):
        """assign_statement"""
        self.assertTrue(TestParser.test("""
            func VoTien() {
                x  := foo() + 3 / 4;
                x.c[2][4] := 1 + 2;
            }
        ""","successful", inspect.stack()[0].function))

    def test_019(self):
        """for_statement"""
        self.assertTrue(TestParser.test("""
            func VoTien() {
                if (x > 10) {return; }
                if (x > 10) {
                  return;
                } else if (x == 10) {
                    var z str;
                } else {
                    var z ID;
                }
            }
        ""","successful", inspect.stack()[0].function))

    def test_020(self):
        """if_statement"""
        self.assertTrue(TestParser.test("""
            func VoTien() {
                for i < 10 {return; }
                for i := 0; i < 10; i += 1 {return; }
                for index, value := range array {return; }
            }
        ""","successful", inspect.stack()[0].function))


    def test_021(self):
        """break and continue, return, Call  statement"""
        self.assertTrue(TestParser.test("""
            func VoTien() {
                for i < 10 {break;}
                break;
                continue;
                return 1;
                return
                foo(2 + x, 4 / y); m.goo();
             }

        ""","successful", inspect.stack()[0].function))

    def test_022(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""
            const a = 0b11;
        ""","successful", inspect.stack()[0].function))

    def test_023(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""
            var z VOTIEN = [true]int{1};
        ""","Error on line 2 col 28: true", inspect.stack()[0].function))

    def test_024(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""
            var z VOTIEN = ID {};
        ""","successful", inspect.stack()[0].function))

    def test_025(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""
            var z VOTIEN = ID {a: 2, b: 2 + 2 + ID {a: 1}};
        ""","successful", inspect.stack()[0].function))

    def test_026(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""
            var z VOTIEN = 1 && 2 && 3 || 1 || 1;
        ""","successful", inspect.stack()[0].function))

    def test_027(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""
            var z VOTIEN = a >= 2 <= "string" > a[2][3] < ID{A: 2} >= [2]S{2};
        ""","successful", inspect.stack()[0].function))

    def test_028(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""
            var z VOTIEN = a.b.a.c.e.g;
        ""","successful", inspect.stack()[0].function))

    def test_029(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""
            var z VOTIEN = a[2][3][a + 2];
        ""","successful", inspect.stack()[0].function))

    def test_030(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""
            var z VOTIEN = a.a.a[2].foo(1);
        ""","successful", inspect.stack()[0].function))

    def test_031(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""
            var z VOTIEN = foo().a[2].goo();
        ""","successful", inspect.stack()[0].function))

    def test_032(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""
            const k = -a + -!-!c - ---[2]int{2};
        ""","successful", inspect.stack()[0].function))

    def test_033(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            var c [2][3]ID
        ""","successful", inspect.stack()[0].function))

    def test_034(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            const a =;
        ""","Error on line 2 col 21: ;", inspect.stack()[0].function))

    def test_035(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            func Add(x int, y [2]int) [2]id {return ;}
""","successful", inspect.stack()[0].function))

    def test_036(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            func Add() {return ;}
""","successful", inspect.stack()[0].function))

    def test_037(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            type Calculator struct {

                value int;
                a [2]int; a [2]ID;
                c Calculator
            }
""","successful", inspect.stack()[0].function))

    def test_038(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            type Calculator struct {
                a int = 2;
            }
""","Error on line 3 col 22: =", inspect.stack()[0].function))

    def test_039(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            type Calculator interface {
                Add(x, y [2]ID) [2]int;
                Subtract(a, b float, c, e int);
                Reset()
                SayHello(name string)
            }
""","successful", inspect.stack()[0].function))

    def test_040(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            type Calculator interface {Reset()}
""","Error on line 2 col 46: }", inspect.stack()[0].function))

    def test_041(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            type Calculator interface {
                Add(x int,c,d ID); Add()
        }
""","successful", inspect.stack()[0].function))

    def test_042(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            func Add(x int, y int) int  {return ;};
""","successful", inspect.stack()[0].function))

    def test_043(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            func (c int) Add(x int) int {return ;}
""","Error on line 2 col 20: int", inspect.stack()[0].function))

    def test_044(self):
        """Declared"""
        self.assertTrue(TestParser.test("""

""","Error on line 3 col 0: <EOF>", inspect.stack()[0].function))

    def test_045(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                         var a int;
                                    };""","successful", inspect.stack()[0].function))

    def test_046(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                         var a = a[2].b;
                                    };""","successful", inspect.stack()[0].function))

    def test_047(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        a += 2;
                                        a -= a[2].b();
                                        a /= 2
                                        a *= 2
                                        a %= 2;
                                    };""","successful", inspect.stack()[0].function))

    def test_048(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        a.c[2].e[3].k += 2;
                                    };""","successful", inspect.stack()[0].function))

    def test_049(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        a.foo() += 2;
                                    };""","Error on line 3 col 48: +=", inspect.stack()[0].function))

    def test_050(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                       a[2+3&&2] += foo().b[2];
                                    };""","successful", inspect.stack()[0].function))

    def test_051(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        if (x.foo().b[2]) {
                                            a := 2;
                                        } else if (a && b) {
                                            return;
                                        } else {
                                            a := 2;
                                        }
                                    };""","successful", inspect.stack()[0].function))

    def test_052(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        for true + 2 + foo().b {return; }
                                    };""","successful", inspect.stack()[0].function))

    def test_053(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        for i := 0; i < 10; i += 1 {
                                           return;
                                        }
                                    };""","successful", inspect.stack()[0].function))

    def test_054(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        for index, value := range 23 {return;
                                        }
                                    };""","successful", inspect.stack()[0].function))

    def test_055(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        break;
                                        continue
                                        break; continue; break
                                    };""","successful", inspect.stack()[0].function))

    def test_056(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        return
                                        return 2 + a[2].b()
                                        return; return a
                                    };""","successful", inspect.stack()[0].function))

    def test_057(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        a.foo(2 + 3, a {a:2})
                                        foo(2 + 3, a {a:2});
                                    };""","successful", inspect.stack()[0].function))

    def test_058(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        a[2][3].foo(2 + 3, a {a:2})
                                    };""","successful", inspect.stack()[0].function))

    def test_059(self):
        """array_literal"""
        self.assertTrue(TestParser.test("""const a = [1]int{{1, 0x1}, ID{}, {{ID{}}}}
""","successful", inspect.stack()[0].function))

    def test_060(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        for var b [2]ID = 1 + 2 / 4; foo().a.b(); i := 1 {
                                            return;
                                        }
                                    };""","successful", inspect.stack()[0].function))

    def test_061(self):
        self.assertTrue(TestParser.test("""
                                            const a = [ID][2][VT]int{{{1}}}
                                        ""","successful", inspect.stack()[0].function))

    def test_062(self):
        self.assertTrue(TestParser.test("""
                                            var a;
                                        ""","Error on line 2 col 49: ;", inspect.stack()[0].function))
    def test_063(self):
        self.assertTrue(TestParser.test("""
                                            var a = {1, 2};
                                        ""","Error on line 2 col 52: {", inspect.stack()[0].function))


    def test_064(self):
            """Statement"""
            self.assertTrue(TestParser.test("""
                func Add() {
                                            }
    ""","successful", inspect.stack()[0].function))

    def test_065(self):
            self.assertTrue(TestParser.test("""
                func (p Person) Greet() string {
                    if (1) {return;
                    }else if (1) {}
                };
    ""","successful", inspect.stack()[0].function))

    def test_066(self):
            self.assertTrue(TestParser.test("""
                func (p Person) Greet() string {
                    for i < 10 {
    // loop body
    }
                };
    ""","successful", inspect.stack()[0].function))

    def test_067(self):
            self.assertTrue(TestParser.test("""
                func (p Person) Greet() string {
                    for i := 0; i < 10; i += 1 {
    // loop body
    }
                };
    ""","successful", inspect.stack()[0].function))

    def test_068(self):
            self.assertTrue(TestParser.test("""
                func (p Person) Greet() string {
                    for index, value := range STRUCT{} {
    // loop body
    };
                };
    ""","successful", inspect.stack()[0].function))

    def test_069(self):
            self.assertTrue(TestParser.test("""
                                                const a = [ID][2][VT]int{{{1}}, ID, a, {b}}
                                            ""","successful", inspect.stack()[0].function))

    def test_070(self):
            """array_literal"""
            self.assertTrue(TestParser.test("""const a = [1]int{[1]int{1}}
    ""","Error on line 1 col 17: [", inspect.stack()[0].function))

    def test_071(self):
            self.assertTrue(TestParser.test("""
                                            var a = {1, 2};
                                            ""","Error on line 2 col 52: {", inspect.stack()[0].function))

    def test_072(self):
            """expression"""
            self.assertTrue(TestParser.test("const Votien = ca.foo(132) + b.c[2];","successful", inspect.stack()[0].function))

    def test_073(self):
            """Expressions"""
            self.assertTrue(TestParser.test("""
            var z VOTIEN = [2]int{};
            ""","Error on line 2 col 34: }", inspect.stack()[0].function))

    def test_074(self):
        """String operations"""
        self.assertTrue(TestParser.test("""func main(){
        str1 := "Hello"
        str2 := "World"
        str3 := str1 + " " + str2 // str3 == "Hello World"
        str4 := "apple"
        str5 := "banana"
        result := str4 == str5 // result == false
}
        ""","successful", inspect.stack()[0].function))


    def test_075(self):
            self.assertTrue(TestParser.test("""
                func (p Person) Greet() string {
                    if (1) {return;}
                else if (1)
                    {}
                };
    ""","Error on line 4 col 16: else", inspect.stack()[0].function))

    def test_076(self):
        """Null struct"""
        self.assertTrue(TestParser.test("""
        type Null struct {}
        var n Null;
        ""","Error on line 2 col 26: }", inspect.stack()[0].function))


    def test_077(self):
        """Null Interface"""
        self.assertTrue(TestParser.test("""
        type Null interface {}
        var n Null;
        ""","Error on line 2 col 29: }", inspect.stack()[0].function))


    def test_078(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        for var b [2]ID = 1 + 2 / 4; foo().a.b(); i := 1 {
                                            return;
                                        }
                                    };""","successful", inspect.stack()[0].function))

    def test_079(self):
        self.assertTrue(
            TestParser.test(
                """
            func (p Person) Greet() string {
                for index, value := range STRUCT{} {
// loop body
};
            };
""",
                "successful",
                inspect.stack()[0].function,
            )
        )

    def test_080(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    if (x > 10) {
                                        return;
                                    } else if (x == 10) {
                                        var z str;
                                    } else {
                                        var z ID;
                                    }
                                    ""","Error on line 2 col 36: if", inspect.stack()[0].function))

    def test_081(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    return;
                                    ""","Error on line 2 col 36: return", inspect.stack()[0].function))

    def test_082(self):
        """struct initialization"""
        self.assertTrue(TestParser.test("""
        func main() {
            p := Person{name: "Alice", age: 30}
        }
        ""","successful", inspect.stack()[0].function))

    def test_083(self):
        """zero-value instance"""
        self.assertTrue(TestParser.test("""
        func main() {
            p := Person{}
        }
        ""","successful", inspect.stack()[0].function))


    def test_084(self):
        """defined method"""
        self.assertTrue(TestParser.test("""
        func (p Person) Greet() string {
            return "Hello, " + p.name
        }
        ""","successful", inspect.stack()[0].function))

    def test_085(self):
        """type and initialization"""
        self.assertTrue(TestParser.test("""
        var x int = 5;
        ""","successful", inspect.stack()[0].function))

    def test_086(self):
        """type and initialization"""
        self.assertTrue(TestParser.test("""
        var y int = "Hello";
        ""","successful", inspect.stack()[0].function))

    def test_087(self):
        """type and initialization"""
        self.assertTrue(TestParser.test("""
        var x int;
        ""","successful", inspect.stack()[0].function))

    def test_088(self):
        """global constant"""
        self.assertTrue(TestParser.test("""
        const Pi = 3.14;
        ""","successful", inspect.stack()[0].function))

    def test_089(self):
        """constant with literal string"""
        self.assertTrue(TestParser.test("""
            const message = "Hello, World!";
        ""","successful", inspect.stack()[0].function))

    def test_090(self):
        """constant with expression"""
        self.assertTrue(TestParser.test("""
            const MaxSize = 100 + 50;
        ""","successful", inspect.stack()[0].function))

    def test_091(self):
        """basic function"""
        self.assertTrue(TestParser.test("""
            func Add(x int, y int) int {
                return x + y;
            }
        ""","successful", inspect.stack()[0].function))


    def test_092(self):
        """basic method"""
        self.assertTrue(TestParser.test("""
            type Calculator struct {
                value int;
            }
                func (c Calculator) Add(x int) int {
                c.value += x;
                return c.value;
            }
        ""","successful", inspect.stack()[0].function))

    def test_093(self):
        """basic array litteral"""
        self.assertTrue(TestParser.test("""
        func main() {
            arr := [3]int{10, 20, 30}  // Valid
        }
        ""","successful", inspect.stack()[0].function))

    def test_094(self):
        """basic array litteral"""
        self.assertTrue(TestParser.test("""
        func main() {
            marr := [2][3]int{{1, 2, 3}, {4, 5, 6}}
        }
        ""","successful", inspect.stack()[0].function))

    def test_095(self):
        """method access"""
        self.assertTrue(TestParser.test("""
        func main() {
            calculator.add(3, 4)
        }
        ""","successful", inspect.stack()[0].function))

    def test_096(self):
        """basic for loop"""
        self.assertTrue(TestParser.test("""
        func main() {
            for i < 10 {
                // loop body
            }
        }
        ""","successful", inspect.stack()[0].function))


    # def test_075(self):
    #     """Array declarations"""
    #     self.assertTrue(TestParser.test("""
    #     var arr [5]int; // defines an array of 5 integers.
    #     var multi_arr [2][5][100][-100][100]int; // defines an array of 2 x 5 integers.
    #     ""","Error on line 3 col 27: -", inspect.stack()[0].function))

    # def test_076(self):
    #     """Array access"""
    #     self.assertTrue(TestParser.test("""
    #     func main(){
    #     a := multi_arr[0][1000][-1][1.2] b := 10
    #     }
    #     ""","Error on line 3 col 42: b", inspect.stack()[0].function))

    # def test_077(self):
    #     """Array size expressions"""
    #     self.assertTrue(TestParser.test("""
    #     var arr [2 + 3]int;
    #     ""","Error on line 2 col 20: +", inspect.stack()[0].function))

    # def test_078(self):
    #     """Struct definition"""
    #     self.assertTrue(TestParser.test("""
    #     type s struct { a int; b b; c c; a a123;
    #      b float; hello hello; arr [5]int; arr [1000][100]hello.hello
    #     };
    #     ""","successful", inspect.stack()[0].function))

    # def test_079(self):
    #     """Invalid if condition"""
    #     self.assertTrue(TestParser.test("""func H() Person{
    #     if ():= true;}
    #     ""","Error on line 2 col 13: )", inspect.stack()[0].function))

    # def test_080(self):
    #     """Array indexing"""
    #     self.assertTrue(TestParser.test("""func H() Person{
    #     x := arr[(53)];
    #     x := arr[3,23];
    #     }
    #     ""","Error on line 3 col 19: ,", inspect.stack()[0].function))

    # def test_081(self):
    #     """Unclosed string literal"""
    #     self.assertTrue(TestParser.test("""func H() Person{
    #     str := "Hello World
    #     }
    #     ""","Error on line 2 col 21: \"Hello World\"", inspect.stack()[0].function))

    # def test_082(self):
    #     """Octal number"""
    #     self.assertTrue(TestParser.test("""func H() Person{
    #     /* This is a comment */
    #     a := 0o101;
    #     }
    #     ""","successful", inspect.stack()[0].function))

    # def test_083(self):
    #     """Empty array size"""
    #     self.assertTrue(TestParser.test("""
    #     var arr []int;
    #     ""","Error on line 2 col 18: ]", inspect.stack()[0].function))

    # def test_084(self):
    #     """Negative array size"""
    #     self.assertTrue(TestParser.test("""
    #     var arr [-5]int;
    #     ""","Error on line 2 col 18: -", inspect.stack()[0].function))

    # def test_085(self):
    #     """Chained comparisons"""
    #     self.assertTrue(TestParser.test("""
    #     func H() Person{
    #     a := 5 < 10 > 3;
    #     }
    #     ""","successful", inspect.stack()[0].function))

    # def test_086(self):
    #     """Complex expression"""
    #     self.assertTrue(TestParser.test("""
    #     func H() Person{
    #     result := (a + b * c) % d == e && !f || g;
    #     }
    #     ""","successful", inspect.stack()[0].function))

    # def test_087(self):
    #     """Invalid array declaration"""
    #     self.assertTrue(TestParser.test("""
    #     var arr [5][3];
    #     ""","Error on line 2 col 23: ;", inspect.stack()[0].function))

    # def test_088(self):
    #     """Float modulo"""
    #     self.assertTrue(TestParser.test("""
    #     func H() Person{
    #     a := 5.5 % 2.0;
    #     }
    #     ""","successful", inspect.stack()[0].function))

    # def test_089(self):
    #     """Invalid member access"""
    #     self.assertTrue(TestParser.test("""func H() Person{
    #     x := person.123;
    #     }
    #     ""","Error on line 2 col 21: 123", inspect.stack()[0].function))

    # def test_090(self):
    #     """Person struct operations"""
    #     self.assertTrue(TestParser.test("""
    #     type Person struct {
    #     name string;
    #     age int;
    #     radius float;
    #     shape Shape;
    #     }
    #     func H() Person{
    #     p := Person{name: "Alice", age: 30}
    #     p := Person{}
    #     PutStringLn(p.name)
    #     PutIntLn(p.age) // Output: 30
    #     p.age := 31
    #     PutIntLn(p.age) // Output: 31
    #     }
    #     func (p Person) Greet() string {
    #     return "Hello, " + p.name
    #     PutStringLn(p.Greet()) // Output: Hello, Alice
    #     }
    #     ""","successful", inspect.stack()[0].function))

    # def test_091(self):
    #     """Shape interface"""
    #     self.assertTrue(TestParser.test("""
    #     type Shape interface {
    #         Area() float
    #         Perimeter(w, h int) float
    #         Draw(name string, scale float) int
    #         Rotate(angle float, speed int) string
    #     }
    #     ""","successful", inspect.stack()[0].function))

    # def test_092(self):
    #     """Invalid interface"""
    #     self.assertTrue(TestParser.test("""
    #     type InvalidInterface interface {
    #         Method1() Method2()
    #     }
    #     ""","Error on line 3 col 30: (", inspect.stack()[0].function))

    # def test_093(self):
    #     """Invalid interface method"""
    #     self.assertTrue(TestParser.test("""
    #     type Test interface {
    #         Add(x, y int, z);
    #     }
    #     ""","Error on line 3 col 28: )", inspect.stack()[0].function))

    # def test_094(self):
    #     """Invalid interface keyword"""
    #     self.assertTrue(TestParser.test("""
    #     type Test interface {
    #         type(a int);
    #     }
    #     ""","Error on line 3 col 13: type", inspect.stack()[0].function))

    # def test_095(self):
    #     """Empty interface"""
    #     self.assertTrue(TestParser.test("""
    #     type Empty interface {}
    #     ""","Error on line 2 col 31: }", inspect.stack()[0].function))

    # def test_096(self):
    #     """Wrong syntax"""
    #     self.assertTrue(TestParser.test("""
    #     type WrongSyntax {
    #         Method();
    #     }
    #     ""","Error on line 2 col 26: {", inspect.stack()[0].function))

    # def test_097(self):
    #     """Invalid return type"""
    #     self.assertTrue(TestParser.test("""
    #     type Test interface {
    #         Process(data string) int float;
    #     }
    #     ""","Error on line 3 col 38: float", inspect.stack()[0].function))

    # def test_098(self):
    #     """Variable declarations"""
    #     self.assertTrue(TestParser.test("""
    #     var globalVar int = 10;
    #     func main() {
    #         var localVar = 20;
    #         var x, y int = 5, 10;
    #         var z float;
    #         var a = "Hello";
    #         var b int = globalVar + localVar;
    #         var c = x + y;
    #         var d = c * 2;
    #         var e float = 3.14;
    #         var f = e + 2.0;
    #     }
    #     ""","successful", inspect.stack()[0].function))

    # def test_099(self):
    #     """Nested scopes"""
    #     self.assertTrue(TestParser.test("""
    #     var x int = 5;
    #     func main() {
    #         var x = 10;
    #         {
    #             var x = 15;
    #             var y = x + 5;
    #         }
    #         var y = x + 1;
    #     }
    #     func foo(x int) {
    #         var x = 20;
    #         var y = x + 10;
    #     }
    #     ""","successful", inspect.stack()[0].function))

    # def test_100(self):
    #     """Complex declarations"""
    #     self.assertTrue(TestParser.test("""
    #     var arr [5]int;
    #     var matrix [2][3]float;
    #     var str string = "Hello";
    #     var person = Person { name : "HELLO" , age : 97 };
    #     var calc Calculator;
    #     func main() {
    #         var x = arr[0];
    #         var y = matrix[1][2];
    #         var z = person.name;
    #         var w = calc.Add(1, 2);
    #         var invalid = x + y;
    #     }
    #     ""","successful", inspect.stack()[0].function))

    # def test_101(self):
    #     """Invalid array declaration"""
    #     self.assertTrue(TestParser.test("""
    #     var a, b int;
    #     ""","", inspect.stack()[0].function))