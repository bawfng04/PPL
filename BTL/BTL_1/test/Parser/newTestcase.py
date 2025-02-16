import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
# -------------------------------------------------------------------------------------------------
################################################################################################
###################################################################################################
####################################################################################################
########################################################################################################


    def test_001(self):
        input = """ func main(){
        str1 := "Hello"
str2 := "World"
str3 := str1 + " " + str2 // str3 == "Hello World"
str4 := "apple"
str5 := "banana"
result := str4 == str5 // result == false
}
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))
    def test_002(self):
        input = """
        var arr [5]int; // defines an array of 5 integers.
var multi_arr [2][5][100][-100][100]int; // defines an array of 2 x 5 integers.
        """
        expect = "Error on line 3 col 27: -"
        self.assertTrue(TestParser.checkParser(input,expect,202))
    def test_003(self):
        input = """
        func main(){
        a := multi_arr[0][1000][-1][1.2] b := 10
        }
        """
        expect = "Error on line 3 col 42: b"
        self.assertTrue(TestParser.checkParser(input, expect, 203))

    def test_004(self):
        input = """
        var arr [2 + 3]int;
        """
        expect = "Error on line 2 col 20: +"
        self.assertTrue(TestParser.checkParser(input, expect, 204))

    def test_005(self):
        input = """
        type s struct { a int; b b; c c; a a123;
         b float; hello hello; arr [5]int; arr [1000][100]hello.hello
        };
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 205))

    def test_006(self):
        input = """func H() Person{
        if ():= true;}
        """
        expect = "Error on line 2 col 13: )"
        self.assertTrue(TestParser.checkParser(input, expect, 206))

    def test_007(self):
        input = """func H() Person{
        x := arr[(53)];
        x := arr[3,23];
        }
        """
        expect = "Error on line 3 col 19: ,"
        self.assertTrue(TestParser.checkParser(input, expect, 207))

    def test_008(self):
        input = """func H() Person{
        str := "Hello World
        }
        """
        expect = """"Hello World"""
        self.assertTrue(TestParser.checkParser(input, expect, 208))

    def test_009(self):
        input = """func H() Person{
        /* This is a comment */
        a := 0o101;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 209))

    def test_010(self):
        input = """
        var arr []int;
        """
        expect = "Error on line 2 col 18: ]"
        self.assertTrue(TestParser.checkParser(input, expect, 210))

    def test_011(self):
        input = """
        var arr [-5]int;
        """
        expect = "Error on line 2 col 18: -"
        self.assertTrue(TestParser.checkParser(input, expect, 211))

    def test_012(self):
        input = """
        func H() Person{
        a := 5 < 10 > 3;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 212))

    def test_013(self):
        input = """
        func H() Person{
        result := (a + b * c) % d == e && !f || g;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 213))

    def test_014(self):
        input = """
        var arr [5][3];
        """
        expect = "Error on line 2 col 23: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 214))

    def test_015(self):
        input = """
        func H() Person{
        a := 5.5 % 2.0;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 215))

    def test_016(self):
        input = """func H() Person{
        x := person.123;
        }
        """
        expect = "Error on line 2 col 21: 123"
        self.assertTrue(TestParser.checkParser(input, expect, 216))

    def test_017(self):
        input = """
        type Person struct {
        name string ;
age int ;
radius float;
            shape Shape; 
}
func H() Person{
p := Person{name: "Alice", age: 30}
p := Person{}
PutStringLn(p.name) 
PutIntLn(p.age) // Output: 30
p.age := 31
PutIntLn(p.age) // Output: 31
}
func (p Person) Greet() string {
return "Hello, " + p.name
PutStringLn(p.Greet()) // Output: Hello, Alice
}

        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 217))


    def test_018(self):
        input = """
        type Shape interface {
            Area() float
            Perimeter(w, h int) float
            Draw(name string, scale float) int
            Rotate(angle float, speed int) string
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 218))


    def test_019(self):
        input = """
        type InvalidInterface interface {
            Method1() Method2()
        }
        """
        expect = "Error on line 3 col 30: ("
        self.assertTrue(TestParser.checkParser(input, expect, 219))

    def test_020(self):
        input = """
        type Test interface {
            Add(x, y int, z);
        }
        """
        expect = "Error on line 3 col 28: )"
        self.assertTrue(TestParser.checkParser(input, expect, 220))


    def test_021(self):
        input = """
        type Test interface {
            type(a int);
        }
        """
        expect = "Error on line 3 col 13: type"
        self.assertTrue(TestParser.checkParser(input, expect, 221))


    def test_022(self):
        input = """
        type Empty interface {}
        """
        expect = "Error on line 2 col 31: }"
        self.assertTrue(TestParser.checkParser(input, expect, 222))


    def test_023(self):
        input = """
        type WrongSyntax {
            Method();
        }
        """
        expect = "Error on line 2 col 26: {"
        self.assertTrue(TestParser.checkParser(input, expect, 223))


    def test_024(self):
        input = """
        type Test interface {
            Process(data string) int float;
        }
        """
        expect = "Error on line 3 col 38: float"
        self.assertTrue(TestParser.checkParser(input, expect, 224))

    def test_025(self):
        input = """
        var globalVar int = 10; 
        func main() {
            var localVar = 20; 
            var x, y int = 5, 10; 
            var z float; 
            var a = "Hello"; 
            var b int = globalVar + localVar; 
            var c = x + y; 
            var d = c * 2; 
            var e float = 3.14; 
            var f = e + 2.0; 
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 225)) 

    def test_026(self):
        input = """
        var x int = 5; 
        func main() {
            var x = 10; 
            {
                var x = 15; 
                var y = x + 5; 
            }
            var y = x + 1; 
        }
        func foo(x int) {
            var x = 20; 
            var y = x + 10; 
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 226))

    def test_027(self):
        input = """
        var arr [5]int; 
        var matrix [2][3]float; 
        var str string = "Hello"; 
        var person = Person { name : "HELLO" , age : 97 }; 
        var calc Calculator; 
        func main() {
            var x = arr[0]; 
            var y = matrix[1][2]; 
            var z = person.name; 
            var w = calc.Add(1, 2); 
            var invalid = x + y; 
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 227))

    def test_028(self):

        self.assertTrue(TestParser.checkParser("""
                                        func createArray() [5]int {
	var arr [5]int
	for i := 0; i < len(arr); i+=1 {
		arr[i] := i * 2
	}
	return arr
}

