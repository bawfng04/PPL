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

    def test_097(self):
        self.assertTrue(TestParser.test("""
        type Person struct {
            func (p Person) Greet() string {
                return "Hello, " + p.name
            }
        c c
        func (c c) Add(x, y int, b float) {return ;}
        value int;
        }
        """, "Error on line 3 col 12: func", inspect.stack()[0].function))


    def test_098(self):
        """Literal"""
        self.assertTrue(TestParser.test("const Votien = 1;","successful", inspect.stack()[0].function))

    def test_099(self):
        """Literal"""
        self.assertTrue(TestParser.test("const Votien = true;","successful", inspect.stack()[0].function))

    def test_100(self):
        """Literal"""
        self.assertTrue(TestParser.test("const Votien = [5][0]string{1, \"string\"};","successful", inspect.stack()[0].function))

    def test_101(self):
        """Literal"""
        self.assertTrue(TestParser.test("const Votien = [1.]ID{1, 3};","Error on line 1 col 16: 1.", inspect.stack()[0].function))

    def test_102(self):
        """Literal"""
        self.assertTrue(TestParser.test("const Votien = Person{name: \"Alice\", age: 30};","successful", inspect.stack()[0].function))

    def test_103(self):
        """expression"""
        self.assertTrue(TestParser.test("const Votien = 1 || 2 && c + 3 / 2 - -1;","successful", inspect.stack()[0].function))

    def test_104(self):
        """expression"""
        self.assertTrue(TestParser.test("const Votien = 1[2] + foo()[2] + ID[2].b.b;","successful", inspect.stack()[0].function))

    def test_105(self):
        """expression"""
        self.assertTrue(TestParser.test("const Votien = ca.foo(132) + b.c[2];","successful", inspect.stack()[0].function))

    def test_106(self):
        """expression"""
        self.assertTrue(TestParser.test("const Votien = a.a.foo();","successful", inspect.stack()[0].function))

    def test_107(self):
        """declared variables"""
        self.assertTrue(TestParser.test("""
            var x int = foo() + 3 / 4;
            var y = "Hello" / 4;
            var z str;
        ""","successful", inspect.stack()[0].function))

    def test_108(self):
        """declared constants"""
        self.assertTrue(TestParser.test("""
            const VoTien = a.b() + 2;
        ""","successful", inspect.stack()[0].function))

    def test_109(self):
        """declared function"""
        self.assertTrue(TestParser.test("""
            func VoTien(x int, y int) int {return;}
            func VoTien1() [2][3] ID {return;};
            func VoTien2() {return;}
        ""","successful", inspect.stack()[0].function))

    def test_110(self):
        """declared method"""
        self.assertTrue(TestParser.test("""
            func (c Calculator) VoTien(x int) int {return;};
            func (c Calculator) VoTien() ID {return;}
            func (c Calculator) VoTien(x int, y [2]VoTien) {return;}
        ""","successful", inspect.stack()[0].function))

    def test_111(self):
        """declared struct"""
        self.assertTrue(TestParser.test("""
            type VoTien struct {
                VoTien string ;
                VoTien [1][3]VoTien ;
            }
        ""","successful", inspect.stack()[0].function))

    def test_112(self):
        """declared Interface"""
        self.assertTrue(TestParser.test("""
            type VoTien struct {}
        ""","Error on line 2 col 32: }", inspect.stack()[0].function))

    def test_113(self):
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

    def test_114(self):
        """declared_statement"""
        self.assertTrue(TestParser.test("""
            func VoTien() {
                var x int = foo() + 3 / 4;
                var y = "Hello" / 4;
                var z str;

                const VoTien = a.b() + 2;
            }
        ""","successful", inspect.stack()[0].function))


    def test_115(self):
        """assign_statement"""
        self.assertTrue(TestParser.test("""
            func VoTien() {
                x  := foo() + 3 / 4;
                x.c[2][4] := 1 + 2;
            }
        ""","successful", inspect.stack()[0].function))

    def test_116(self):
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

    def test_117(self):
        """if_statement"""
        self.assertTrue(TestParser.test("""
            func VoTien() {
                for i < 10 {return; }
                for i := 0; i < 10; i += 1 {return; }
                for index, value := range array {return; }
            }
        ""","successful", inspect.stack()[0].function))


    def test_118(self):
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

    def test_119(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""
            const a = 0b11;
        ""","successful", inspect.stack()[0].function))

    def test_120(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""
            const a = 1.;
        ""","successful", inspect.stack()[0].function))

    def test_121(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""
            var z VOTIEN 1;
        ""","Error on line 2 col 25: 1", inspect.stack()[0].function))

    def test_122(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""
            var z VOTIEN = int{1};
        ""","Error on line 2 col 27: int", inspect.stack()[0].function))

    def test_123(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""
            var z VOTIEN = [true]int{1};
        ""","Error on line 2 col 28: true", inspect.stack()[0].function))

    def test_124(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""
            var z VOTIEN = []int{1};
        ""","Error on line 2 col 28: ]", inspect.stack()[0].function))

    def test_125(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""
            var z VOTIEN = []int{1};
        ""","Error on line 2 col 28: ]", inspect.stack()[0].function))

    def test_126(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""
            var z VOTIEN = [2]int{1;
        ""","Error on line 2 col 35: ;", inspect.stack()[0].function))

    def test_127(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""
            var z VOTIEN = [2]int{1,3,4;
        ""","Error on line 2 col 39: ;", inspect.stack()[0].function))

    def test_128(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""
            var z VOTIEN = [2]int{};
        ""","Error on line 2 col 34: }", inspect.stack()[0].function))

    def test_129(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""
            var z VOTIEN = ID {};
        ""","successful", inspect.stack()[0].function))

    def test_130(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""
            var z VOTIEN = ID {a: 2, b: 2 + 2 + ID {a: 1}};
        ""","successful", inspect.stack()[0].function))

    def test_131(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""
            var z VOTIEN = int {};
        ""","Error on line 2 col 27: int", inspect.stack()[0].function))

    def test_132(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""
            var z VOTIEN = ID + 3;
        ""","successful", inspect.stack()[0].function))

    def test_133(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""
            var z VOTIEN = ID {a: };
        ""","Error on line 2 col 34: }", inspect.stack()[0].function))

    def test_134(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""
            var z VOTIEN = 1 && 2 && 3 || 1 || 1;
        ""","successful", inspect.stack()[0].function))

    def test_135(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""
            var z VOTIEN = a >= 2 <= "string" > a[2][3] < ID{A: 2} >= [2]S{2};
        ""","successful", inspect.stack()[0].function))

    def test_136(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""
            var z VOTIEN = a + b - [2]int{2} + c - z;
        ""","successful", inspect.stack()[0].function))

    def test_137(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""
            var z VOTIEN = a * b / d % e * 2;
        ""","successful", inspect.stack()[0].function))

    def test_138(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""
            var z VOTIEN = a.b.a.c.e.g;
        ""","successful", inspect.stack()[0].function))

    def test_139(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""
            var z VOTIEN = a[2][3][a + 2];
        ""","successful", inspect.stack()[0].function))

    def test_140(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""
            var z VOTIEN = a[2, 3];
        ""","Error on line 2 col 30: ,", inspect.stack()[0].function))

    def test_141(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""
            var z VOTIEN = a[];
        ""","Error on line 2 col 29: ]", inspect.stack()[0].function))

    def test_142(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""
            var z VOTIEN = a.a.a[2].foo();
        ""","successful", inspect.stack()[0].function))

    def test_143(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""
            var z VOTIEN = a.a.a[2].foo(1);
        ""","successful", inspect.stack()[0].function))

    def test_144(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""
            var z VOTIEN = a.a.a[2].c[2].foo(1, a.b);
        ""","successful", inspect.stack()[0].function))

    def test_145(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""
            var z VOTIEN = a.a.a[2].c[2].foo(1,);
        ""","Error on line 2 col 47: )", inspect.stack()[0].function))

    def test_146(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""
            var z VOTIEN = foo() + foo(2) + foo(2, 3, 4) + a;
        ""","successful", inspect.stack()[0].function))

    def test_147(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""
            var z VOTIEN = (a + 23) * 3 && (1 + 1);
        ""","successful", inspect.stack()[0].function))

    def test_148(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""
            var z VOTIEN = foo().a[2].goo();
        ""","successful", inspect.stack()[0].function))

    def test_149(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""
            const k = [2]int{1}[3][4].foo();
        ""","successful", inspect.stack()[0].function))

    def test_150(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""
            const k = ID {a : 2}.c[2] + 2[2] + true.foo() + (2).foo();
        ""","successful", inspect.stack()[0].function))

    def test_151(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""
            const k = -a + -!-!c - ---[2]int{2};
        ""","successful", inspect.stack()[0].function))

    def test_152(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""
            const k = foo() + foo(a{a:2}) + foo(2, 3,4);
        ""","successful", inspect.stack()[0].function))

    def test_153(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""
            const k =  int;
        ""","Error on line 2 col 23: int", inspect.stack()[0].function))

    def test_154(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""
            const k =  (1, 2);
        ""","Error on line 2 col 25: ,", inspect.stack()[0].function))

    def test_155(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            var a VOTIEN = 2 + 3 / 4;
        ""","successful", inspect.stack()[0].function))

    def test_156(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            var a [2][3]int = 2 + 3 / 4;
        ""","successful", inspect.stack()[0].function))

    def test_157(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            var a [][3]int = 2 + 3 / 4;
        ""","Error on line 2 col 19: ]", inspect.stack()[0].function))

    def test_158(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            var a = a.foo()[2];
        ""","successful", inspect.stack()[0].function))

    def test_159(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            var a = ;
        ""","Error on line 2 col 20: ;", inspect.stack()[0].function))

    def test_160(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            var a 1;
        ""","Error on line 2 col 18: 1", inspect.stack()[0].function))

    def test_161(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            var c [2][3]int;
        ""","successful", inspect.stack()[0].function))

    def test_162(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            var c [2][3]ID
        ""","successful", inspect.stack()[0].function))

    def test_163(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            const a;
        ""","Error on line 2 col 19: ;", inspect.stack()[0].function))

    def test_164(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            const a := 1 + foo.a[2];
        ""","Error on line 2 col 20: :=", inspect.stack()[0].function))

    def test_165(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            const a =;
        ""","Error on line 2 col 21: ;", inspect.stack()[0].function))

    def test_166(self):
        """Declared"""
        self.assertTrue(TestParser.test("""

            var a int; var d = 2;

            var d = 2;

            const a = 2; var d int = 3;


            var d = 2;""","successful", inspect.stack()[0].function))

    def test_167(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            func Add(x int, y [2]int) [2]id {return ;}
""","successful", inspect.stack()[0].function))

    def test_168(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            func Add() [2]id {return ;}
""","successful", inspect.stack()[0].function))

    def test_169(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            func Add(a) [2]id {return ;}
""","Error on line 2 col 22: )", inspect.stack()[0].function))

    def test_170(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            func Add(int a) int {return ;}
""","Error on line 2 col 21: int", inspect.stack()[0].function))

    def test_171(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            func Add() {return ;}
""","successful", inspect.stack()[0].function))

    def test_172(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            func Add(a int, ) {}
""","Error on line 2 col 28: )", inspect.stack()[0].function))

    def test_173(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            type Calculator struct {value int}
""","Error on line 2 col 45: }", inspect.stack()[0].function))

    def test_174(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            type Calculator struct {value int;}
""","successful", inspect.stack()[0].function))

    def test_175(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            type Calculator struct {

                value int;
                a [2]int; a [2]ID;
                c Calculator
            }
""","successful", inspect.stack()[0].function))

    def test_176(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            type Calculator struct {
                c Calculator
                c Cal a int;
            }
""","Error on line 4 col 22: a", inspect.stack()[0].function))

    def test_177(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            type Calculator struct {
                a int = 2;
            }
""","Error on line 3 col 22: =", inspect.stack()[0].function))

    def test_178(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            type Calculator interface {
                Add(x, y [2]ID) [2]int;
                Subtract(a, b float, c, e int);
                Reset()
                SayHello(name string)
            }
""","successful", inspect.stack()[0].function))

    def test_179(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            type Calculator interface {Reset()}
""","Error on line 2 col 46: }", inspect.stack()[0].function))

    def test_180(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            type Calculator interface {Reset()
        }
""","successful", inspect.stack()[0].function))

    def test_181(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            type Calculator interface {Reset();}
""","successful", inspect.stack()[0].function))

    def test_182(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            type Calculator interface {
                Add(x int,c,d ID); Add()
        }
""","successful", inspect.stack()[0].function))

    def test_183(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            type Calculator interface {
                Add(x int,c,d ID){}
        }
""","Error on line 3 col 33: {", inspect.stack()[0].function))

    def test_184(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            type Calculator interface {Reset();} type Person struct{value int;}
""","Error on line 2 col 49: type", inspect.stack()[0].function))

    def test_185(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            type Calculator interface {Reset();}; type Person struct{value int;}
""","successful", inspect.stack()[0].function))

    def test_186(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            func Add(x int, y int) int  {return ;};
""","successful", inspect.stack()[0].function))

    def test_187(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            func (c Calculator) Add(x int) int {return ;}
""","successful", inspect.stack()[0].function))

    def test_188(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            func (c int) Add(x int) int {return ;}
""","Error on line 2 col 20: int", inspect.stack()[0].function))

    def test_189(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            func (c c) Add(x int) {return ;}
""","successful", inspect.stack()[0].function))

    def test_190(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            func (c c) Add(x, c int) {return ;}
""","successful", inspect.stack()[0].function))

    def test_191(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            func (c [2]c) Add(x int) {return ;}
""","Error on line 2 col 20: [", inspect.stack()[0].function))

    def test_192(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            func (int c) Add(x int) {return ;}
""","Error on line 2 col 18: int", inspect.stack()[0].function))

    def test_193(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            func (c c) Add(x int) {return ;};
""","successful", inspect.stack()[0].function))

    def test_194(self):
        """Declared"""
        self.assertTrue(TestParser.test("""

            func (c c) Add(x int) {return ;}

            func Add(x int) {return ;}; var c int;

            var c int; type Calculator struct{c int;}; type Calculator struct{c int;} var c int;
""","Error on line 7 col 86: var", inspect.stack()[0].function))

    def test_195(self):
        """Declared"""
        self.assertTrue(TestParser.test("""

            var c int func (c c) Add(x int) {return ;}
""","Error on line 3 col 22: func", inspect.stack()[0].function))

    def test_196(self):
        """Declared"""
        self.assertTrue(TestParser.test("""

            const a = 2 func (c c) Add(x int) {return ;}
""","Error on line 3 col 24: func", inspect.stack()[0].function))

    def test_197(self):
        """Declared"""
        self.assertTrue(TestParser.test("""

            const MaxSize = 100 + 50; func (c c) Add() {return ;}
""","successful", inspect.stack()[0].function))

    def test_198(self):
        """Declared"""
        self.assertTrue(TestParser.test("""

""","Error on line 3 col 0: <EOF>", inspect.stack()[0].function))

    def test_199(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
            func Add() {
                                        }
""","successful", inspect.stack()[0].function))

    def test_200(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                         var a int = 2;
                                    };""","successful", inspect.stack()[0].function))

    def test_201(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                         var a int;
                                    };""","successful", inspect.stack()[0].function))

    def test_202(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                         var a = a[2].b;
                                    };""","successful", inspect.stack()[0].function))

    def test_203(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                         const a = a[2].b;
                                    };""","successful", inspect.stack()[0].function))

    def test_204(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        const a = a[2].b
                                        var a = a[2].b; var a = "s";
                                    };""","successful", inspect.stack()[0].function))

    def test_205(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        const a = a[2].b
                                        var a = a[2].b var a = "s";
                                    };""","Error on line 4 col 55: var", inspect.stack()[0].function))

    def test_206(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        a += 2;
                                        a -= a[2].b();
                                        a /= 2
                                        a *= 2
                                        a %= 2;
                                    };""","successful", inspect.stack()[0].function))


    def test_207(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        a[2].b := 2;
                                    };""","successful", inspect.stack()[0].function))


    def test_208(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        a.c[2].e[3].k += 2;
                                    };""","successful", inspect.stack()[0].function))

    def test_209(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        a.foo() += 2;
                                    };""","Error on line 3 col 48: +=", inspect.stack()[0].function))

    def test_210(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        2 + 2 += 2;
                                    };""","Error on line 3 col 40: 2", inspect.stack()[0].function))

    def test_211(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                       ID {id:2}.c += 2;
                                    };""","Error on line 3 col 42: {", inspect.stack()[0].function))

    def test_212(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                       a[2+3&&2] += foo().b[2];
                                    };""","successful", inspect.stack()[0].function))

    def test_213(self):
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

    def test_214(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        if (x.foo().b[2]) {
                                            if (){return;}
                                        }
                                    };""","Error on line 4 col 48: )", inspect.stack()[0].function))

    def test_215(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        if (x.foo().b[2]) {
                                            if (1){return; } else {return; }

                                        } else if(2) {return;
                                        }
                                    };""","successful", inspect.stack()[0].function))

    def test_216(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        if (x.foo().b[2]) {return
                                        } else if(){
                                        }
                                    };""","Error on line 4 col 50: )", inspect.stack()[0].function))

    def test_217(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        if (x.foo().b[2]) {return;
                                        } else if(1){return;
                                        }else if(1){return;
                                        }else if(2){return
                                        }else {return;
                                        }
                                    };""","successful", inspect.stack()[0].function))

    def test_218(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        for true {return; }
                                    };""","successful", inspect.stack()[0].function))

    def test_219(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        for true + 2 + foo().b {return; }
                                    };""","successful", inspect.stack()[0].function))

    def test_220(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        for int {return; }
                                    };""","Error on line 3 col 44: int", inspect.stack()[0].function))

    def test_221(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        for int {return; }
                                    };""","Error on line 3 col 44: int", inspect.stack()[0].function))

    def test_222(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        for i := 0; i < 10; i += 1 {
                                           return;
                                        }
                                    };""","successful", inspect.stack()[0].function))

    def test_223(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        for var i = 0; i < 10; i += 1 {
                                           return;
                                        }
                                    };""","successful", inspect.stack()[0].function))

    def test_224(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        for const i = 0; i < 10; i += 1 {
                                            return;
                                        }
                                    };""","Error on line 3 col 44: const", inspect.stack()[0].function))

    def test_225(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        for var i [2] int = 0; foo().a.b(); i[3] := 1 {
                                            return;
                                        }
                                    };""","Error on line 3 col 77: [", inspect.stack()[0].function))

    def test_226(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        for var i [2]int = 0; foo().a.b();  {
                                            return;
                                        }
                                    };""","Error on line 3 col 76: {", inspect.stack()[0].function))

    def test_227(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        for var i [2]int = 0; foo().a.b(); var i [2]int = 0 {
                                            return;
                                        }
                                    };""","Error on line 3 col 75: var", inspect.stack()[0].function))

    def test_228(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        for index, value := range arr {
                                        // index: 0, 1, 2
                                        // value: 10, 20, 30
                                        return;
                                        }
                                    };""","successful", inspect.stack()[0].function))

    def test_229(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        for index[2], value := range arr {
                                        // index: 0, 1, 2
                                        // value: 10, 20, 30
                                        return;
                                        }
                                    };""","Error on line 3 col 52: ,", inspect.stack()[0].function))

    def test_230(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        for index.ab, value := range arr {
                                        // index: 0, 1, 2
                                        // value: 10, 20, 30
                                        return;
                                        }
                                    };""","Error on line 3 col 52: ,", inspect.stack()[0].function))

    def test_231(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        for index, value[2] := range arr {
                                        // index: 0, 1, 2
                                        return;
                                        }
                                    };""","Error on line 3 col 56: [", inspect.stack()[0].function))

    def test_232(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        for index, value := range arr[2] {return
                                        }
                                    };""","successful", inspect.stack()[0].function))

    def test_233(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        for index, value := range 23 {return;
                                        }
                                    };""","successful", inspect.stack()[0].function))

    def test_234(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        for index, value := range 23 {
                                            for index, value := range 23 {return; }
                                        }
                                    };""","successful", inspect.stack()[0].function))

    def test_235(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        break;
                                        continue
                                        break; continue; break
                                    };""","successful", inspect.stack()[0].function))

    def test_236(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        return
                                        return 2 + a[2].b()
                                        return; return a
                                    };""","successful", inspect.stack()[0].function))

    def test_237(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        return return 2 + a[2].b()

                                    };""","Error on line 3 col 47: return", inspect.stack()[0].function))

    def test_238(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        break continue

                                    };""","Error on line 3 col 46: continue", inspect.stack()[0].function))

    def test_239(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        a.foo();
                                        foo()
                                    };""","successful", inspect.stack()[0].function))

    def test_240(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        a.foo(2 + 3, a {a:2})
                                        foo(2 + 3, a {a:2});
                                    };""","successful", inspect.stack()[0].function))

    def test_241(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        (1+2).foo(2 + 3, a {a:2})
                                    };""","Error on line 3 col 40: (", inspect.stack()[0].function))

    def test_242(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        a[2][3].foo(2 + 3, a {a:2})
                                    };""","successful", inspect.stack()[0].function))

    def test_243(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        {break;}
                                    };""","Error on line 3 col 40: {", inspect.stack()[0].function))

    def test_244(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                        break;
                                    func Add() {
                                    };""","Error on line 2 col 40: break", inspect.stack()[0].function))

    def test_245(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        return (2 + 3).b
                                        return -1.c
                                    };""","Error on line 4 col 50: c", inspect.stack()[0].function))

    def test_246(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        return (2 + 3)[b]
                                        return -1.c[c]
                                    };""","Error on line 4 col 50: c", inspect.stack()[0].function))

    def test_247(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        if (1) {return struct;}
                                        else if(2) {return string;}
                                        else if(3) {reutrn int;}
                                    };""","Error on line 3 col 55: struct", inspect.stack()[0].function))

    def test_248(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        if (1) {return;}else if(2) {return string;}else if(3) {reutrn int;}
                                    };""","Error on line 3 col 75: string", inspect.stack()[0].function))

    def test_249(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        if (1) {return;}else if(2) {return string;}else if(3) {reutrn int;}else  {return struct;}
                                    };""","Error on line 3 col 75: string", inspect.stack()[0].function))

    def test_250(self):
        """array_literal"""
        self.assertTrue(TestParser.test("""const a = [1]int{1+1}
""","Error on line 1 col 18: +", inspect.stack()[0].function))

    def test_251(self):
        """array_literal"""
        self.assertTrue(TestParser.test("""const a = [1]int{{1, 0x1}, ID{}, {{ID{}}}}
""","successful", inspect.stack()[0].function))

    def test_252(self):
        """array_literal"""
        self.assertTrue(TestParser.test("""const a = [1]int{}
""","Error on line 1 col 17: }", inspect.stack()[0].function))

    def test_253(self):
        """array_literal"""
        self.assertTrue(TestParser.test("""const a = [1]int{[1]int{1}}
""","Error on line 1 col 17: [", inspect.stack()[0].function))

    def test_254(self):
        """array_literal"""
        self.assertTrue(TestParser.test("""const a = [1]int{{1, 0x1}, ID{}, 1.2, "s", true, false, nil} + nil
""","successful", inspect.stack()[0].function))

    def test_255(self):
        self.assertTrue(TestParser.test("""
        func Add(x, y int, b float) {return ;}
""","successful", inspect.stack()[0].function))

    def test_256(self):
        self.assertTrue(TestParser.test("""
        func (c c) Add(x, y int, b float) {return ;}
""","successful", inspect.stack()[0].function))

    def test_257(self):
        self.assertTrue(TestParser.test("""
        type Person struct {
            func (p Person) Greet() string {
                return "Hello, " + p.name
            }
            c c
            func (c c) Add(x, y int, b float) {return ;}
            value int;
        }
""","successful", inspect.stack()[0].function))

    def test_258(self):
        self.assertTrue(TestParser.test("""
        type Person struct {
            c int  c int;
        }
""","Error on line 3 col 19: c", inspect.stack()[0].function))

    def test_259(self):
        self.assertTrue(TestParser.test("""
            func (p Person) Greet() string {
                for i := 0
                    i < 10
                    i += 1 {
                    return
                }
                for i := 0
                    i < 10
                    i += 1
                {
                    return
                }
            };
""","Error on line 10 col 26: ;", inspect.stack()[0].function))

    def test_260(self):
        self.assertTrue(TestParser.test("""
            func (p Person) Greet() string {
                if (1) {return;}
                else if (1)
                {}
            };
""","Error on line 4 col 16: else", inspect.stack()[0].function))

    def test_261(self):
        self.assertTrue(TestParser.test("""
            func (p Person) Greet() string {
                if (1) {return;
                }else if (1) {}
            };
""","successful", inspect.stack()[0].function))

    def test_262(self):
        self.assertTrue(TestParser.test("""
            func (p Person) Greet() string {
                if (1) {return;
                }else {}
            };
""","successful", inspect.stack()[0].function))

    def test_263(self):
        self.assertTrue(TestParser.test("""
            func (p Person) Greet() string {
                if (1) {}
            };
""","successful", inspect.stack()[0].function))

    def test_264(self):
        self.assertTrue(TestParser.test("""
            func (p Person) Greet() string {
                for i < 10 {
// loop body
}
            };
""","successful", inspect.stack()[0].function))

    def test_265(self):
        self.assertTrue(TestParser.test("""
            func (p Person) Greet() string {
                for i := 0; i < 10; i += 1 {
// loop body
}
            };
""","successful", inspect.stack()[0].function))

    def test_266(self):
        self.assertTrue(TestParser.test("""
            func (p Person) Greet() string {
                for index, value := range STRUCT{} {
// loop body
};
            };
""","successful", inspect.stack()[0].function))

    def test_267(self):
        self.assertTrue(TestParser.test("""
        const a = a.2;
""","Error on line 2 col 20: 2", inspect.stack()[0].function))

    def test_268(self):
        self.assertTrue(TestParser.test("""
        const a = a.b.c().d().e[2].k()[2];
""","successful", inspect.stack()[0].function))

    def test_269(self):
        self.assertTrue(TestParser.test("""
        const a = [1]int{1, 2
""","Error on line 2 col 29: ;", inspect.stack()[0].function))

    def test_270(self):
        self.assertTrue(TestParser.test("""
        const a = foo(1, 2
""","Error on line 2 col 26: ;", inspect.stack()[0].function))

    def test_271(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        for var i [2] int = 0; foo().a.b(); i.b := 1 {
                                            return;
                                        }
                                    };""","Error on line 3 col 77: .", inspect.stack()[0].function))

    def test_272(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        for var i [2] int = 0; foo().a.b(); i[2].c += 1 {
                                            return;
                                        }
                                    };""","Error on line 3 col 77: [", inspect.stack()[0].function))

    def test_273(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        for i[2] := 1; foo().a.b(); i := 1 {
                                            return;
                                        }
                                    };""","Error on line 3 col 49: :=", inspect.stack()[0].function))

    def test_274(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        for i.c[2] := 1; foo().a.b(); i := 1 {
                                            return;
                                        }
                                    };""","Error on line 3 col 51: :=", inspect.stack()[0].function))

    def test_275(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        for i.c[2] := 1; foo().a.b(); i := 1 {
                                            return;
                                        }
                                    };""","Error on line 3 col 51: :=", inspect.stack()[0].function))

    def test_276(self):
        self.assertTrue(TestParser.test("""
        type Person struct {
            func (p Person) Greet() string {
                return "Hello, " + p.name
            };
        }
