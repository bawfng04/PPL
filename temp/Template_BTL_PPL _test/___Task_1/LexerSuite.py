"""
 * Initial code for Assignment
 * Programming Language Principles
 * Author: Võ Tiến
 * Link FB : https://www.facebook.com/Shiba.Vo.Tien
 * Link Group : https://www.facebook.com/groups/khmt.ktmt.cse.bku
 * Date: 02.01.2025
"""
import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

#1. Mô tả chuỗi có độ dài lẻ
    def test_1(self):
        """test """
        self.assertTrue(TestLexer.test("aaa*%","aaa*%,<EOF>",101))
    def test_2(self):
        """test """
        self.assertTrue(TestLexer.test("ba aa","ba aa,<EOF>",102))
    def test_3(self):
        """test """
        self.assertTrue(TestLexer.test("ba","Error Token ba",103))
    def test_4(self):
        """test """
        self.assertTrue(TestLexer.test("","Error Token ",104))
    def test_5(self):
        """test """
        self.assertTrue(TestLexer.test("a","a,<EOF>",105))


#2. Mô tả số thực trong C++.

    # def test_1(self):
    #     """test valid floating-point number"""
    #     self.assertTrue(TestLexer.test("3.14", "3.14,<EOF>", 101))

    # def test_2(self):
    #     """test valid floating-point number with no leading digit"""
    #     self.assertTrue(TestLexer.test(".5", ".5,<EOF>", 102))

    # def test_3(self):
    #     """test valid floating-point number in scientific notation"""
    #     self.assertTrue(TestLexer.test("1.23e-4", "1.23e-4,<EOF>", 103))

    # def test_4(self):
    #     """test valid floating-point number with positive exponent"""
    #     self.assertTrue(TestLexer.test("4.56E+10", "4.56E+10,<EOF>", 104))

    # def test_5(self):
    #     """test invalid floating-point number with missing exponent"""
    #     self.assertTrue(TestLexer.test("3.14e", "Error Token 3.14e", 105))

    # def test_6(self):
    #     """test invalid floating-point number with multiple dots"""
    #     self.assertTrue(TestLexer.test("3.14.5", "Error Token 3.14.5", 106))

    # def test_7(self):
    #     """test valid floating-point number with negative sign"""
    #     self.assertTrue(TestLexer.test("-3.14", "-3.14,<EOF>", 107))

    # def test_9(self):
    #     """test invalid floating-point number with letters"""
    #     self.assertTrue(TestLexer.test("3.14abc", "Error Token 3.14abc", 109))

    # def test_10(self):
    #     """test floating-point number with no fractional part"""
    #     self.assertTrue(TestLexer.test("5.", "5.0,<EOF>", 110))

    # def test_11(self):
    #     """test valid scientific notation without fractional part"""
    #     self.assertTrue(TestLexer.test("1e10", "1e10,<EOF>", 111))

    # def test_12(self):
    #     """test invalid number starting with dot"""
    #     self.assertTrue(TestLexer.test(".e5", "Error Token .e5", 112))

    # def test_13(self):
    #     """test valid long double literal"""
    #     self.assertTrue(TestLexer.test("1.23l", "1.23l,<EOF>", 113))

    # def test_14(self):
    #     """test invalid exponent without base"""
    #     self.assertTrue(TestLexer.test("e5", "Error Token e5", 114))

    # def test_15(self):
    #     """test valid negative floating-point number in scientific notation"""
    #     self.assertTrue(TestLexer.test("-7.89e+2", "-7.89e+2,<EOF>", 115))