func main() {
	for j, value := range createArray(2+2).hello(1+2) {
		fmt.Printf("createArray()[%d] = %d\\n", j, value)
	}
}
""","successful", 228))
    def test_029(self):
        input = """
        func Add(x int, y int) int {
            return x + y;
        }
        type Calculator struct {
            value int;
        }
        func (c Calculator) Increment(n int) STUDENT {
            c.value := c.value + n;
            return c.value;
        }
        func Process(a, b int, c float, d string) string {
        return d + " processed";
    }
    func Sum(a, a int) [5][CONST]int { 
        return a + a;
    }
func (s Student) GetName() string {
        return s.name;
    }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 229))
    
    def test_030(self):
        input = """
        func c Calculator Reset() { 
            c.value = 0;
        }
        """
        expect = "Error on line 2 col 16: Calculator"
        self.assertTrue(TestParser.checkParser(input, expect, 230))

    def test_031(self):
        input = """
        func SayHello() fmt.Print("Hello") ;
        }
        
        """
        expect = "Error on line 2 col 34: ("
        self.assertTrue(TestParser.checkParser(input, expect, 231))

    def test_032(self):
        input = """func B(a ,b int)float {
        person.getAddress().city := "New York";
        y := 5.5 % 2.0;
        str := "Hello" + 42;
        x := -a + !b * c;
        result := add(3, 4) * 5;
        flag := (a > b) && (c <= d) || !(e == f);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,232))

    def test_033(self):
        input = """
        func B(a ,b int)float {
        p := Person{name: "Alice" age: 30};
        }
        """
        expect = "Error on line 3 col 35: age"
        self.assertTrue(TestParser.checkParser(input, expect, 233))

    def test_034(self):
        input = """
        func B(a ,b int)float {
        x := arr[];
        x+y := 6
        }
        """
        expect = "Error on line 3 col 18: ]"
        self.assertTrue(TestParser.checkParser(input, expect, 234))

    def test_035(self):
        input = """
        func B(a ,b int)float {
        x := 5;
        2+2
        y := x + 10;
        z := "Hello";
        arr[2] := 10;
        arr[0] := arr[1] + arr[2];
        person.name := "John";
        person.age := 30;
        x += 10;
        y -= 5;
        z *= 2;
        arr[0] /= 3;
        x := 5;
        y := x + 10;
        z := y * 2;
        x := 5;
        y := z + 10;
        x := (a + b) * (c - d) / e % f;
        arr[2] := (a + b) * (c - d) / e % f;
        person.age := (a + b) * (c - d) / e % f;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 235))

    def test_036(self):
        input = """
        func B(a ,b int)float {
        if (x > 10) {
            print("> 10");
        } else if (x == 10) {
            print("= 10");
        } else {
            print("< 10");
        }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 236))

    def test_037(self):
        input = """
        func B(a ,b int)float {
        if (x > 0) print("+");
        }
        """
        expect = "Error on line 3 col 20: print"
        self.assertTrue(TestParser.checkParser(input, expect, 237))

    def test_038(self):
        input = """
        func B(a ,b int)float {
        if (x ++ 5) {
            print("hello");
        }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 238))

    def test_039(self):
        input = """
        func B(a ,b int)float {
        if (a) {
            if (b) {
                print("hello");
            }
        }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 239))

    def test_040(self):
        input = """
        func B(a ,b int)float {
        if () {
            print("hello");
        }
        }
        """
        expect = "Error on line 3 col 13: )"
        self.assertTrue(TestParser.checkParser(input, expect, 240))

    def test_041(self):
        input = """
        if (x) {
            print("X");
        } else if () {
            print("hello");
        }
        """
        expect = "Error on line 2 col 9: if"
        self.assertTrue(TestParser.checkParser(input, expect, 241))

    def test_042(self):
        input = """
        func B(a ,b int)float {
        else {
            print("hello");
        }
        }
        """
        expect = "Error on line 3 col 9: else"
        self.assertTrue(TestParser.checkParser(input, expect, 242))

    def test_043(self):
        input = """
        func B(a ,b int)float {
        if (x) {} 
        else {} 
        else {}
        }
        """
        expect = "Error on line 4 col 9: else"
        self.assertTrue(TestParser.checkParser(input, expect, 243))

    
    def test_044(self):
        input = """
        func B(a ,b int)float {
        else if (x) {}
        }
        """
        expect = "Error on line 3 col 9: else"
        self.assertTrue(TestParser.checkParser(input, expect, 244))

    def test_045(self):
        input = """
        func B(a ,b int)float {
        if (a && b || !(c >= d + 5)) {
            print("hello");
        }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 245))

    def test_046(self):
        input = """
        func B(a ,b int)float {
        for i < 10 {
            if (i % 2 == 0) {
                print("even");
            }
        }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 246))

    def test_047(self):
        input = """
        func B(a ,b int)float {
        for i := 0; i < 5; i += 1 {
            if (i == 3) {
                print("= 3");
            } else {
                print("!= 3");
            }
        }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 247))

    def test_048(self):
        input = """
        func B(a ,b int)float {
        for idx, val := range arr {
            if (val > 100) {
                break;
            }
            print(val);
        }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 248))

    def test_049(self):
        input = """
        func B(a ,b int)float {
        for i < 5 {
            if (i == 2){
                print("error");
        }
        }
        """
        expect = "Error on line 8 col 9: <EOF>"
        self.assertTrue(TestParser.checkParser(input, expect, 249))

    def test_050(self):
        input = """
        func B(a ,b int)float {
        for i := 0; i < 3; i += 1 {
            if (i % 2 == 0) {
                for j := 0; j < 2; j += 1 {
                    print(i, j);
                }
            }
        }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 250))

    def test_051(self):
        input = """
        func B(a ,b int)float {
        for i := 0; i 10; i += 1 {
            print(i);
        }
        }
        """
        expect = "Error on line 3 col 23: 10"
        self.assertTrue(TestParser.checkParser(input, expect, 251))

    def test_052(self):
        input = """
        func B(a ,b int)float {
        if (x > 0) {
            print("+");
        } else {
            for i := 0; i < 3; i += 1 {
                print("-");
            }
        }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 252))

    def test_053(self):
        input = """
        func B(a ,b int)float {
        break; 
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 253))

    def test_054(self):
        input = """
        func B(a ,b int)float {
        for _, val := range arr {
            if (val == "STOP") {
                break;
            }
        }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 254))

    def test_055(self):
        input = """
        func B(a ,b int)float {
        for idx val := range arr { 
            print(idx, val);
        }
        }
        """
        expect = "Error on line 3 col 17: val"
        self.assertTrue(TestParser.checkParser(input, expect, 255))

    def test_056(self):
        input = """
        func B(a ,b int)float {
        for i < 5 {}
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 256))

    def test_057(self):
        input = """
        func B(a ,b int)float {
        if (for i < 5 {}) {
            print("invalid");
        }
        }
        """
        expect = "Error on line 3 col 13: for"
        self.assertTrue(TestParser.checkParser(input, expect, 257))

    def test_058(self):
        input = """
        func B(a ,b int)float {
        for i := 0; i < 10; i += 1 {
            if (i < 5) {
                print("small");
            } else if (i < 8) {
                print("medium");
            } else {
                print("large");
            }
        }
        return x+y
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 258))

    def test_059(self):
        input = """
        func B(a ,b int)float {
        for i := 0 i < 5 i += 1 { 
            print(i);
        }
        return x+ y
        }
        """
        expect = "Error on line 3 col 20: i"
        self.assertTrue(TestParser.checkParser(input, expect, 259))

    def test_060(self):
        input = """
        func B(a ,b int)float { 
        for {
            if (x == 0) {
                break;
            }
        }
        }
        """
        expect = "Error on line 3 col 13: {"
        self.assertTrue(TestParser.checkParser(input, expect, 260))

    def test_061(self):
        input = """
        func B(a ,b int)float {
        for i := 0; (i < 10 && j > 5) || k == 0; i += 1 {
            print(i);
        }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 261))

    def test_062(self):
        input = """
        func B(a ,b int)int {
        for var i = 0; i < 5; i += 1 {} 
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 262))

    def test_063(self):
        input = """
        func (c c) A(){
        for idx, person := range people {
            if (person.age > 18) {
                print("mature");
            }
        }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 263))

    def test_064(self):
        input = """
        func (c c) A(){
        for ; ; { 
            print("Loop");
        }
        }
        """
        expect = "Error on line 3 col 13: ;"  
        self.assertTrue(TestParser.checkParser(input, expect, 264))

    def test_065(self):
        input = """
        func A(){
        if (x) {
            print("X");
        } else if (y) {
            for i := 0; i < 3; i += 1 {
                print("Y");
            }
        } else {
            print("another");
        }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 265))
    
    def test_066(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for var b int; foo().a.b(); i := 1 {
                                            return; 
                                        }
                                    };""","successful", 266))
    def test_067(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Multiply() {
                                        for var c float; bar().x.y(); j := 2 {
                                            return; 
                                        }
                                    };""","successful", 267))

    def test_068(self):
            """Statement"""
            self.assertTrue(TestParser.checkParser("""
                                        func Subtract() {
                                            for var d string; baz().p.q(); k := 3 {
                                                return; 
                                            }
                                        };""","successful", 268))

    def test_069(self):
            """Statement"""
            self.assertTrue(TestParser.checkParser("""
                                        func Divide() {
                                            for var e bool; qux().r.s(); l := 4 {
                                                return; 
                                            }
                                        };""","successful", 269))

    def test_070(self):
            """Statement"""
            self.assertTrue(TestParser.checkParser("""
                                        func Modulo() {
                                            for var f char; quux().u.v(); m := 5 {
                                                return; 
                                            }
                                        };""","successful", 270))

    def test_071(self):
            """Statement"""
            self.assertTrue(TestParser.checkParser("""
                                        func Power() {
                                            for var g int; corge().w.x(); n := 6 {
                                                return; 
                                            }
                                        };""","successful", 271))

    def test_072(self):
            """Statement"""
            self.assertTrue(TestParser.checkParser("""
                                        func Log() {
                                            for var h float; grault().y.z(); o := 7 {
                                                return; 
                                            }
                                        };""","successful", 272))

    def test_073(self):
            """Statement"""
            self.assertTrue(TestParser.checkParser("""
                                        func Exp() {
                                            for var i string; garply().a.b(); p := 8 {
                                                return; 
                                            }
                                        };""","successful", 273))

    def test_074(self):
            """Statement"""
            self.assertTrue(TestParser.checkParser("""
                                        func Sqrt() {
                                            for var j bool; waldo().c.d(); q := 9 {
                                                return; 
                                            }
                                        };""","successful", 274))

    def test_075(self):
            """Statement"""
            self.assertTrue(TestParser.checkParser("""
                                        func Abs() {
                                            for var k char; fred().e.f(); r := 10 {
                                                return; 
                                            }
                                        };""","successful", 275))

    def test_076(self):
            """Statement"""
            self.assertTrue(TestParser.checkParser("""
                                        func Min() {
                                            for var l int; plugh().g.h(); s := 11 {
                                                return; 
                                            }
                                        };""","successful", 276))

    def test_077(self):
            """Statement"""
            self.assertTrue(TestParser.checkParser("""
                                        func Max() {
                                            for var m float; xyzzy().i.j(); t := 12 {
                                                return; 
                                            }
                                        };""","successful", 277))

    def test_078(self):
            """Statement"""
            self.assertTrue(TestParser.checkParser("""
                                        func Round() {
                                            for var n string; thud().k.l(); u := 13 {
                                                return; 
                                            }
                                        };""","successful", 278))

    def test_079(self):
            """Statement"""
            self.assertTrue(TestParser.checkParser("""
                                        func Floor() {
                                            for var o bool; blar().m.n(); v := 14 {
                                                return; 
                                            }
                                        };""","successful", 279))

    def test_080(self):
            """Statement"""
            self.assertTrue(TestParser.checkParser("""
                                        func Ceil() {
                                            for var p char; baz().o.p(); w := 15 {
                                                return; 
                                            }
                                        };""","successful", 280))

    def test_081(self):
            """Statement"""
            self.assertTrue(TestParser.checkParser("""
                                        func Sin() {
                                            for var q int; foo().q.r(); x := 16 {
                                                return; 
                                            }
                                        };""","successful", 281))

    def test_082(self):
            """Statement"""
            self.assertTrue(TestParser.checkParser("""
                                        func Cos() {
                                            for var r float; bar().s.t(); y := 17 {
                                                return; 
                                            }
                                        };""","successful", 282))

    def test_083(self):
            """Statement"""
            self.assertTrue(TestParser.checkParser("""
                                        func Tan() {
                                            for var s string; baz().u.v(); z := 18 {
                                                return; 
                                            }
                                        };""","successful", 283))

    def test_084(self):
            """Statement"""
            self.assertTrue(TestParser.checkParser("""
                                        func Asin() {
                                            for var t bool; qux().w.x(); aa := 19 {
                                                return; 
                                            }
                                        };""","successful", 284))

    def test_085(self):
            """Statement"""
            self.assertTrue(TestParser.checkParser("""
                                        func Acos() {
                                            for var u char; quux().y.z(); bb := 20 {
                                                return; 
                                            }
                                        };""","successful", 285))

    def test_086(self):
            """Statement"""
            self.assertTrue(TestParser.checkParser("""
                                        func Atan() {
                                            for var v int; corge().a.b(); cc := 21 {
                                                return; 
                                            }
                                        };""","successful", 286))

    def test_087(self):
            """Statement"""
            self.assertTrue(TestParser.checkParser("""
                                        func Sinh() {
                                            for var w float; grault().c.d(); dd := 22 {
                                                return; 
                                            }
                                        };""","successful", 287))

    def test_088(self):
            """Statement"""
            self.assertTrue(TestParser.checkParser("""
                                        func Cosh() {
                                            for var x string; garply().e.f(); ee := 23 {
                                                return; 
                                            }
                                        };""","successful", 288))

    def test_089(self):
            """Statement"""
            self.assertTrue(TestParser.checkParser("""
                                        func Tanh() {
                                            for var y bool; waldo().g.h(); ff := 24 {
                                                return; 
                                            }
                                        };""","successful", 289))

    def test_090(self):
            """Statement"""
            self.assertTrue(TestParser.checkParser("""
                                        func Asinh() {
                                            for var z char; fred().i.j(); gg := 25 {
                                                return; 
                                            }
                                        };""","successful", 290))

    def test_091(self):
            """Statement"""
            self.assertTrue(TestParser.checkParser("""
                                        func Acosh() {
                                            for var aa int; plugh().k.l(); hh := 26 {
                                                return; 
                                            }
                                        };""","successful", 291))

    def test_092(self):
            """Statement"""
            self.assertTrue(TestParser.checkParser("""
                                        func Atanh() {
                                            for var bb float; xyzzy().m.n(); ii := 27 {
                                                return; 
                                            }
                                        };""","successful", 292))

    def test_093(self):
            """Statement"""
            self.assertTrue(TestParser.checkParser("""
                                        func Hypot() {
                                            for var cc string; thud().o.p(); jj := 28 {
                                                return; 
                                            }
                                        };""","successful", 293))

    def test_094(self):
            """Statement"""
            self.assertTrue(TestParser.checkParser("""
                                        func Degrees() {
                                            for var dd bool; blar().q.r(); kk := 29 {
                                                return; 
                                            }
                                        };""","successful", 294))

    def test_095(self):
            """Statement"""
            self.assertTrue(TestParser.checkParser("""
                                        func Radians() {
                                            for var ee char; baz().s.t(); ll := 30 {
                                                return; 
                                            }
                                        };""","successful", 295))

    def test_096(self):
            """Statement"""
            self.assertTrue(TestParser.checkParser("""
                                        func Exp2() {
                                            for var ff int; foo().u.v(); mm := 31 {
                                                return; 
                                            }
                                        };""","successful", 296))

    def test_097(self):
            """Statement"""
            self.assertTrue(TestParser.checkParser("""
                                        func Expm1() {
                                            for var gg float; bar().w.x(); nn := 32 {
                                                return; 
                                            }
                                        };""","successful", 297))

    def test_098(self):
            """Statement"""
            self.assertTrue(TestParser.checkParser("""
                                        func Log10() {
                                            for var hh string; baz().y.z(); oo := 33 {
                                                return; 
                                            }
                                        };""","successful", 298))

    def test_099(self):
            """Statement"""
            self.assertTrue(TestParser.checkParser("""
                                        func Log2() {
                                            for var ii bool; qux().a.b(); pp := 34 {
                                                return; 
                                            }
                                        };""","successful", 299))

    def test_100(self):
            """Statement"""
            self.assertTrue(TestParser.checkParser("""
                                        func Log1p() {
                                            for var jj string; quux().c.d(); qq := 35 {
                                                return; 
                                            }
                                        };""","successful", 300))

        


# --------------------------------------------------------------------------------------------------------------
################################################################################################################
###################################################################################################################
####################################################################################################################
###################################################################################################################