""","Error on line 3 col 12: func", inspect.stack()[0].function))

    def test_277(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        for var b; foo().a.b(); i := 1 {
                                            return;
                                        }
                                    };""","Error on line 3 col 49: ;", inspect.stack()[0].function))

    def test_278(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        for var b int; foo().a.b(); i := 1 {
                                            return;
                                        }
                                    };""","Error on line 3 col 53: ;", inspect.stack()[0].function))

    def test_279(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        for var b [2]ID = 1 + 2 / 4; foo().a.b(); i := 1 {
                                            return;
                                        }
                                    };""","successful", inspect.stack()[0].function))

    def test_280(self):
        self.assertTrue(TestParser.test("""
                                            const a = [ID][2][VT]int{a, b, {c}}
                                        ""","successful", inspect.stack()[0].function))

    def test_281(self):
        self.assertTrue(TestParser.test("""
                                            var a;
                                        ""","Error on line 2 col 49: ;", inspect.stack()[0].function))
    def test_282(self):
        self.assertTrue(TestParser.test("""
                                            var a = {1, 2};
                                        ""","Error on line 2 col 52: {", inspect.stack()[0].function))

    def test_283(self):
        self.assertTrue(TestParser.test("""
                                            var a = {1, 2};
                                        ""","Error on line 2 col 52: {", inspect.stack()[0].function))

    def test_284(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        {
                                            return;
                                        }
                                    };""","Error on line 3 col 40: {", inspect.stack()[0].function))

    def test_285(self):
        self.assertTrue(TestParser.test("""
                                            const a = [ID][2][VT]int{a, b, {c}}
                                        ""","successful", inspect.stack()[0].function))

    def test_286(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                            return;
                                    };""","successful", inspect.stack()[0].function))

    def test_287(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                            return true;
                                        };""","successful", inspect.stack()[0].function))

    def test_288(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                            return false;
                                        };""","successful", inspect.stack()[0].function))

    def test_289(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                            const a = a[2].b;
                                            var x = x.y.z;
                                        };""","successful", inspect.stack()[0].function))