# 3. Mô tả chuỗi có nhiều nhất 4 chữ 'a'

    # def test_1(self):
    #     """Test chuỗi có 3 chữ 'a'"""
    #     self.assertTrue(TestLexer.test("aaa", "aaa,<EOF>", 101))

    # def test_2(self):
    #     """Test chuỗi có 1 chữ 'a'"""
    #     self.assertTrue(TestLexer.test("a", "a,<EOF>", 102))

    # def test_3(self):
    #     """Test chuỗi có 4 chữ 'a'"""
    #     self.assertTrue(TestLexer.test("aaaa", "aaaa,<EOF>", 103))

    # def test_4(self):
    #     """Test chuỗi không chứa chữ 'a'"""
    #     self.assertTrue(TestLexer.test("bcdef", "bcdef,<EOF>", 104))

    # def test_5(self):
    #     """Test chuỗi có 5 chữ 'a' (lỗi)"""
    #     self.assertTrue(TestLexer.test("aaaaa", "Error Token aaaaa", 105))

    # def test_6(self):
    #     """Test chuỗi có nhiều ký tự khác nhau nhưng không quá 4 chữ 'a'"""
    #     self.assertTrue(TestLexer.test("abca", "abca,<EOF>", 106))

    # def test_7(self):
    #     """Test chuỗi có 0 chữ 'a'"""
    #     self.assertTrue(TestLexer.test("bc", "bc,<EOF>", 107))

    # def test_8(self):
    #     """Test chuỗi có chữ 'a' nhưng không vượt quá số lần quy định"""
    #     self.assertTrue(TestLexer.test("a b c a", "a b c a,<EOF>", 108))

    # def test_9(self):
    #     """Test chuỗi có 5 chữ 'a' nhưng đã bị từ chối"""
    #     self.assertTrue(TestLexer.test("aaaaab", "Error Token aaaaab", 109))

# 4. Mô tả chuỗi có ít nhất 4 chữ 'a'

    # def test_1(self):
    #     """Test chuỗi có ít nhất 4 chữ 'a'"""
    #     self.assertTrue(TestLexer.test("aaxaa", "aaxaa,<EOF>", 101))

    # def test_2(self):
    #     """Test chuỗi có đúng 4 chữ 'a'"""
    #     self.assertTrue(TestLexer.test("aaaab", "aaaab,<EOF>", 102))

    # def test_3(self):
    #     """Test chuỗi có 5 chữ 'a'"""
    #     self.assertTrue(TestLexer.test("aaaaa", "aaaaa,<EOF>", 103))

    # def test_4(self):
    #     """Test chuỗi có 6 chữ 'a'"""
    #     self.assertTrue(TestLexer.test("aaaaaa", "aaaaaa,<EOF>", 104))

    # def test_5(self):
    #     """Test chuỗi có ít hơn 4 chữ 'a' (lỗi)"""
    #     self.assertTrue(TestLexer.test("aa", "Error Token aa", 105))

    # def test_6(self):
    #     """Test chuỗi có 3 chữ 'a' (lỗi)"""
    #     self.assertTrue(TestLexer.test("aaa", "Error Token aaa", 106))

    # def test_7(self):
    #     """Test chuỗi có ít hơn 4 chữ 'a' (lỗi)"""
    #     self.assertTrue(TestLexer.test("a b c", "Error Token a b c", 107))

# 5. Mô tả chuỗi mà a và b không kề nhau

    # def test_1(self):
    #     """Test chuỗi không có 'a' và 'b' kề nhau"""
    #     self.assertTrue(TestLexer.test("a", "a,<EOF>", 101))

    # def test_2(self):
    #     """Test chuỗi có 'a' và 'b' không kề nhau"""
    #     self.assertTrue(TestLexer.test("acb", "acb,<EOF>", 102))

    # def test_3(self):
    #     """Test chuỗi có nhiều ký tự khác, 'a' và 'b' không kề nhau"""
    #     self.assertTrue(TestLexer.test("axbxaxbxaxb", "axbxaxbxaxb,<EOF>", 103))

    # def test_4(self):
    #     """Test chuỗi có 'a' và 'b' kề nhau (lỗi)"""
    #     self.assertTrue(TestLexer.test("ab", "Error Token ab", 104))

    # def test_5(self):
    #     """Test chuỗi có 'a' và 'b' kề nhau (lỗi)"""
    #     self.assertTrue(TestLexer.test("ba", "Error Token ba", 105))

    # def test_6(self):
    #     """Test chuỗi có 'a' và 'b' kề nhau (lỗi)"""
    #     self.assertTrue(TestLexer.test("aabb", "Error Token aabb", 106))

    # def test_7(self):
    #     """Test chuỗi với ký tự không phải 'a' và 'b'"""
    #     self.assertTrue(TestLexer.test("123456", "123456,<EOF>", 107))

    # def test_8(self):
    #     """Test chuỗi có khoảng trắng giữa các ký tự"""
    #     self.assertTrue(TestLexer.test("a b c", "a b c,<EOF>", 108))

    # def test_9(self):
    #     """Test chuỗi có 'a' và 'b' không kề nhau"""
    #     self.assertTrue(TestLexer.test("a b", "a b,<EOF>", 109))