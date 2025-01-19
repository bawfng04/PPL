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
            func VoTien(x int, y int) int {}
            func VoTien1() [2][3] ID {}
            func VoTien2() {}
        ""","successful", inspect.stack()[0].function))

    def test_013(self):
        """declared method"""
        self.assertTrue(TestParser.test("""
            func (c Calculator) VoTien(x int) int {}
            func (c Calculator) VoTien() ID {}
            func (c Calculator) VoTien(x int, y [2]VoTien) {}
        ""","successful", inspect.stack()[0].function))

    def test_014(self):
        """declared struct"""
        self.assertTrue(TestParser.test("""
            type VoTien struct {
                VoTien string;
                VoTien [1][3]VoTien;
            }
            type VoTien struct {}
        ""","successful", inspect.stack()[0].function))

    def test_015(self):
        """declared Interface"""
        self.assertTrue(TestParser.test("""
            type VoTien struct {
                VoTien string ;
                VoTien [1][3]VoTien ;
            }
            type VoTien struct {}
        ""","successful", inspect.stack()[0].function))

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
        ""","successful", inspect.stack()[0].function))

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
                if (x > 10) {}
                if (x > 10) {

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
                for i < 10 {}
                for i := 0; i < 10; i += 1 {}
                for index, value := range array {}
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

#Testcase của Bằng

    def test_022(self):
        """variable declaration"""
        self.assertTrue(TestParser.test("var x int;","successful", inspect.stack()[0].function))

    def test_023(self):
        """variable declaration with initialization"""
        self.assertTrue(TestParser.test("var x = 10;","successful", inspect.stack()[0].function))

    def test_024(self):
        """constant declaration"""
        self.assertTrue(TestParser.test("const y = 3.14;","successful", inspect.stack()[0].function))

    def test_025(self):
        """function declaration with no parameters"""
        self.assertTrue(TestParser.test("func foo() {}","successful", inspect.stack()[0].function))

    def test_026(self):
        """function declaration with parameters"""
        self.assertTrue(TestParser.test("func add(a int, b int) int {}","successful", inspect.stack()[0].function))

    def test_027(self):
        """method declaration"""
        self.assertTrue(TestParser.test("func (p Person) greet() string {}","successful", inspect.stack()[0].function))

    def test_028(self):
        """struct declaration"""
        self.assertTrue(TestParser.test("""
            type Person struct {
                name string;
                age int;
            }
        ""","successful", inspect.stack()[0].function))

    def test_029(self):
        """interface declaration"""
        self.assertTrue(TestParser.test("""
            type Greeter interface {
                greet() string;
            }
        ""","successful", inspect.stack()[0].function))

    def test_030(self):
        """if statement"""
        self.assertTrue(TestParser.test("""
            func check(x int) {
                if (x > 0) {
                    return true;
                } else {
                    return false;
                }
            }
        ""","successful", inspect.stack()[0].function))

    def test_031(self):
        """for loop with condition"""
        self.assertTrue(TestParser.test("""
            func loop() {
                for i < 10 {
                    i += 1;
                }
            }
        ""","successful", inspect.stack()[0].function))

    def test_032(self):
        """for loop with initialization and update"""
        self.assertTrue(TestParser.test("""
            func loop() {
                for i := 0; i < 10; i += 1 {}
            }
        ""","successful", inspect.stack()[0].function))

    def test_033(self):
        """for loop with range"""
        self.assertTrue(TestParser.test("""
            func loop() {
                for index, value := range array {}
            }
        ""","successful", inspect.stack()[0].function))

    def test_034(self):
        """break statement"""
        self.assertTrue(TestParser.test("""
            func loop() {
                for i < 10 {
                    if (i == 5) {
                        break;
                    }
                    i += 1;
                }
            }
        ""","successful", inspect.stack()[0].function))

    def test_035(self):
        """continue statement"""
        self.assertTrue(TestParser.test("""
            func loop() {
                for i < 10 {
                    if (i == 5) {
                        continue;
                    }
                    i += 1;
                }
            }
        ""","successful", inspect.stack()[0].function))

    def test_036(self):
        """return statement"""
        self.assertTrue(TestParser.test("""
            func add(a int, b int) int {
                return a + b;
            }
        ""","successful", inspect.stack()[0].function))

    def test_037(self):
        """call statement"""
        self.assertTrue(TestParser.test("""
            func main() {
                foo(2 + x, 4 / y);
                m.goo();
            }
        ""","successful", inspect.stack()[0].function))

    def test_038(self):
        """nested if statement"""
        self.assertTrue(TestParser.test("""
            func check(x int) {
                if (x > 0) {
                    if (x < 10) {
                        return true;
                    }
                } else {
                    return false;
                }
            }
        ""","successful", inspect.stack()[0].function))

    def test_039(self):
        """nested for loop"""
        self.assertTrue(TestParser.test("""
            func nestedLoop() {
                for i := 0; i < 10; i += 1 {
                    for j := 0; j < 5; j += 1 {}
                }
            }
        ""","successful", inspect.stack()[0].function))

    def test_040(self):
        """array declaration"""
        self.assertTrue(TestParser.test("var arr [5]int;","successful", inspect.stack()[0].function))

    def test_041(self):
        """multi-dimensional array declaration"""
        self.assertTrue(TestParser.test("var multiArr [2][3]int;","successful", inspect.stack()[0].function))

    def test_042(self):
        """array literal"""
        self.assertTrue(TestParser.test("var arr = [3]int{1, 2, 3};","successful", inspect.stack()[0].function))

    def test_043(self):
        """struct literal"""
        self.assertTrue(TestParser.test("""
            var p = Person{name: "Alice", age: 30};
        ""","successful", inspect.stack()[0].function))

    def test_044(self):
        """access struct field"""
        self.assertTrue(TestParser.test("""
            var p = Person{name: "Alice", age: 30};
            var name = p.name;
        ""","successful", inspect.stack()[0].function))

    def test_045(self):
        """modify struct field"""
        self.assertTrue(TestParser.test("""
            func main() {
                var p = Person{name: "Alice", age: 30};
                p.age = 31;
            }
        ""","successful", inspect.stack()[0].function))

    def test_046(self):
        """method call on struct"""
        self.assertTrue(TestParser.test("""
            func (p Person) greet() string {
                return "Hello, " + p.name;
            }
            var p = Person{name: "Alice"};
            var greeting = p.greet();
        ""","successful", inspect.stack()[0].function))

    def test_047(self):
        """boolean expression"""
        self.assertTrue(TestParser.test("var result = true && false || !true;","successful", inspect.stack()[0].function))

    def test_048(self):
        """arithmetic expression"""
        self.assertTrue(TestParser.test("var result = 1 + 2 * 3 - 4 / 5 % 6;","successful", inspect.stack()[0].function))

    def test_049(self):
        """comparison expression"""
        self.assertTrue(TestParser.test("var result = 1 < 2 && 3 >= 4;","successful", inspect.stack()[0].function))

    def test_050(self):
        """string concatenation"""
        self.assertTrue(TestParser.test('var str = "Hello" + " " + "World";',"successful", inspect.stack()[0].function))