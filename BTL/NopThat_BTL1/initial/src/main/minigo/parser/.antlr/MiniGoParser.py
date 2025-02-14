# Generated from d:/Projects/PPL-Assignment/BTL/NopThat_BTL1/initial/src/main/minigo/parser/MiniGo.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,63,827,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,58,2,59,
        7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,65,7,65,
        2,66,7,66,2,67,7,67,2,68,7,68,2,69,7,69,2,70,7,70,2,71,7,71,2,72,
        7,72,2,73,7,73,2,74,7,74,2,75,7,75,2,76,7,76,2,77,7,77,2,78,7,78,
        2,79,7,79,2,80,7,80,2,81,7,81,2,82,7,82,2,83,7,83,1,0,1,0,1,0,1,
        0,1,0,1,0,1,1,1,1,1,1,3,1,178,8,1,1,2,1,2,1,2,1,2,1,2,3,2,185,8,
        2,1,3,1,3,1,3,1,3,1,3,1,3,3,3,193,8,3,1,3,1,3,1,4,1,4,1,4,1,4,1,
        4,3,4,202,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,212,8,5,1,6,1,
        6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,3,7,223,8,7,1,8,1,8,1,8,1,8,3,8,229,
        8,8,1,8,1,8,1,8,1,8,1,8,3,8,236,8,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,3,8,246,8,8,1,9,1,9,1,9,1,9,3,9,252,8,9,1,10,1,10,1,10,1,10,
        3,10,258,8,10,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,3,12,
        269,8,12,1,13,1,13,1,13,1,13,1,14,1,14,3,14,277,8,14,1,14,1,14,1,
        14,3,14,282,8,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,3,15,292,
        8,15,1,16,1,16,1,16,1,16,3,16,298,8,16,1,16,1,16,3,16,302,8,16,1,
        16,3,16,305,8,16,1,16,1,16,3,16,309,8,16,1,17,1,17,1,17,1,17,1,17,
        1,17,3,17,317,8,17,1,18,1,18,1,18,1,18,1,18,3,18,324,8,18,1,19,1,
        19,1,19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,3,20,336,8,20,1,20,1,
        20,3,20,340,8,20,1,20,3,20,343,8,20,1,20,1,20,1,20,1,21,1,21,1,21,
        1,21,1,21,3,21,353,8,21,1,22,1,22,1,22,1,23,1,23,1,23,1,23,1,23,
        1,23,1,23,1,23,1,23,1,23,1,23,3,23,369,8,23,1,24,1,24,1,24,1,24,
        1,24,1,24,3,24,377,8,24,1,25,1,25,1,25,1,25,1,25,3,25,384,8,25,1,
        26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,27,1,27,1,27,1,
        27,1,28,1,28,1,28,1,28,1,28,3,28,405,8,28,1,29,1,29,1,29,3,29,410,
        8,29,1,30,1,30,1,30,1,30,1,30,3,30,417,8,30,1,30,3,30,420,8,30,1,
        31,1,31,1,31,1,31,3,31,426,8,31,1,32,1,32,1,32,1,32,3,32,432,8,32,
        1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,34,1,34,1,34,
        1,35,1,35,1,35,1,35,3,35,451,8,35,1,36,1,36,1,36,1,36,3,36,457,8,
        36,1,37,1,37,1,37,3,37,462,8,37,1,37,1,37,3,37,466,8,37,1,37,1,37,
        1,37,1,37,3,37,472,8,37,1,37,1,37,3,37,476,8,37,1,37,3,37,479,8,
        37,1,38,1,38,3,38,483,8,38,1,39,1,39,3,39,487,8,39,1,40,1,40,3,40,
        491,8,40,1,41,1,41,3,41,495,8,41,1,42,1,42,1,42,1,42,3,42,501,8,
        42,1,43,1,43,1,44,1,44,1,44,1,45,1,45,1,45,3,45,511,8,45,1,45,1,
        45,3,45,515,8,45,1,46,1,46,1,46,1,46,1,46,1,46,1,46,1,46,1,46,3,
        46,526,8,46,1,47,1,47,1,47,1,47,1,47,1,47,1,47,1,47,1,47,1,47,1,
        47,1,47,1,47,1,47,1,47,1,47,1,47,1,47,1,47,3,47,547,8,47,1,48,1,
        48,1,48,1,48,1,48,1,48,1,48,1,48,1,48,1,48,3,48,559,8,48,1,48,1,
        48,3,48,563,8,48,1,49,1,49,1,49,1,49,1,50,1,50,1,50,1,51,1,51,1,
        51,1,52,1,52,3,52,577,8,52,1,52,1,52,3,52,581,8,52,1,52,3,52,584,
        8,52,1,53,1,53,3,53,588,8,53,1,53,1,53,3,53,592,8,53,1,53,1,53,3,
        53,596,8,53,1,54,1,54,3,54,600,8,54,1,54,1,54,3,54,604,8,54,1,54,
        1,54,1,55,1,55,1,55,1,55,1,55,1,55,3,55,614,8,55,1,56,1,56,1,56,
        1,56,1,56,3,56,621,8,56,1,57,1,57,1,57,1,57,1,57,1,57,5,57,629,8,
        57,10,57,12,57,632,9,57,1,58,1,58,1,58,1,58,1,58,1,58,5,58,640,8,
        58,10,58,12,58,643,9,58,1,59,1,59,1,59,1,59,1,59,1,59,5,59,651,8,
        59,10,59,12,59,654,9,59,1,60,1,60,1,60,1,60,1,60,1,60,5,60,662,8,
        60,10,60,12,60,665,9,60,1,61,1,61,1,61,1,61,1,61,1,61,5,61,673,8,
        61,10,61,12,61,676,9,61,1,62,1,62,1,62,1,62,1,62,1,62,5,62,684,8,
        62,10,62,12,62,687,9,62,1,63,1,63,1,63,1,63,1,63,3,63,694,8,63,1,
        64,1,64,1,64,1,65,1,65,1,65,1,65,3,65,703,8,65,1,65,1,65,3,65,707,
        8,65,1,66,1,66,1,66,1,66,1,66,1,66,3,66,715,8,66,1,67,1,67,1,67,
        1,67,1,68,1,68,1,68,1,69,1,69,3,69,726,8,69,1,69,1,69,1,70,1,70,
        1,70,1,70,1,70,1,70,1,70,1,70,1,70,3,70,739,8,70,1,71,1,71,1,71,
        1,71,1,71,1,72,1,72,1,72,1,72,1,73,1,73,1,73,1,73,1,73,1,73,1,73,
        1,73,1,73,3,73,759,8,73,1,74,1,74,1,74,1,74,1,74,3,74,766,8,74,1,
        75,1,75,1,75,1,75,1,75,1,75,1,75,1,75,1,75,3,75,777,8,75,1,76,1,
        76,1,76,1,76,1,76,1,76,1,77,1,77,1,77,1,77,1,77,3,77,790,8,77,1,
        78,1,78,1,78,1,78,1,78,1,78,3,78,798,8,78,1,79,1,79,1,79,1,79,1,
        79,1,80,1,80,3,80,807,8,80,1,81,1,81,1,81,1,81,1,81,3,81,814,8,81,
        1,82,1,82,1,82,1,82,1,83,1,83,1,83,1,83,1,83,3,83,825,8,83,1,83,
        0,6,114,116,118,120,122,124,84,0,2,4,6,8,10,12,14,16,18,20,22,24,
        26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,
        70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100,102,104,106,108,
        110,112,114,116,118,120,122,124,126,128,130,132,134,136,138,140,
        142,144,146,148,150,152,154,156,158,160,162,164,166,0,8,2,0,52,52,
        57,57,2,0,7,8,53,53,2,0,35,40,43,43,2,0,44,44,53,53,1,0,26,27,1,
        0,28,31,1,0,21,22,1,0,23,25,864,0,168,1,0,0,0,2,177,1,0,0,0,4,184,
        1,0,0,0,6,192,1,0,0,0,8,201,1,0,0,0,10,211,1,0,0,0,12,213,1,0,0,
        0,14,222,1,0,0,0,16,245,1,0,0,0,18,251,1,0,0,0,20,257,1,0,0,0,22,
        259,1,0,0,0,24,268,1,0,0,0,26,270,1,0,0,0,28,274,1,0,0,0,30,291,
        1,0,0,0,32,293,1,0,0,0,34,316,1,0,0,0,36,323,1,0,0,0,38,325,1,0,
        0,0,40,328,1,0,0,0,42,352,1,0,0,0,44,354,1,0,0,0,46,368,1,0,0,0,
        48,376,1,0,0,0,50,383,1,0,0,0,52,385,1,0,0,0,54,395,1,0,0,0,56,404,
        1,0,0,0,58,409,1,0,0,0,60,411,1,0,0,0,62,425,1,0,0,0,64,431,1,0,
        0,0,66,433,1,0,0,0,68,443,1,0,0,0,70,450,1,0,0,0,72,456,1,0,0,0,
        74,478,1,0,0,0,76,482,1,0,0,0,78,486,1,0,0,0,80,490,1,0,0,0,82,494,
        1,0,0,0,84,496,1,0,0,0,86,502,1,0,0,0,88,504,1,0,0,0,90,514,1,0,
        0,0,92,516,1,0,0,0,94,527,1,0,0,0,96,562,1,0,0,0,98,564,1,0,0,0,
        100,568,1,0,0,0,102,571,1,0,0,0,104,574,1,0,0,0,106,587,1,0,0,0,
        108,597,1,0,0,0,110,613,1,0,0,0,112,620,1,0,0,0,114,622,1,0,0,0,
        116,633,1,0,0,0,118,644,1,0,0,0,120,655,1,0,0,0,122,666,1,0,0,0,
        124,677,1,0,0,0,126,693,1,0,0,0,128,695,1,0,0,0,130,706,1,0,0,0,
        132,714,1,0,0,0,134,716,1,0,0,0,136,720,1,0,0,0,138,723,1,0,0,0,
        140,738,1,0,0,0,142,740,1,0,0,0,144,745,1,0,0,0,146,758,1,0,0,0,
        148,765,1,0,0,0,150,776,1,0,0,0,152,778,1,0,0,0,154,789,1,0,0,0,
        156,797,1,0,0,0,158,799,1,0,0,0,160,806,1,0,0,0,162,813,1,0,0,0,
        164,815,1,0,0,0,166,824,1,0,0,0,168,169,3,2,1,0,169,170,3,6,3,0,
        170,171,3,4,2,0,171,172,3,2,1,0,172,173,5,0,0,1,173,1,1,0,0,0,174,
        178,1,0,0,0,175,176,5,57,0,0,176,178,3,2,1,0,177,174,1,0,0,0,177,
        175,1,0,0,0,178,3,1,0,0,0,179,185,1,0,0,0,180,181,3,2,1,0,181,182,
        3,6,3,0,182,183,3,4,2,0,183,185,1,0,0,0,184,179,1,0,0,0,184,180,
        1,0,0,0,185,5,1,0,0,0,186,193,3,12,6,0,187,193,3,22,11,0,188,193,
        3,32,16,0,189,193,3,40,20,0,190,193,3,52,26,0,191,193,3,66,33,0,
        192,186,1,0,0,0,192,187,1,0,0,0,192,188,1,0,0,0,192,189,1,0,0,0,
        192,190,1,0,0,0,192,191,1,0,0,0,193,194,1,0,0,0,194,195,3,2,1,0,
        195,7,1,0,0,0,196,202,3,10,5,0,197,198,3,10,5,0,198,199,3,2,1,0,
        199,200,3,8,4,0,200,202,1,0,0,0,201,196,1,0,0,0,201,197,1,0,0,0,
        202,9,1,0,0,0,203,212,3,82,41,0,204,212,3,84,42,0,205,212,3,92,46,
        0,206,212,3,94,47,0,207,212,3,100,50,0,208,212,3,102,51,0,209,212,
        3,106,53,0,210,212,3,104,52,0,211,203,1,0,0,0,211,204,1,0,0,0,211,
        205,1,0,0,0,211,206,1,0,0,0,211,207,1,0,0,0,211,208,1,0,0,0,211,
        209,1,0,0,0,211,210,1,0,0,0,212,11,1,0,0,0,213,214,5,14,0,0,214,
        215,3,14,7,0,215,216,7,0,0,0,216,13,1,0,0,0,217,223,3,16,8,0,218,
        219,3,16,8,0,219,220,5,51,0,0,220,221,3,14,7,0,221,223,1,0,0,0,222,
        217,1,0,0,0,222,218,1,0,0,0,223,15,1,0,0,0,224,225,5,53,0,0,225,
        228,3,156,78,0,226,227,5,35,0,0,227,229,3,114,57,0,228,226,1,0,0,
        0,228,229,1,0,0,0,229,246,1,0,0,0,230,231,5,53,0,0,231,232,3,18,
        9,0,232,235,3,156,78,0,233,234,5,35,0,0,234,236,3,112,56,0,235,233,
        1,0,0,0,235,236,1,0,0,0,236,246,1,0,0,0,237,238,5,53,0,0,238,239,
        5,35,0,0,239,246,3,114,57,0,240,241,5,53,0,0,241,242,3,20,10,0,242,
        243,5,35,0,0,243,244,3,112,56,0,244,246,1,0,0,0,245,224,1,0,0,0,
        245,230,1,0,0,0,245,237,1,0,0,0,245,240,1,0,0,0,246,17,1,0,0,0,247,
        252,1,0,0,0,248,249,5,51,0,0,249,250,5,53,0,0,250,252,3,18,9,0,251,
        247,1,0,0,0,251,248,1,0,0,0,252,19,1,0,0,0,253,258,1,0,0,0,254,255,
        5,51,0,0,255,256,5,53,0,0,256,258,3,20,10,0,257,253,1,0,0,0,257,
        254,1,0,0,0,258,21,1,0,0,0,259,260,5,13,0,0,260,261,3,24,12,0,261,
        262,7,0,0,0,262,23,1,0,0,0,263,269,3,26,13,0,264,265,3,26,13,0,265,
        266,5,51,0,0,266,267,3,24,12,0,267,269,1,0,0,0,268,263,1,0,0,0,268,
        264,1,0,0,0,269,25,1,0,0,0,270,271,5,53,0,0,271,272,5,35,0,0,272,
        273,3,114,57,0,273,27,1,0,0,0,274,276,5,47,0,0,275,277,5,57,0,0,
        276,275,1,0,0,0,276,277,1,0,0,0,277,278,1,0,0,0,278,279,3,10,5,0,
        279,281,3,30,15,0,280,282,5,57,0,0,281,280,1,0,0,0,281,282,1,0,0,
        0,282,283,1,0,0,0,283,284,5,48,0,0,284,29,1,0,0,0,285,292,1,0,0,
        0,286,287,3,10,5,0,287,288,3,30,15,0,288,292,1,0,0,0,289,290,5,57,
        0,0,290,292,3,30,15,0,291,285,1,0,0,0,291,286,1,0,0,0,291,289,1,
        0,0,0,292,31,1,0,0,0,293,294,5,5,0,0,294,295,5,53,0,0,295,297,5,
        45,0,0,296,298,3,46,23,0,297,296,1,0,0,0,297,298,1,0,0,0,298,299,
        1,0,0,0,299,301,5,46,0,0,300,302,3,34,17,0,301,300,1,0,0,0,301,302,
        1,0,0,0,302,304,1,0,0,0,303,305,5,57,0,0,304,303,1,0,0,0,304,305,
        1,0,0,0,305,306,1,0,0,0,306,308,3,28,14,0,307,309,5,52,0,0,308,307,
        1,0,0,0,308,309,1,0,0,0,309,33,1,0,0,0,310,311,5,45,0,0,311,312,
        3,156,78,0,312,313,3,36,18,0,313,314,5,46,0,0,314,317,1,0,0,0,315,
        317,3,156,78,0,316,310,1,0,0,0,316,315,1,0,0,0,317,35,1,0,0,0,318,
        324,1,0,0,0,319,320,5,51,0,0,320,321,3,156,78,0,321,322,3,36,18,
        0,322,324,1,0,0,0,323,318,1,0,0,0,323,319,1,0,0,0,324,37,1,0,0,0,
        325,326,5,53,0,0,326,327,7,1,0,0,327,39,1,0,0,0,328,329,5,5,0,0,
        329,330,5,45,0,0,330,331,3,38,19,0,331,332,5,46,0,0,332,333,5,53,
        0,0,333,335,5,45,0,0,334,336,3,46,23,0,335,334,1,0,0,0,335,336,1,
        0,0,0,336,337,1,0,0,0,337,339,5,46,0,0,338,340,3,156,78,0,339,338,
        1,0,0,0,339,340,1,0,0,0,340,342,1,0,0,0,341,343,5,57,0,0,342,341,
        1,0,0,0,342,343,1,0,0,0,343,344,1,0,0,0,344,345,3,108,54,0,345,346,
        7,0,0,0,346,41,1,0,0,0,347,353,3,44,22,0,348,349,3,44,22,0,349,350,
        5,51,0,0,350,351,3,42,21,0,351,353,1,0,0,0,352,347,1,0,0,0,352,348,
        1,0,0,0,353,43,1,0,0,0,354,355,5,53,0,0,355,356,3,156,78,0,356,45,
        1,0,0,0,357,358,5,53,0,0,358,369,3,156,78,0,359,360,5,53,0,0,360,
        361,3,20,10,0,361,362,3,156,78,0,362,369,1,0,0,0,363,369,3,48,24,
        0,364,365,3,48,24,0,365,366,5,51,0,0,366,367,3,46,23,0,367,369,1,
        0,0,0,368,357,1,0,0,0,368,359,1,0,0,0,368,363,1,0,0,0,368,364,1,
        0,0,0,369,47,1,0,0,0,370,371,5,53,0,0,371,377,3,156,78,0,372,373,
        5,53,0,0,373,374,3,50,25,0,374,375,3,156,78,0,375,377,1,0,0,0,376,
        370,1,0,0,0,376,372,1,0,0,0,377,49,1,0,0,0,378,379,5,51,0,0,379,
        384,5,53,0,0,380,381,5,51,0,0,381,382,5,53,0,0,382,384,3,50,25,0,
        383,378,1,0,0,0,383,380,1,0,0,0,384,51,1,0,0,0,385,386,5,6,0,0,386,
        387,5,53,0,0,387,388,5,7,0,0,388,389,5,47,0,0,389,390,3,58,29,0,
        390,391,3,54,27,0,391,392,3,58,29,0,392,393,5,48,0,0,393,394,7,0,
        0,0,394,53,1,0,0,0,395,396,3,60,30,0,396,397,3,58,29,0,397,398,3,
        56,28,0,398,55,1,0,0,0,399,405,1,0,0,0,400,401,3,60,30,0,401,402,
        3,58,29,0,402,403,3,56,28,0,403,405,1,0,0,0,404,399,1,0,0,0,404,
        400,1,0,0,0,405,57,1,0,0,0,406,410,1,0,0,0,407,408,5,57,0,0,408,
        410,3,58,29,0,409,406,1,0,0,0,409,407,1,0,0,0,410,59,1,0,0,0,411,
        412,5,53,0,0,412,413,3,62,31,0,413,419,3,156,78,0,414,420,5,52,0,
        0,415,417,5,52,0,0,416,415,1,0,0,0,416,417,1,0,0,0,417,418,1,0,0,
        0,418,420,5,57,0,0,419,414,1,0,0,0,419,416,1,0,0,0,420,61,1,0,0,
        0,421,426,1,0,0,0,422,423,5,51,0,0,423,424,5,53,0,0,424,426,3,62,
        31,0,425,421,1,0,0,0,425,422,1,0,0,0,426,63,1,0,0,0,427,432,1,0,
        0,0,428,429,3,60,30,0,429,430,3,64,32,0,430,432,1,0,0,0,431,427,
        1,0,0,0,431,428,1,0,0,0,432,65,1,0,0,0,433,434,5,6,0,0,434,435,5,
        53,0,0,435,436,5,8,0,0,436,437,5,47,0,0,437,438,3,58,29,0,438,439,
        3,68,34,0,439,440,3,58,29,0,440,441,5,48,0,0,441,442,7,0,0,0,442,
        67,1,0,0,0,443,444,3,74,37,0,444,445,3,70,35,0,445,69,1,0,0,0,446,
        451,1,0,0,0,447,448,3,74,37,0,448,449,3,70,35,0,449,451,1,0,0,0,
        450,446,1,0,0,0,450,447,1,0,0,0,451,71,1,0,0,0,452,457,1,0,0,0,453,
        454,3,74,37,0,454,455,3,72,36,0,455,457,1,0,0,0,456,452,1,0,0,0,
        456,453,1,0,0,0,457,73,1,0,0,0,458,459,5,53,0,0,459,461,5,45,0,0,
        460,462,3,46,23,0,461,460,1,0,0,0,461,462,1,0,0,0,462,463,1,0,0,
        0,463,465,5,46,0,0,464,466,3,156,78,0,465,464,1,0,0,0,465,466,1,
        0,0,0,466,467,1,0,0,0,467,479,7,0,0,0,468,469,5,53,0,0,469,471,5,
        45,0,0,470,472,3,46,23,0,471,470,1,0,0,0,471,472,1,0,0,0,472,473,
        1,0,0,0,473,475,5,46,0,0,474,476,3,156,78,0,475,474,1,0,0,0,475,
        476,1,0,0,0,476,477,1,0,0,0,477,479,7,0,0,0,478,458,1,0,0,0,478,
        468,1,0,0,0,479,75,1,0,0,0,480,483,1,0,0,0,481,483,3,46,23,0,482,
        480,1,0,0,0,482,481,1,0,0,0,483,77,1,0,0,0,484,487,1,0,0,0,485,487,
        3,156,78,0,486,484,1,0,0,0,486,485,1,0,0,0,487,79,1,0,0,0,488,491,
        1,0,0,0,489,491,5,52,0,0,490,488,1,0,0,0,490,489,1,0,0,0,491,81,
        1,0,0,0,492,495,3,12,6,0,493,495,3,22,11,0,494,492,1,0,0,0,494,493,
        1,0,0,0,495,83,1,0,0,0,496,497,3,88,44,0,497,498,3,86,43,0,498,500,
        3,114,57,0,499,501,5,52,0,0,500,499,1,0,0,0,500,501,1,0,0,0,501,
        85,1,0,0,0,502,503,7,2,0,0,503,87,1,0,0,0,504,505,5,53,0,0,505,506,
        3,90,45,0,506,89,1,0,0,0,507,515,1,0,0,0,508,511,3,136,68,0,509,
        511,3,134,67,0,510,508,1,0,0,0,510,509,1,0,0,0,511,512,1,0,0,0,512,
        513,3,90,45,0,513,515,1,0,0,0,514,507,1,0,0,0,514,510,1,0,0,0,515,
        91,1,0,0,0,516,517,5,1,0,0,517,518,5,45,0,0,518,519,3,114,57,0,519,
        520,5,46,0,0,520,525,3,28,14,0,521,522,5,2,0,0,522,526,3,92,46,0,
        523,524,5,2,0,0,524,526,3,28,14,0,525,521,1,0,0,0,525,523,1,0,0,
        0,525,526,1,0,0,0,526,93,1,0,0,0,527,546,5,3,0,0,528,529,7,3,0,0,
        529,530,5,51,0,0,530,531,7,3,0,0,531,532,5,43,0,0,532,533,5,17,0,
        0,533,534,3,114,57,0,534,535,3,28,14,0,535,547,1,0,0,0,536,537,3,
        96,48,0,537,538,7,0,0,0,538,539,3,114,57,0,539,540,7,0,0,0,540,541,
        3,98,49,0,541,542,3,28,14,0,542,547,1,0,0,0,543,544,3,114,57,0,544,
        545,3,28,14,0,545,547,1,0,0,0,546,528,1,0,0,0,546,536,1,0,0,0,546,
        543,1,0,0,0,547,95,1,0,0,0,548,549,5,53,0,0,549,550,5,43,0,0,550,
        563,3,114,57,0,551,552,5,53,0,0,552,553,3,86,43,0,553,554,3,114,
        57,0,554,563,1,0,0,0,555,556,5,14,0,0,556,558,5,53,0,0,557,559,3,
        156,78,0,558,557,1,0,0,0,558,559,1,0,0,0,559,560,1,0,0,0,560,561,
        5,35,0,0,561,563,3,114,57,0,562,548,1,0,0,0,562,551,1,0,0,0,562,
        555,1,0,0,0,563,97,1,0,0,0,564,565,5,53,0,0,565,566,3,86,43,0,566,
        567,3,114,57,0,567,99,1,0,0,0,568,569,5,16,0,0,569,570,7,0,0,0,570,
        101,1,0,0,0,571,572,5,15,0,0,572,573,7,0,0,0,573,103,1,0,0,0,574,
        583,5,4,0,0,575,577,3,114,57,0,576,575,1,0,0,0,576,577,1,0,0,0,577,
        578,1,0,0,0,578,584,5,52,0,0,579,581,3,114,57,0,580,579,1,0,0,0,
        580,581,1,0,0,0,581,582,1,0,0,0,582,584,5,57,0,0,583,576,1,0,0,0,
        583,580,1,0,0,0,584,105,1,0,0,0,585,588,5,53,0,0,586,588,3,88,44,
        0,587,585,1,0,0,0,587,586,1,0,0,0,588,589,1,0,0,0,589,591,5,45,0,
        0,590,592,3,166,83,0,591,590,1,0,0,0,591,592,1,0,0,0,592,593,1,0,
        0,0,593,595,5,46,0,0,594,596,5,52,0,0,595,594,1,0,0,0,595,596,1,
        0,0,0,596,107,1,0,0,0,597,599,5,47,0,0,598,600,5,57,0,0,599,598,
        1,0,0,0,599,600,1,0,0,0,600,601,1,0,0,0,601,603,3,110,55,0,602,604,
        5,57,0,0,603,602,1,0,0,0,603,604,1,0,0,0,604,605,1,0,0,0,605,606,
        5,48,0,0,606,109,1,0,0,0,607,614,1,0,0,0,608,609,3,10,5,0,609,610,
        3,110,55,0,610,614,1,0,0,0,611,612,5,57,0,0,612,614,3,110,55,0,613,
        607,1,0,0,0,613,608,1,0,0,0,613,611,1,0,0,0,614,111,1,0,0,0,615,
        621,3,114,57,0,616,617,3,114,57,0,617,618,5,51,0,0,618,619,3,112,
        56,0,619,621,1,0,0,0,620,615,1,0,0,0,620,616,1,0,0,0,621,113,1,0,
        0,0,622,623,6,57,-1,0,623,624,3,116,58,0,624,630,1,0,0,0,625,626,
        10,2,0,0,626,627,5,33,0,0,627,629,3,116,58,0,628,625,1,0,0,0,629,
        632,1,0,0,0,630,628,1,0,0,0,630,631,1,0,0,0,631,115,1,0,0,0,632,
        630,1,0,0,0,633,634,6,58,-1,0,634,635,3,118,59,0,635,641,1,0,0,0,
        636,637,10,2,0,0,637,638,5,32,0,0,638,640,3,118,59,0,639,636,1,0,
        0,0,640,643,1,0,0,0,641,639,1,0,0,0,641,642,1,0,0,0,642,117,1,0,
        0,0,643,641,1,0,0,0,644,645,6,59,-1,0,645,646,3,120,60,0,646,652,
        1,0,0,0,647,648,10,2,0,0,648,649,7,4,0,0,649,651,3,120,60,0,650,
        647,1,0,0,0,651,654,1,0,0,0,652,650,1,0,0,0,652,653,1,0,0,0,653,
        119,1,0,0,0,654,652,1,0,0,0,655,656,6,60,-1,0,656,657,3,122,61,0,
        657,663,1,0,0,0,658,659,10,2,0,0,659,660,7,5,0,0,660,662,3,122,61,
        0,661,658,1,0,0,0,662,665,1,0,0,0,663,661,1,0,0,0,663,664,1,0,0,
        0,664,121,1,0,0,0,665,663,1,0,0,0,666,667,6,61,-1,0,667,668,3,124,
        62,0,668,674,1,0,0,0,669,670,10,2,0,0,670,671,7,6,0,0,671,673,3,
        124,62,0,672,669,1,0,0,0,673,676,1,0,0,0,674,672,1,0,0,0,674,675,
        1,0,0,0,675,123,1,0,0,0,676,674,1,0,0,0,677,678,6,62,-1,0,678,679,
        3,126,63,0,679,685,1,0,0,0,680,681,10,2,0,0,681,682,7,7,0,0,682,
        684,3,126,63,0,683,680,1,0,0,0,684,687,1,0,0,0,685,683,1,0,0,0,685,
        686,1,0,0,0,686,125,1,0,0,0,687,685,1,0,0,0,688,689,5,34,0,0,689,
        694,3,126,63,0,690,691,5,22,0,0,691,694,3,126,63,0,692,694,3,128,
        64,0,693,688,1,0,0,0,693,690,1,0,0,0,693,692,1,0,0,0,694,127,1,0,
        0,0,695,696,3,132,66,0,696,697,3,130,65,0,697,129,1,0,0,0,698,707,
        1,0,0,0,699,703,3,134,67,0,700,703,3,136,68,0,701,703,3,138,69,0,
        702,699,1,0,0,0,702,700,1,0,0,0,702,701,1,0,0,0,703,704,1,0,0,0,
        704,705,3,130,65,0,705,707,1,0,0,0,706,698,1,0,0,0,706,702,1,0,0,
        0,707,131,1,0,0,0,708,715,3,140,70,0,709,715,5,53,0,0,710,711,5,
        45,0,0,711,712,3,114,57,0,712,713,5,46,0,0,713,715,1,0,0,0,714,708,
        1,0,0,0,714,709,1,0,0,0,714,710,1,0,0,0,715,133,1,0,0,0,716,717,
        5,49,0,0,717,718,3,114,57,0,718,719,5,50,0,0,719,135,1,0,0,0,720,
        721,5,41,0,0,721,722,5,53,0,0,722,137,1,0,0,0,723,725,5,45,0,0,724,
        726,3,166,83,0,725,724,1,0,0,0,725,726,1,0,0,0,726,727,1,0,0,0,727,
        728,5,46,0,0,728,139,1,0,0,0,729,739,5,55,0,0,730,739,5,54,0,0,731,
        739,5,56,0,0,732,739,5,19,0,0,733,739,5,20,0,0,734,739,5,18,0,0,
        735,739,3,142,71,0,736,739,3,144,72,0,737,739,3,158,79,0,738,729,
        1,0,0,0,738,730,1,0,0,0,738,731,1,0,0,0,738,732,1,0,0,0,738,733,
        1,0,0,0,738,734,1,0,0,0,738,735,1,0,0,0,738,736,1,0,0,0,738,737,
        1,0,0,0,739,141,1,0,0,0,740,741,3,152,76,0,741,742,5,47,0,0,742,
        743,3,148,74,0,743,744,5,48,0,0,744,143,1,0,0,0,745,746,5,47,0,0,
        746,747,3,148,74,0,747,748,5,48,0,0,748,145,1,0,0,0,749,750,3,152,
        76,0,750,751,5,47,0,0,751,752,3,148,74,0,752,753,5,48,0,0,753,759,
        1,0,0,0,754,755,5,47,0,0,755,756,3,148,74,0,756,757,5,48,0,0,757,
        759,1,0,0,0,758,749,1,0,0,0,758,754,1,0,0,0,759,147,1,0,0,0,760,
        766,3,150,75,0,761,762,3,150,75,0,762,763,5,51,0,0,763,764,3,148,
        74,0,764,766,1,0,0,0,765,760,1,0,0,0,765,761,1,0,0,0,766,149,1,0,
        0,0,767,777,3,144,72,0,768,777,3,158,79,0,769,777,5,55,0,0,770,777,
        5,54,0,0,771,777,5,56,0,0,772,777,5,19,0,0,773,777,5,20,0,0,774,
        777,5,18,0,0,775,777,5,53,0,0,776,767,1,0,0,0,776,768,1,0,0,0,776,
        769,1,0,0,0,776,770,1,0,0,0,776,771,1,0,0,0,776,772,1,0,0,0,776,
        773,1,0,0,0,776,774,1,0,0,0,776,775,1,0,0,0,777,151,1,0,0,0,778,
        779,5,49,0,0,779,780,5,55,0,0,780,781,5,50,0,0,781,782,3,154,77,
        0,782,783,3,156,78,0,783,153,1,0,0,0,784,790,1,0,0,0,785,786,5,49,
        0,0,786,787,5,55,0,0,787,788,5,50,0,0,788,790,3,154,77,0,789,784,
        1,0,0,0,789,785,1,0,0,0,790,155,1,0,0,0,791,798,5,10,0,0,792,798,
        5,11,0,0,793,798,5,9,0,0,794,798,5,12,0,0,795,798,5,53,0,0,796,798,
        3,152,76,0,797,791,1,0,0,0,797,792,1,0,0,0,797,793,1,0,0,0,797,794,
        1,0,0,0,797,795,1,0,0,0,797,796,1,0,0,0,798,157,1,0,0,0,799,800,
        5,53,0,0,800,801,5,47,0,0,801,802,3,160,80,0,802,803,5,48,0,0,803,
        159,1,0,0,0,804,807,1,0,0,0,805,807,3,162,81,0,806,804,1,0,0,0,806,
        805,1,0,0,0,807,161,1,0,0,0,808,814,3,164,82,0,809,810,3,164,82,
        0,810,811,5,51,0,0,811,812,3,162,81,0,812,814,1,0,0,0,813,808,1,
        0,0,0,813,809,1,0,0,0,814,163,1,0,0,0,815,816,5,53,0,0,816,817,5,
        42,0,0,817,818,3,114,57,0,818,165,1,0,0,0,819,825,3,114,57,0,820,
        821,3,114,57,0,821,822,5,51,0,0,822,823,3,166,83,0,823,825,1,0,0,
        0,824,819,1,0,0,0,824,820,1,0,0,0,825,167,1,0,0,0,82,177,184,192,
        201,211,222,228,235,245,251,257,268,276,281,291,297,301,304,308,
        316,323,335,339,342,352,368,376,383,404,409,416,419,425,431,450,
        456,461,465,471,475,478,482,486,490,494,500,510,514,525,546,558,
        562,576,580,583,587,591,595,599,603,613,620,630,641,652,663,674,
        685,693,702,706,714,725,738,758,765,776,789,797,806,813,824
    ]

class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'for'", "'return'", 
                     "'func'", "'type'", "'struct'", "'interface'", "'string'", 
                     "'int'", "'float'", "'boolean'", "'const'", "'var'", 
                     "'continue'", "'break'", "'range'", "'nil'", "'true'", 
                     "'false'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
                     "'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", 
                     "'!'", "'='", "'+='", "'-='", "'*='", "'/='", "'%='", 
                     "'.'", "':'", "':='", "'_'", "'('", "')'", "'{'", "'}'", 
                     "'['", "']'", "','", "';'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "FOR", "RETURN", "FUNC", 
                      "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", 
                      "BOOLEAN", "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", 
                      "NIL", "TRUE", "FALSE", "ADD", "SUB", "MUL", "DIV", 
                      "MOD", "EQUAL", "NOT_EQUAL", "LESS", "LESS_OR_EQUAL", 
                      "GREATER", "GREATER_OR_EQUAL", "AND", "OR", "NOT", 
                      "ASSIGN", "ADD_ASSIGN", "SUB_ASSIGN", "MUL_ASSIGN", 
                      "DIV_ASSIGN", "MOD_ASSIGN", "DOT", "COLON", "SHORT_ASSIGN", 
                      "UNDERSCORE", "LP", "RP", "LB", "RB", "LSB", "RSB", 
                      "COMMA", "SEMI", "ID", "FLOAT_LIT", "INT_LIT", "STRING_LIT", 
                      "NEWLINE", "WS", "BLOCK_COMMENT", "LINE_COMMENT", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_newlines = 1
    RULE_more_declared = 2
    RULE_declared = 3
    RULE_list_statement = 4
    RULE_statement = 5
    RULE_variables_declared = 6
    RULE_var_decl_list = 7
    RULE_var_decl = 8
    RULE_type_name_ids = 9
    RULE_comma_ids = 10
    RULE_constants_declared = 11
    RULE_const_decl_list = 12
    RULE_const_decl = 13
    RULE_not_null_block_statement = 14
    RULE_more_statements = 15
    RULE_function_declared = 16
    RULE_return_type = 17
    RULE_more_types = 18
    RULE_receiver = 19
    RULE_method_declared = 20
    RULE_method_params = 21
    RULE_method_param = 22
    RULE_params_list = 23
    RULE_param = 24
    RULE_comma_param_ids = 25
    RULE_struct_declared = 26
    RULE_struct_type_list = 27
    RULE_more_struct_fields = 28
    RULE_opt_newlines = 29
    RULE_struct_field = 30
    RULE_more_ids = 31
    RULE_struct_type = 32
    RULE_interface_declared = 33
    RULE_interface_type_list = 34
    RULE_more_interface_methods = 35
    RULE_interface_type = 36
    RULE_interface_method = 37
    RULE_optional_params = 38
    RULE_optional_type = 39
    RULE_optional_semi = 40
    RULE_declared_statement = 41
    RULE_assign_statement = 42
    RULE_assign_op = 43
    RULE_assign_lhs = 44
    RULE_more_access = 45
    RULE_if_statement = 46
    RULE_for_statement = 47
    RULE_for_init = 48
    RULE_for_update = 49
    RULE_break_statement = 50
    RULE_continue_statement = 51
    RULE_return_statement = 52
    RULE_call_statement = 53
    RULE_block_stmt = 54
    RULE_block_content = 55
    RULE_expr_list = 56
    RULE_expression = 57
    RULE_expression1 = 58
    RULE_expression2 = 59
    RULE_expression3 = 60
    RULE_expression4 = 61
    RULE_expression5 = 62
    RULE_expression6 = 63
    RULE_expression7 = 64
    RULE_more_access_expr = 65
    RULE_operand = 66
    RULE_element_access = 67
    RULE_field_access = 68
    RULE_call_expr = 69
    RULE_literal = 70
    RULE_typed_array_literal = 71
    RULE_untyped_array_literal = 72
    RULE_array_literal = 73
    RULE_literal_list = 74
    RULE_literal_item = 75
    RULE_array_type = 76
    RULE_more_dimensions = 77
    RULE_type_name = 78
    RULE_struct_literal = 79
    RULE_optional_field_list = 80
    RULE_field_list = 81
    RULE_field_init = 82
    RULE_list_expression = 83

    ruleNames =  [ "program", "newlines", "more_declared", "declared", "list_statement", 
                   "statement", "variables_declared", "var_decl_list", "var_decl", 
                   "type_name_ids", "comma_ids", "constants_declared", "const_decl_list", 
                   "const_decl", "not_null_block_statement", "more_statements", 
                   "function_declared", "return_type", "more_types", "receiver", 
                   "method_declared", "method_params", "method_param", "params_list", 
                   "param", "comma_param_ids", "struct_declared", "struct_type_list", 
                   "more_struct_fields", "opt_newlines", "struct_field", 
                   "more_ids", "struct_type", "interface_declared", "interface_type_list", 
                   "more_interface_methods", "interface_type", "interface_method", 
                   "optional_params", "optional_type", "optional_semi", 
                   "declared_statement", "assign_statement", "assign_op", 
                   "assign_lhs", "more_access", "if_statement", "for_statement", 
                   "for_init", "for_update", "break_statement", "continue_statement", 
                   "return_statement", "call_statement", "block_stmt", "block_content", 
                   "expr_list", "expression", "expression1", "expression2", 
                   "expression3", "expression4", "expression5", "expression6", 
                   "expression7", "more_access_expr", "operand", "element_access", 
                   "field_access", "call_expr", "literal", "typed_array_literal", 
                   "untyped_array_literal", "array_literal", "literal_list", 
                   "literal_item", "array_type", "more_dimensions", "type_name", 
                   "struct_literal", "optional_field_list", "field_list", 
                   "field_init", "list_expression" ]

    EOF = Token.EOF
    IF=1
    ELSE=2
    FOR=3
    RETURN=4
    FUNC=5
    TYPE=6
    STRUCT=7
    INTERFACE=8
    STRING=9
    INT=10
    FLOAT=11
    BOOLEAN=12
    CONST=13
    VAR=14
    CONTINUE=15
    BREAK=16
    RANGE=17
    NIL=18
    TRUE=19
    FALSE=20
    ADD=21
    SUB=22
    MUL=23
    DIV=24
    MOD=25
    EQUAL=26
    NOT_EQUAL=27
    LESS=28
    LESS_OR_EQUAL=29
    GREATER=30
    GREATER_OR_EQUAL=31
    AND=32
    OR=33
    NOT=34
    ASSIGN=35
    ADD_ASSIGN=36
    SUB_ASSIGN=37
    MUL_ASSIGN=38
    DIV_ASSIGN=39
    MOD_ASSIGN=40
    DOT=41
    COLON=42
    SHORT_ASSIGN=43
    UNDERSCORE=44
    LP=45
    RP=46
    LB=47
    RB=48
    LSB=49
    RSB=50
    COMMA=51
    SEMI=52
    ID=53
    FLOAT_LIT=54
    INT_LIT=55
    STRING_LIT=56
    NEWLINE=57
    WS=58
    BLOCK_COMMENT=59
    LINE_COMMENT=60
    UNCLOSE_STRING=61
    ILLEGAL_ESCAPE=62
    ERROR_CHAR=63

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def newlines(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.NewlinesContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.NewlinesContext,i)


        def declared(self):
            return self.getTypedRuleContext(MiniGoParser.DeclaredContext,0)


        def more_declared(self):
            return self.getTypedRuleContext(MiniGoParser.More_declaredContext,0)


        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_program




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.newlines()
            self.state = 169
            self.declared()
            self.state = 170
            self.more_declared()
            self.state = 171
            self.newlines()
            self.state = 172
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NewlinesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(MiniGoParser.NEWLINE, 0)

        def newlines(self):
            return self.getTypedRuleContext(MiniGoParser.NewlinesContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_newlines




    def newlines(self):

        localctx = MiniGoParser.NewlinesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_newlines)
        try:
            self.state = 177
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 175
                self.match(MiniGoParser.NEWLINE)
                self.state = 176
                self.newlines()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class More_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def newlines(self):
            return self.getTypedRuleContext(MiniGoParser.NewlinesContext,0)


        def declared(self):
            return self.getTypedRuleContext(MiniGoParser.DeclaredContext,0)


        def more_declared(self):
            return self.getTypedRuleContext(MiniGoParser.More_declaredContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_more_declared




    def more_declared(self):

        localctx = MiniGoParser.More_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_more_declared)
        try:
            self.state = 184
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 180
                self.newlines()
                self.state = 181
                self.declared()
                self.state = 182
                self.more_declared()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def newlines(self):
            return self.getTypedRuleContext(MiniGoParser.NewlinesContext,0)


        def variables_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Variables_declaredContext,0)


        def constants_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Constants_declaredContext,0)


        def function_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Function_declaredContext,0)


        def method_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Method_declaredContext,0)


        def struct_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_declaredContext,0)


        def interface_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_declaredContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_declared




    def declared(self):

        localctx = MiniGoParser.DeclaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declared)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 186
                self.variables_declared()
                pass

            elif la_ == 2:
                self.state = 187
                self.constants_declared()
                pass

            elif la_ == 3:
                self.state = 188
                self.function_declared()
                pass

            elif la_ == 4:
                self.state = 189
                self.method_declared()
                pass

            elif la_ == 5:
                self.state = 190
                self.struct_declared()
                pass

            elif la_ == 6:
                self.state = 191
                self.interface_declared()
                pass


            self.state = 194
            self.newlines()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(MiniGoParser.StatementContext,0)


        def newlines(self):
            return self.getTypedRuleContext(MiniGoParser.NewlinesContext,0)


        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_statement




    def list_statement(self):

        localctx = MiniGoParser.List_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_list_statement)
        try:
            self.state = 201
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 196
                self.statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 197
                self.statement()
                self.state = 198
                self.newlines()
                self.state = 199
                self.list_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declared_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Declared_statementContext,0)


        def assign_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_statementContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(MiniGoParser.If_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(MiniGoParser.For_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Continue_statementContext,0)


        def call_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Call_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Return_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_statement




    def statement(self):

        localctx = MiniGoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_statement)
        try:
            self.state = 211
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 203
                self.declared_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 204
                self.assign_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 205
                self.if_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 206
                self.for_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 207
                self.break_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 208
                self.continue_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 209
                self.call_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 210
                self.return_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variables_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def var_decl_list(self):
            return self.getTypedRuleContext(MiniGoParser.Var_decl_listContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def NEWLINE(self):
            return self.getToken(MiniGoParser.NEWLINE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_variables_declared




    def variables_declared(self):

        localctx = MiniGoParser.Variables_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_variables_declared)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(MiniGoParser.VAR)
            self.state = 214
            self.var_decl_list()
            self.state = 215
            _la = self._input.LA(1)
            if not(_la==52 or _la==57):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_decl_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Var_declContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def var_decl_list(self):
            return self.getTypedRuleContext(MiniGoParser.Var_decl_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_decl_list




    def var_decl_list(self):

        localctx = MiniGoParser.Var_decl_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_var_decl_list)
        try:
            self.state = 222
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                self.var_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 218
                self.var_decl()
                self.state = 219
                self.match(MiniGoParser.COMMA)
                self.state = 220
                self.var_decl_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def type_name(self):
            return self.getTypedRuleContext(MiniGoParser.Type_nameContext,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def type_name_ids(self):
            return self.getTypedRuleContext(MiniGoParser.Type_name_idsContext,0)


        def expr_list(self):
            return self.getTypedRuleContext(MiniGoParser.Expr_listContext,0)


        def comma_ids(self):
            return self.getTypedRuleContext(MiniGoParser.Comma_idsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_decl




    def var_decl(self):

        localctx = MiniGoParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_var_decl)
        self._la = 0 # Token type
        try:
            self.state = 245
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 224
                self.match(MiniGoParser.ID)
                self.state = 225
                self.type_name()
                self.state = 228
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==35:
                    self.state = 226
                    self.match(MiniGoParser.ASSIGN)
                    self.state = 227
                    self.expression(0)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 230
                self.match(MiniGoParser.ID)
                self.state = 231
                self.type_name_ids()
                self.state = 232
                self.type_name()
                self.state = 235
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==35:
                    self.state = 233
                    self.match(MiniGoParser.ASSIGN)
                    self.state = 234
                    self.expr_list()


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 237
                self.match(MiniGoParser.ID)

                self.state = 238
                self.match(MiniGoParser.ASSIGN)
                self.state = 239
                self.expression(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 240
                self.match(MiniGoParser.ID)
                self.state = 241
                self.comma_ids()

                self.state = 242
                self.match(MiniGoParser.ASSIGN)
                self.state = 243
                self.expr_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_name_idsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def type_name_ids(self):
            return self.getTypedRuleContext(MiniGoParser.Type_name_idsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_type_name_ids




    def type_name_ids(self):

        localctx = MiniGoParser.Type_name_idsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_type_name_ids)
        try:
            self.state = 251
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9, 10, 11, 12, 49, 53]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [51]:
                self.enterOuterAlt(localctx, 2)
                self.state = 248
                self.match(MiniGoParser.COMMA)
                self.state = 249
                self.match(MiniGoParser.ID)
                self.state = 250
                self.type_name_ids()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comma_idsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def comma_ids(self):
            return self.getTypedRuleContext(MiniGoParser.Comma_idsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_comma_ids




    def comma_ids(self):

        localctx = MiniGoParser.Comma_idsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_comma_ids)
        try:
            self.state = 257
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9, 10, 11, 12, 35, 49, 53]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [51]:
                self.enterOuterAlt(localctx, 2)
                self.state = 254
                self.match(MiniGoParser.COMMA)
                self.state = 255
                self.match(MiniGoParser.ID)
                self.state = 256
                self.comma_ids()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Constants_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(MiniGoParser.CONST, 0)

        def const_decl_list(self):
            return self.getTypedRuleContext(MiniGoParser.Const_decl_listContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def NEWLINE(self):
            return self.getToken(MiniGoParser.NEWLINE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_constants_declared




    def constants_declared(self):

        localctx = MiniGoParser.Constants_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_constants_declared)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.match(MiniGoParser.CONST)
            self.state = 260
            self.const_decl_list()
            self.state = 261
            _la = self._input.LA(1)
            if not(_la==52 or _la==57):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Const_decl_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def const_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Const_declContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def const_decl_list(self):
            return self.getTypedRuleContext(MiniGoParser.Const_decl_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_const_decl_list




    def const_decl_list(self):

        localctx = MiniGoParser.Const_decl_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_const_decl_list)
        try:
            self.state = 268
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 263
                self.const_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 264
                self.const_decl()
                self.state = 265
                self.match(MiniGoParser.COMMA)
                self.state = 266
                self.const_decl_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Const_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_const_decl




    def const_decl(self):

        localctx = MiniGoParser.Const_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_const_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.match(MiniGoParser.ID)
            self.state = 271
            self.match(MiniGoParser.ASSIGN)
            self.state = 272
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Not_null_block_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def statement(self):
            return self.getTypedRuleContext(MiniGoParser.StatementContext,0)


        def more_statements(self):
            return self.getTypedRuleContext(MiniGoParser.More_statementsContext,0)


        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NEWLINE)
            else:
                return self.getToken(MiniGoParser.NEWLINE, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_not_null_block_statement




    def not_null_block_statement(self):

        localctx = MiniGoParser.Not_null_block_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_not_null_block_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.match(MiniGoParser.LB)
            self.state = 276
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==57:
                self.state = 275
                self.match(MiniGoParser.NEWLINE)


            self.state = 278
            self.statement()
            self.state = 279
            self.more_statements()
            self.state = 281
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==57:
                self.state = 280
                self.match(MiniGoParser.NEWLINE)


            self.state = 283
            self.match(MiniGoParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class More_statementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(MiniGoParser.StatementContext,0)


        def more_statements(self):
            return self.getTypedRuleContext(MiniGoParser.More_statementsContext,0)


        def NEWLINE(self):
            return self.getToken(MiniGoParser.NEWLINE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_more_statements




    def more_statements(self):

        localctx = MiniGoParser.More_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_more_statements)
        try:
            self.state = 291
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 286
                self.statement()
                self.state = 287
                self.more_statements()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 289
                self.match(MiniGoParser.NEWLINE)
                self.state = 290
                self.more_statements()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def not_null_block_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Not_null_block_statementContext,0)


        def params_list(self):
            return self.getTypedRuleContext(MiniGoParser.Params_listContext,0)


        def return_type(self):
            return self.getTypedRuleContext(MiniGoParser.Return_typeContext,0)


        def NEWLINE(self):
            return self.getToken(MiniGoParser.NEWLINE, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_function_declared




    def function_declared(self):

        localctx = MiniGoParser.Function_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_function_declared)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.match(MiniGoParser.FUNC)
            self.state = 294
            self.match(MiniGoParser.ID)
            self.state = 295
            self.match(MiniGoParser.LP)
            self.state = 297
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==53:
                self.state = 296
                self.params_list()


            self.state = 299
            self.match(MiniGoParser.RP)
            self.state = 301
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 9605333580258816) != 0):
                self.state = 300
                self.return_type()


            self.state = 304
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==57:
                self.state = 303
                self.match(MiniGoParser.NEWLINE)


            self.state = 306
            self.not_null_block_statement()
            self.state = 308
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==52:
                self.state = 307
                self.match(MiniGoParser.SEMI)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def type_name(self):
            return self.getTypedRuleContext(MiniGoParser.Type_nameContext,0)


        def more_types(self):
            return self.getTypedRuleContext(MiniGoParser.More_typesContext,0)


        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_return_type




    def return_type(self):

        localctx = MiniGoParser.Return_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_return_type)
        try:
            self.state = 316
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [45]:
                self.enterOuterAlt(localctx, 1)
                self.state = 310
                self.match(MiniGoParser.LP)
                self.state = 311
                self.type_name()
                self.state = 312
                self.more_types()
                self.state = 313
                self.match(MiniGoParser.RP)
                pass
            elif token in [9, 10, 11, 12, 49, 53]:
                self.enterOuterAlt(localctx, 2)
                self.state = 315
                self.type_name()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class More_typesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def type_name(self):
            return self.getTypedRuleContext(MiniGoParser.Type_nameContext,0)


        def more_types(self):
            return self.getTypedRuleContext(MiniGoParser.More_typesContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_more_types




    def more_types(self):

        localctx = MiniGoParser.More_typesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_more_types)
        try:
            self.state = 323
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [46]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [51]:
                self.enterOuterAlt(localctx, 2)
                self.state = 319
                self.match(MiniGoParser.COMMA)
                self.state = 320
                self.type_name()
                self.state = 321
                self.more_types()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReceiverContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def STRUCT(self):
            return self.getToken(MiniGoParser.STRUCT, 0)

        def INTERFACE(self):
            return self.getToken(MiniGoParser.INTERFACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_receiver




    def receiver(self):

        localctx = MiniGoParser.ReceiverContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_receiver)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self.match(MiniGoParser.ID)
            self.state = 326
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 9007199254741376) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def LP(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LP)
            else:
                return self.getToken(MiniGoParser.LP, i)

        def receiver(self):
            return self.getTypedRuleContext(MiniGoParser.ReceiverContext,0)


        def RP(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RP)
            else:
                return self.getToken(MiniGoParser.RP, i)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Block_stmtContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NEWLINE)
            else:
                return self.getToken(MiniGoParser.NEWLINE, i)

        def params_list(self):
            return self.getTypedRuleContext(MiniGoParser.Params_listContext,0)


        def type_name(self):
            return self.getTypedRuleContext(MiniGoParser.Type_nameContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_declared




    def method_declared(self):

        localctx = MiniGoParser.Method_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_method_declared)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self.match(MiniGoParser.FUNC)
            self.state = 329
            self.match(MiniGoParser.LP)
            self.state = 330
            self.receiver()
            self.state = 331
            self.match(MiniGoParser.RP)
            self.state = 332
            self.match(MiniGoParser.ID)
            self.state = 333
            self.match(MiniGoParser.LP)
            self.state = 335
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==53:
                self.state = 334
                self.params_list()


            self.state = 337
            self.match(MiniGoParser.RP)
            self.state = 339
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 9570149208169984) != 0):
                self.state = 338
                self.type_name()


            self.state = 342
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==57:
                self.state = 341
                self.match(MiniGoParser.NEWLINE)


            self.state = 344
            self.block_stmt()
            self.state = 345
            _la = self._input.LA(1)
            if not(_la==52 or _la==57):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_paramsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def method_param(self):
            return self.getTypedRuleContext(MiniGoParser.Method_paramContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def method_params(self):
            return self.getTypedRuleContext(MiniGoParser.Method_paramsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_params




    def method_params(self):

        localctx = MiniGoParser.Method_paramsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_method_params)
        try:
            self.state = 352
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 347
                self.method_param()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 348
                self.method_param()
                self.state = 349
                self.match(MiniGoParser.COMMA)
                self.state = 350
                self.method_params()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_paramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def type_name(self):
            return self.getTypedRuleContext(MiniGoParser.Type_nameContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_param




    def method_param(self):

        localctx = MiniGoParser.Method_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_method_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            self.match(MiniGoParser.ID)
            self.state = 355
            self.type_name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Params_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def type_name(self):
            return self.getTypedRuleContext(MiniGoParser.Type_nameContext,0)


        def comma_ids(self):
            return self.getTypedRuleContext(MiniGoParser.Comma_idsContext,0)


        def param(self):
            return self.getTypedRuleContext(MiniGoParser.ParamContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def params_list(self):
            return self.getTypedRuleContext(MiniGoParser.Params_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_params_list




    def params_list(self):

        localctx = MiniGoParser.Params_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_params_list)
        try:
            self.state = 368
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 357
                self.match(MiniGoParser.ID)
                self.state = 358
                self.type_name()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 359
                self.match(MiniGoParser.ID)
                self.state = 360
                self.comma_ids()
                self.state = 361
                self.type_name()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 363
                self.param()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 364
                self.param()
                self.state = 365
                self.match(MiniGoParser.COMMA)
                self.state = 366
                self.params_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def type_name(self):
            return self.getTypedRuleContext(MiniGoParser.Type_nameContext,0)


        def comma_param_ids(self):
            return self.getTypedRuleContext(MiniGoParser.Comma_param_idsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_param




    def param(self):

        localctx = MiniGoParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_param)
        try:
            self.state = 376
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 370
                self.match(MiniGoParser.ID)
                self.state = 371
                self.type_name()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 372
                self.match(MiniGoParser.ID)
                self.state = 373
                self.comma_param_ids()
                self.state = 374
                self.type_name()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comma_param_idsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def comma_param_ids(self):
            return self.getTypedRuleContext(MiniGoParser.Comma_param_idsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_comma_param_ids




    def comma_param_ids(self):

        localctx = MiniGoParser.Comma_param_idsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_comma_param_ids)
        try:
            self.state = 383
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 378
                self.match(MiniGoParser.COMMA)
                self.state = 379
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 380
                self.match(MiniGoParser.COMMA)
                self.state = 381
                self.match(MiniGoParser.ID)
                self.state = 382
                self.comma_param_ids()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def STRUCT(self):
            return self.getToken(MiniGoParser.STRUCT, 0)

        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def opt_newlines(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Opt_newlinesContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Opt_newlinesContext,i)


        def struct_type_list(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_type_listContext,0)


        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def NEWLINE(self):
            return self.getToken(MiniGoParser.NEWLINE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_declared




    def struct_declared(self):

        localctx = MiniGoParser.Struct_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_struct_declared)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 385
            self.match(MiniGoParser.TYPE)
            self.state = 386
            self.match(MiniGoParser.ID)
            self.state = 387
            self.match(MiniGoParser.STRUCT)
            self.state = 388
            self.match(MiniGoParser.LB)
            self.state = 389
            self.opt_newlines()
            self.state = 390
            self.struct_type_list()
            self.state = 391
            self.opt_newlines()
            self.state = 392
            self.match(MiniGoParser.RB)
            self.state = 393
            _la = self._input.LA(1)
            if not(_la==52 or _la==57):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_type_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_field(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_fieldContext,0)


        def opt_newlines(self):
            return self.getTypedRuleContext(MiniGoParser.Opt_newlinesContext,0)


        def more_struct_fields(self):
            return self.getTypedRuleContext(MiniGoParser.More_struct_fieldsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_type_list




    def struct_type_list(self):

        localctx = MiniGoParser.Struct_type_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_struct_type_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395
            self.struct_field()
            self.state = 396
            self.opt_newlines()
            self.state = 397
            self.more_struct_fields()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class More_struct_fieldsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_field(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_fieldContext,0)


        def opt_newlines(self):
            return self.getTypedRuleContext(MiniGoParser.Opt_newlinesContext,0)


        def more_struct_fields(self):
            return self.getTypedRuleContext(MiniGoParser.More_struct_fieldsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_more_struct_fields




    def more_struct_fields(self):

        localctx = MiniGoParser.More_struct_fieldsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_more_struct_fields)
        try:
            self.state = 404
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [48, 57]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [53]:
                self.enterOuterAlt(localctx, 2)
                self.state = 400
                self.struct_field()
                self.state = 401
                self.opt_newlines()
                self.state = 402
                self.more_struct_fields()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Opt_newlinesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(MiniGoParser.NEWLINE, 0)

        def opt_newlines(self):
            return self.getTypedRuleContext(MiniGoParser.Opt_newlinesContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_opt_newlines




    def opt_newlines(self):

        localctx = MiniGoParser.Opt_newlinesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_opt_newlines)
        try:
            self.state = 409
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 407
                self.match(MiniGoParser.NEWLINE)
                self.state = 408
                self.opt_newlines()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_fieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def more_ids(self):
            return self.getTypedRuleContext(MiniGoParser.More_idsContext,0)


        def type_name(self):
            return self.getTypedRuleContext(MiniGoParser.Type_nameContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def NEWLINE(self):
            return self.getToken(MiniGoParser.NEWLINE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_field




    def struct_field(self):

        localctx = MiniGoParser.Struct_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_struct_field)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 411
            self.match(MiniGoParser.ID)
            self.state = 412
            self.more_ids()
            self.state = 413
            self.type_name()
            self.state = 419
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 414
                self.match(MiniGoParser.SEMI)
                pass

            elif la_ == 2:
                self.state = 416
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==52:
                    self.state = 415
                    self.match(MiniGoParser.SEMI)


                self.state = 418
                self.match(MiniGoParser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class More_idsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def more_ids(self):
            return self.getTypedRuleContext(MiniGoParser.More_idsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_more_ids




    def more_ids(self):

        localctx = MiniGoParser.More_idsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_more_ids)
        try:
            self.state = 425
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9, 10, 11, 12, 49, 53]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [51]:
                self.enterOuterAlt(localctx, 2)
                self.state = 422
                self.match(MiniGoParser.COMMA)
                self.state = 423
                self.match(MiniGoParser.ID)
                self.state = 424
                self.more_ids()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_field(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_fieldContext,0)


        def struct_type(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_type




    def struct_type(self):

        localctx = MiniGoParser.Struct_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_struct_type)
        try:
            self.state = 431
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 428
                self.struct_field()
                self.state = 429
                self.struct_type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def INTERFACE(self):
            return self.getToken(MiniGoParser.INTERFACE, 0)

        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def opt_newlines(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Opt_newlinesContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Opt_newlinesContext,i)


        def interface_type_list(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_type_listContext,0)


        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def NEWLINE(self):
            return self.getToken(MiniGoParser.NEWLINE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_declared




    def interface_declared(self):

        localctx = MiniGoParser.Interface_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_interface_declared)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 433
            self.match(MiniGoParser.TYPE)
            self.state = 434
            self.match(MiniGoParser.ID)
            self.state = 435
            self.match(MiniGoParser.INTERFACE)
            self.state = 436
            self.match(MiniGoParser.LB)
            self.state = 437
            self.opt_newlines()
            self.state = 438
            self.interface_type_list()
            self.state = 439
            self.opt_newlines()
            self.state = 440
            self.match(MiniGoParser.RB)
            self.state = 441
            _la = self._input.LA(1)
            if not(_la==52 or _la==57):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_type_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def interface_method(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_methodContext,0)


        def more_interface_methods(self):
            return self.getTypedRuleContext(MiniGoParser.More_interface_methodsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_type_list




    def interface_type_list(self):

        localctx = MiniGoParser.Interface_type_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_interface_type_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 443
            self.interface_method()
            self.state = 444
            self.more_interface_methods()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class More_interface_methodsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def interface_method(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_methodContext,0)


        def more_interface_methods(self):
            return self.getTypedRuleContext(MiniGoParser.More_interface_methodsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_more_interface_methods




    def more_interface_methods(self):

        localctx = MiniGoParser.More_interface_methodsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_more_interface_methods)
        try:
            self.state = 450
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [48, 57]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [53]:
                self.enterOuterAlt(localctx, 2)
                self.state = 447
                self.interface_method()
                self.state = 448
                self.more_interface_methods()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def interface_method(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_methodContext,0)


        def interface_type(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_type




    def interface_type(self):

        localctx = MiniGoParser.Interface_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_interface_type)
        try:
            self.state = 456
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 453
                self.interface_method()
                self.state = 454
                self.interface_type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_methodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def NEWLINE(self):
            return self.getToken(MiniGoParser.NEWLINE, 0)

        def params_list(self):
            return self.getTypedRuleContext(MiniGoParser.Params_listContext,0)


        def type_name(self):
            return self.getTypedRuleContext(MiniGoParser.Type_nameContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_method




    def interface_method(self):

        localctx = MiniGoParser.Interface_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_interface_method)
        self._la = 0 # Token type
        try:
            self.state = 478
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 458
                self.match(MiniGoParser.ID)
                self.state = 459
                self.match(MiniGoParser.LP)
                self.state = 461
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==53:
                    self.state = 460
                    self.params_list()


                self.state = 463
                self.match(MiniGoParser.RP)
                self.state = 465
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 9570149208169984) != 0):
                    self.state = 464
                    self.type_name()


                self.state = 467
                _la = self._input.LA(1)
                if not(_la==52 or _la==57):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 468
                self.match(MiniGoParser.ID)
                self.state = 469
                self.match(MiniGoParser.LP)
                self.state = 471
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==53:
                    self.state = 470
                    self.params_list()


                self.state = 473
                self.match(MiniGoParser.RP)
                self.state = 475
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 9570149208169984) != 0):
                    self.state = 474
                    self.type_name()


                self.state = 477
                _la = self._input.LA(1)
                if not(_la==52 or _la==57):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Optional_paramsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def params_list(self):
            return self.getTypedRuleContext(MiniGoParser.Params_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_optional_params




    def optional_params(self):

        localctx = MiniGoParser.Optional_paramsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_optional_params)
        try:
            self.state = 482
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [-1]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [53]:
                self.enterOuterAlt(localctx, 2)
                self.state = 481
                self.params_list()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Optional_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_name(self):
            return self.getTypedRuleContext(MiniGoParser.Type_nameContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_optional_type




    def optional_type(self):

        localctx = MiniGoParser.Optional_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_optional_type)
        try:
            self.state = 486
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [-1]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [9, 10, 11, 12, 49, 53]:
                self.enterOuterAlt(localctx, 2)
                self.state = 485
                self.type_name()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Optional_semiContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_optional_semi




    def optional_semi(self):

        localctx = MiniGoParser.Optional_semiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_optional_semi)
        try:
            self.state = 490
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [-1]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [52]:
                self.enterOuterAlt(localctx, 2)
                self.state = 489
                self.match(MiniGoParser.SEMI)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declared_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variables_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Variables_declaredContext,0)


        def constants_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Constants_declaredContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_declared_statement




    def declared_statement(self):

        localctx = MiniGoParser.Declared_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_declared_statement)
        try:
            self.state = 494
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 492
                self.variables_declared()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 493
                self.constants_declared()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_lhs(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_lhsContext,0)


        def assign_op(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_opContext,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assign_statement




    def assign_statement(self):

        localctx = MiniGoParser.Assign_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_assign_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 496
            self.assign_lhs()
            self.state = 497
            self.assign_op()
            self.state = 498
            self.expression(0)
            self.state = 500
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==52:
                self.state = 499
                self.match(MiniGoParser.SEMI)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def ADD_ASSIGN(self):
            return self.getToken(MiniGoParser.ADD_ASSIGN, 0)

        def SUB_ASSIGN(self):
            return self.getToken(MiniGoParser.SUB_ASSIGN, 0)

        def MUL_ASSIGN(self):
            return self.getToken(MiniGoParser.MUL_ASSIGN, 0)

        def DIV_ASSIGN(self):
            return self.getToken(MiniGoParser.DIV_ASSIGN, 0)

        def MOD_ASSIGN(self):
            return self.getToken(MiniGoParser.MOD_ASSIGN, 0)

        def SHORT_ASSIGN(self):
            return self.getToken(MiniGoParser.SHORT_ASSIGN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assign_op




    def assign_op(self):

        localctx = MiniGoParser.Assign_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_assign_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 502
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 10960756539392) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_lhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def more_access(self):
            return self.getTypedRuleContext(MiniGoParser.More_accessContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assign_lhs




    def assign_lhs(self):

        localctx = MiniGoParser.Assign_lhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_assign_lhs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 504
            self.match(MiniGoParser.ID)
            self.state = 505
            self.more_access()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class More_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def more_access(self):
            return self.getTypedRuleContext(MiniGoParser.More_accessContext,0)


        def field_access(self):
            return self.getTypedRuleContext(MiniGoParser.Field_accessContext,0)


        def element_access(self):
            return self.getTypedRuleContext(MiniGoParser.Element_accessContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_more_access




    def more_access(self):

        localctx = MiniGoParser.More_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_more_access)
        try:
            self.state = 514
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [35, 36, 37, 38, 39, 40, 43, 45]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [41, 49]:
                self.enterOuterAlt(localctx, 2)
                self.state = 510
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [41]:
                    self.state = 508
                    self.field_access()
                    pass
                elif token in [49]:
                    self.state = 509
                    self.element_access()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 512
                self.more_access()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def not_null_block_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Not_null_block_statementContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Not_null_block_statementContext,i)


        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def if_statement(self):
            return self.getTypedRuleContext(MiniGoParser.If_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_if_statement




    def if_statement(self):

        localctx = MiniGoParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 516
            self.match(MiniGoParser.IF)
            self.state = 517
            self.match(MiniGoParser.LP)
            self.state = 518
            self.expression(0)
            self.state = 519
            self.match(MiniGoParser.RP)
            self.state = 520
            self.not_null_block_statement()
            self.state = 525
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.state = 521
                self.match(MiniGoParser.ELSE)
                self.state = 522
                self.if_statement()

            elif la_ == 2:
                self.state = 523
                self.match(MiniGoParser.ELSE)
                self.state = 524
                self.not_null_block_statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def SHORT_ASSIGN(self):
            return self.getToken(MiniGoParser.SHORT_ASSIGN, 0)

        def RANGE(self):
            return self.getToken(MiniGoParser.RANGE, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def not_null_block_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Not_null_block_statementContext,0)


        def for_init(self):
            return self.getTypedRuleContext(MiniGoParser.For_initContext,0)


        def for_update(self):
            return self.getTypedRuleContext(MiniGoParser.For_updateContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def UNDERSCORE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.UNDERSCORE)
            else:
                return self.getToken(MiniGoParser.UNDERSCORE, i)

        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMI)
            else:
                return self.getToken(MiniGoParser.SEMI, i)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NEWLINE)
            else:
                return self.getToken(MiniGoParser.NEWLINE, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_for_statement




    def for_statement(self):

        localctx = MiniGoParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_for_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 527
            self.match(MiniGoParser.FOR)
            self.state = 546
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.state = 528
                _la = self._input.LA(1)
                if not(_la==44 or _la==53):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 529
                self.match(MiniGoParser.COMMA)
                self.state = 530
                _la = self._input.LA(1)
                if not(_la==44 or _la==53):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 531
                self.match(MiniGoParser.SHORT_ASSIGN)
                self.state = 532
                self.match(MiniGoParser.RANGE)
                self.state = 533
                self.expression(0)
                self.state = 534
                self.not_null_block_statement()
                pass

            elif la_ == 2:
                self.state = 536
                self.for_init()
                self.state = 537
                _la = self._input.LA(1)
                if not(_la==52 or _la==57):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 538
                self.expression(0)
                self.state = 539
                _la = self._input.LA(1)
                if not(_la==52 or _la==57):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 540
                self.for_update()
                self.state = 541
                self.not_null_block_statement()
                pass

            elif la_ == 3:
                self.state = 543
                self.expression(0)
                self.state = 544
                self.not_null_block_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def SHORT_ASSIGN(self):
            return self.getToken(MiniGoParser.SHORT_ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def assign_op(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_opContext,0)


        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def type_name(self):
            return self.getTypedRuleContext(MiniGoParser.Type_nameContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_init




    def for_init(self):

        localctx = MiniGoParser.For_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_for_init)
        self._la = 0 # Token type
        try:
            self.state = 562
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 548
                self.match(MiniGoParser.ID)
                self.state = 549
                self.match(MiniGoParser.SHORT_ASSIGN)
                self.state = 550
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 551
                self.match(MiniGoParser.ID)
                self.state = 552
                self.assign_op()
                self.state = 553
                self.expression(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 555
                self.match(MiniGoParser.VAR)
                self.state = 556
                self.match(MiniGoParser.ID)
                self.state = 558
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 9570149208169984) != 0):
                    self.state = 557
                    self.type_name()


                self.state = 560
                self.match(MiniGoParser.ASSIGN)
                self.state = 561
                self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_updateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def assign_op(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_opContext,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_update




    def for_update(self):

        localctx = MiniGoParser.For_updateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_for_update)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 564
            self.match(MiniGoParser.ID)
            self.state = 565
            self.assign_op()
            self.state = 566
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MiniGoParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def NEWLINE(self):
            return self.getToken(MiniGoParser.NEWLINE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_break_statement




    def break_statement(self):

        localctx = MiniGoParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_break_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 568
            self.match(MiniGoParser.BREAK)
            self.state = 569
            _la = self._input.LA(1)
            if not(_la==52 or _la==57):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MiniGoParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def NEWLINE(self):
            return self.getToken(MiniGoParser.NEWLINE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_continue_statement




    def continue_statement(self):

        localctx = MiniGoParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_continue_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 571
            self.match(MiniGoParser.CONTINUE)
            self.state = 572
            _la = self._input.LA(1)
            if not(_la==52 or _la==57):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MiniGoParser.RETURN, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def NEWLINE(self):
            return self.getToken(MiniGoParser.NEWLINE, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_return_statement




    def return_statement(self):

        localctx = MiniGoParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_return_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 574
            self.match(MiniGoParser.RETURN)
            self.state = 583
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                self.state = 576
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 135846877820878848) != 0):
                    self.state = 575
                    self.expression(0)


                self.state = 578
                self.match(MiniGoParser.SEMI)
                pass

            elif la_ == 2:
                self.state = 580
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 135846877820878848) != 0):
                    self.state = 579
                    self.expression(0)


                self.state = 582
                self.match(MiniGoParser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def assign_lhs(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_lhsContext,0)


        def list_expression(self):
            return self.getTypedRuleContext(MiniGoParser.List_expressionContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_call_statement




    def call_statement(self):

        localctx = MiniGoParser.Call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_call_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 587
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
            if la_ == 1:
                self.state = 585
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.state = 586
                self.assign_lhs()
                pass


            self.state = 589
            self.match(MiniGoParser.LP)
            self.state = 591
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 135846877820878848) != 0):
                self.state = 590
                self.list_expression()


            self.state = 593
            self.match(MiniGoParser.RP)
            self.state = 595
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==52:
                self.state = 594
                self.match(MiniGoParser.SEMI)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def block_content(self):
            return self.getTypedRuleContext(MiniGoParser.Block_contentContext,0)


        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NEWLINE)
            else:
                return self.getToken(MiniGoParser.NEWLINE, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_block_stmt




    def block_stmt(self):

        localctx = MiniGoParser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_block_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 597
            self.match(MiniGoParser.LB)
            self.state = 599
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,58,self._ctx)
            if la_ == 1:
                self.state = 598
                self.match(MiniGoParser.NEWLINE)


            self.state = 601
            self.block_content()
            self.state = 603
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==57:
                self.state = 602
                self.match(MiniGoParser.NEWLINE)


            self.state = 605
            self.match(MiniGoParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_contentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(MiniGoParser.StatementContext,0)


        def block_content(self):
            return self.getTypedRuleContext(MiniGoParser.Block_contentContext,0)


        def NEWLINE(self):
            return self.getToken(MiniGoParser.NEWLINE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_block_content




    def block_content(self):

        localctx = MiniGoParser.Block_contentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_block_content)
        try:
            self.state = 613
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,60,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 608
                self.statement()
                self.state = 609
                self.block_content()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 611
                self.match(MiniGoParser.NEWLINE)
                self.state = 612
                self.block_content()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def expr_list(self):
            return self.getTypedRuleContext(MiniGoParser.Expr_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr_list




    def expr_list(self):

        localctx = MiniGoParser.Expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_expr_list)
        try:
            self.state = 620
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,61,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 615
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 616
                self.expression(0)
                self.state = 617
                self.match(MiniGoParser.COMMA)
                self.state = 618
                self.expr_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def OR(self):
            return self.getToken(MiniGoParser.OR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 114
        self.enterRecursionRule(localctx, 114, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 623
            self.expression1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 630
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,62,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 625
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 626
                    self.match(MiniGoParser.OR)
                    self.state = 627
                    self.expression1(0) 
                self.state = 632
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,62,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression2(self):
            return self.getTypedRuleContext(MiniGoParser.Expression2Context,0)


        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def AND(self):
            return self.getToken(MiniGoParser.AND, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression1



    def expression1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 116
        self.enterRecursionRule(localctx, 116, self.RULE_expression1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 634
            self.expression2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 641
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,63,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression1)
                    self.state = 636
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 637
                    self.match(MiniGoParser.AND)
                    self.state = 638
                    self.expression2(0) 
                self.state = 643
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,63,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression3(self):
            return self.getTypedRuleContext(MiniGoParser.Expression3Context,0)


        def expression2(self):
            return self.getTypedRuleContext(MiniGoParser.Expression2Context,0)


        def EQUAL(self):
            return self.getToken(MiniGoParser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(MiniGoParser.NOT_EQUAL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression2



    def expression2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 118
        self.enterRecursionRule(localctx, 118, self.RULE_expression2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 645
            self.expression3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 652
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,64,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                    self.state = 647
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 648
                    _la = self._input.LA(1)
                    if not(_la==26 or _la==27):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 649
                    self.expression3(0) 
                self.state = 654
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,64,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression4(self):
            return self.getTypedRuleContext(MiniGoParser.Expression4Context,0)


        def expression3(self):
            return self.getTypedRuleContext(MiniGoParser.Expression3Context,0)


        def LESS(self):
            return self.getToken(MiniGoParser.LESS, 0)

        def LESS_OR_EQUAL(self):
            return self.getToken(MiniGoParser.LESS_OR_EQUAL, 0)

        def GREATER(self):
            return self.getToken(MiniGoParser.GREATER, 0)

        def GREATER_OR_EQUAL(self):
            return self.getToken(MiniGoParser.GREATER_OR_EQUAL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression3



    def expression3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 120
        self.enterRecursionRule(localctx, 120, self.RULE_expression3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 656
            self.expression4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 663
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,65,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                    self.state = 658
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 659
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4026531840) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 660
                    self.expression4(0) 
                self.state = 665
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,65,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression5(self):
            return self.getTypedRuleContext(MiniGoParser.Expression5Context,0)


        def expression4(self):
            return self.getTypedRuleContext(MiniGoParser.Expression4Context,0)


        def ADD(self):
            return self.getToken(MiniGoParser.ADD, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression4



    def expression4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 122
        self.enterRecursionRule(localctx, 122, self.RULE_expression4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 667
            self.expression5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 674
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,66,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                    self.state = 669
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 670
                    _la = self._input.LA(1)
                    if not(_la==21 or _la==22):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 671
                    self.expression5(0) 
                self.state = 676
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,66,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression6(self):
            return self.getTypedRuleContext(MiniGoParser.Expression6Context,0)


        def expression5(self):
            return self.getTypedRuleContext(MiniGoParser.Expression5Context,0)


        def MUL(self):
            return self.getToken(MiniGoParser.MUL, 0)

        def DIV(self):
            return self.getToken(MiniGoParser.DIV, 0)

        def MOD(self):
            return self.getToken(MiniGoParser.MOD, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression5



    def expression5(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression5Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 124
        self.enterRecursionRule(localctx, 124, self.RULE_expression5, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 678
            self.expression6()
            self._ctx.stop = self._input.LT(-1)
            self.state = 685
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,67,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression5)
                    self.state = 680
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 681
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 58720256) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 682
                    self.expression6() 
                self.state = 687
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,67,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)

        def expression6(self):
            return self.getTypedRuleContext(MiniGoParser.Expression6Context,0)


        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def expression7(self):
            return self.getTypedRuleContext(MiniGoParser.Expression7Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expression6




    def expression6(self):

        localctx = MiniGoParser.Expression6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_expression6)
        try:
            self.state = 693
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 688
                self.match(MiniGoParser.NOT)
                self.state = 689
                self.expression6()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 690
                self.match(MiniGoParser.SUB)
                self.state = 691
                self.expression6()
                pass
            elif token in [18, 19, 20, 45, 47, 49, 53, 54, 55, 56]:
                self.enterOuterAlt(localctx, 3)
                self.state = 692
                self.expression7()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self):
            return self.getTypedRuleContext(MiniGoParser.OperandContext,0)


        def more_access_expr(self):
            return self.getTypedRuleContext(MiniGoParser.More_access_exprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expression7




    def expression7(self):

        localctx = MiniGoParser.Expression7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_expression7)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 695
            self.operand()
            self.state = 696
            self.more_access_expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class More_access_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def more_access_expr(self):
            return self.getTypedRuleContext(MiniGoParser.More_access_exprContext,0)


        def element_access(self):
            return self.getTypedRuleContext(MiniGoParser.Element_accessContext,0)


        def field_access(self):
            return self.getTypedRuleContext(MiniGoParser.Field_accessContext,0)


        def call_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Call_exprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_more_access_expr




    def more_access_expr(self):

        localctx = MiniGoParser.More_access_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_more_access_expr)
        try:
            self.state = 706
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,70,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 702
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [49]:
                    self.state = 699
                    self.element_access()
                    pass
                elif token in [41]:
                    self.state = 700
                    self.field_access()
                    pass
                elif token in [45]:
                    self.state = 701
                    self.call_expr()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 704
                self.more_access_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_operand




    def operand(self):

        localctx = MiniGoParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_operand)
        try:
            self.state = 714
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,71,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 708
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 709
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 710
                self.match(MiniGoParser.LP)
                self.state = 711
                self.expression(0)
                self.state = 712
                self.match(MiniGoParser.RP)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Element_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(MiniGoParser.LSB, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RSB(self):
            return self.getToken(MiniGoParser.RSB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_element_access




    def element_access(self):

        localctx = MiniGoParser.Element_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_element_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 716
            self.match(MiniGoParser.LSB)
            self.state = 717
            self.expression(0)
            self.state = 718
            self.match(MiniGoParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_field_access




    def field_access(self):

        localctx = MiniGoParser.Field_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_field_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 720
            self.match(MiniGoParser.DOT)
            self.state = 721
            self.match(MiniGoParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def list_expression(self):
            return self.getTypedRuleContext(MiniGoParser.List_expressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_call_expr




    def call_expr(self):

        localctx = MiniGoParser.Call_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_call_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 723
            self.match(MiniGoParser.LP)
            self.state = 725
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 135846877820878848) != 0):
                self.state = 724
                self.list_expression()


            self.state = 727
            self.match(MiniGoParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(MiniGoParser.FLOAT_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(MiniGoParser.STRING_LIT, 0)

        def TRUE(self):
            return self.getToken(MiniGoParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MiniGoParser.FALSE, 0)

        def NIL(self):
            return self.getToken(MiniGoParser.NIL, 0)

        def typed_array_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Typed_array_literalContext,0)


        def untyped_array_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Untyped_array_literalContext,0)


        def struct_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literalContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_literal




    def literal(self):

        localctx = MiniGoParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_literal)
        try:
            self.state = 738
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [55]:
                self.enterOuterAlt(localctx, 1)
                self.state = 729
                self.match(MiniGoParser.INT_LIT)
                pass
            elif token in [54]:
                self.enterOuterAlt(localctx, 2)
                self.state = 730
                self.match(MiniGoParser.FLOAT_LIT)
                pass
            elif token in [56]:
                self.enterOuterAlt(localctx, 3)
                self.state = 731
                self.match(MiniGoParser.STRING_LIT)
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 4)
                self.state = 732
                self.match(MiniGoParser.TRUE)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 5)
                self.state = 733
                self.match(MiniGoParser.FALSE)
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 6)
                self.state = 734
                self.match(MiniGoParser.NIL)
                pass
            elif token in [49]:
                self.enterOuterAlt(localctx, 7)
                self.state = 735
                self.typed_array_literal()
                pass
            elif token in [47]:
                self.enterOuterAlt(localctx, 8)
                self.state = 736
                self.untyped_array_literal()
                pass
            elif token in [53]:
                self.enterOuterAlt(localctx, 9)
                self.state = 737
                self.struct_literal()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Typed_array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_type(self):
            return self.getTypedRuleContext(MiniGoParser.Array_typeContext,0)


        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def literal_list(self):
            return self.getTypedRuleContext(MiniGoParser.Literal_listContext,0)


        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_typed_array_literal




    def typed_array_literal(self):

        localctx = MiniGoParser.Typed_array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_typed_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 740
            self.array_type()
            self.state = 741
            self.match(MiniGoParser.LB)
            self.state = 742
            self.literal_list()
            self.state = 743
            self.match(MiniGoParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Untyped_array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def literal_list(self):
            return self.getTypedRuleContext(MiniGoParser.Literal_listContext,0)


        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_untyped_array_literal




    def untyped_array_literal(self):

        localctx = MiniGoParser.Untyped_array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_untyped_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 745
            self.match(MiniGoParser.LB)
            self.state = 746
            self.literal_list()
            self.state = 747
            self.match(MiniGoParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_type(self):
            return self.getTypedRuleContext(MiniGoParser.Array_typeContext,0)


        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def literal_list(self):
            return self.getTypedRuleContext(MiniGoParser.Literal_listContext,0)


        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_literal




    def array_literal(self):

        localctx = MiniGoParser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 146, self.RULE_array_literal)
        try:
            self.state = 758
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [49]:
                self.enterOuterAlt(localctx, 1)
                self.state = 749
                self.array_type()
                self.state = 750
                self.match(MiniGoParser.LB)
                self.state = 751
                self.literal_list()
                self.state = 752
                self.match(MiniGoParser.RB)
                pass
            elif token in [47]:
                self.enterOuterAlt(localctx, 2)
                self.state = 754
                self.match(MiniGoParser.LB)
                self.state = 755
                self.literal_list()
                self.state = 756
                self.match(MiniGoParser.RB)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Literal_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal_item(self):
            return self.getTypedRuleContext(MiniGoParser.Literal_itemContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def literal_list(self):
            return self.getTypedRuleContext(MiniGoParser.Literal_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_literal_list




    def literal_list(self):

        localctx = MiniGoParser.Literal_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 148, self.RULE_literal_list)
        try:
            self.state = 765
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,75,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 760
                self.literal_item()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 761
                self.literal_item()
                self.state = 762
                self.match(MiniGoParser.COMMA)
                self.state = 763
                self.literal_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Literal_itemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def untyped_array_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Untyped_array_literalContext,0)


        def struct_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literalContext,0)


        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(MiniGoParser.FLOAT_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(MiniGoParser.STRING_LIT, 0)

        def TRUE(self):
            return self.getToken(MiniGoParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MiniGoParser.FALSE, 0)

        def NIL(self):
            return self.getToken(MiniGoParser.NIL, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_literal_item




    def literal_item(self):

        localctx = MiniGoParser.Literal_itemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 150, self.RULE_literal_item)
        try:
            self.state = 776
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,76,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 767
                self.untyped_array_literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 768
                self.struct_literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 769
                self.match(MiniGoParser.INT_LIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 770
                self.match(MiniGoParser.FLOAT_LIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 771
                self.match(MiniGoParser.STRING_LIT)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 772
                self.match(MiniGoParser.TRUE)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 773
                self.match(MiniGoParser.FALSE)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 774
                self.match(MiniGoParser.NIL)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 775
                self.match(MiniGoParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(MiniGoParser.LSB, 0)

        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def RSB(self):
            return self.getToken(MiniGoParser.RSB, 0)

        def more_dimensions(self):
            return self.getTypedRuleContext(MiniGoParser.More_dimensionsContext,0)


        def type_name(self):
            return self.getTypedRuleContext(MiniGoParser.Type_nameContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_type




    def array_type(self):

        localctx = MiniGoParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 152, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 778
            self.match(MiniGoParser.LSB)
            self.state = 779
            self.match(MiniGoParser.INT_LIT)
            self.state = 780
            self.match(MiniGoParser.RSB)
            self.state = 781
            self.more_dimensions()
            self.state = 782
            self.type_name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class More_dimensionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(MiniGoParser.LSB, 0)

        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def RSB(self):
            return self.getToken(MiniGoParser.RSB, 0)

        def more_dimensions(self):
            return self.getTypedRuleContext(MiniGoParser.More_dimensionsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_more_dimensions




    def more_dimensions(self):

        localctx = MiniGoParser.More_dimensionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 154, self.RULE_more_dimensions)
        try:
            self.state = 789
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,77,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 785
                self.match(MiniGoParser.LSB)
                self.state = 786
                self.match(MiniGoParser.INT_LIT)
                self.state = 787
                self.match(MiniGoParser.RSB)
                self.state = 788
                self.more_dimensions()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def array_type(self):
            return self.getTypedRuleContext(MiniGoParser.Array_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_type_name




    def type_name(self):

        localctx = MiniGoParser.Type_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 156, self.RULE_type_name)
        try:
            self.state = 797
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 791
                self.match(MiniGoParser.INT)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 792
                self.match(MiniGoParser.FLOAT)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 3)
                self.state = 793
                self.match(MiniGoParser.STRING)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 4)
                self.state = 794
                self.match(MiniGoParser.BOOLEAN)
                pass
            elif token in [53]:
                self.enterOuterAlt(localctx, 5)
                self.state = 795
                self.match(MiniGoParser.ID)
                pass
            elif token in [49]:
                self.enterOuterAlt(localctx, 6)
                self.state = 796
                self.array_type()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def optional_field_list(self):
            return self.getTypedRuleContext(MiniGoParser.Optional_field_listContext,0)


        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_literal




    def struct_literal(self):

        localctx = MiniGoParser.Struct_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 158, self.RULE_struct_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 799
            self.match(MiniGoParser.ID)
            self.state = 800
            self.match(MiniGoParser.LB)
            self.state = 801
            self.optional_field_list()
            self.state = 802
            self.match(MiniGoParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Optional_field_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field_list(self):
            return self.getTypedRuleContext(MiniGoParser.Field_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_optional_field_list




    def optional_field_list(self):

        localctx = MiniGoParser.Optional_field_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 160, self.RULE_optional_field_list)
        try:
            self.state = 806
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [48]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [53]:
                self.enterOuterAlt(localctx, 2)
                self.state = 805
                self.field_list()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field_init(self):
            return self.getTypedRuleContext(MiniGoParser.Field_initContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def field_list(self):
            return self.getTypedRuleContext(MiniGoParser.Field_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_field_list




    def field_list(self):

        localctx = MiniGoParser.Field_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 162, self.RULE_field_list)
        try:
            self.state = 813
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,80,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 808
                self.field_init()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 809
                self.field_init()
                self.state = 810
                self.match(MiniGoParser.COMMA)
                self.state = 811
                self.field_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COLON(self):
            return self.getToken(MiniGoParser.COLON, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_field_init




    def field_init(self):

        localctx = MiniGoParser.Field_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 164, self.RULE_field_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 815
            self.match(MiniGoParser.ID)
            self.state = 816
            self.match(MiniGoParser.COLON)
            self.state = 817
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_expression(self):
            return self.getTypedRuleContext(MiniGoParser.List_expressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_expression




    def list_expression(self):

        localctx = MiniGoParser.List_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 166, self.RULE_list_expression)
        try:
            self.state = 824
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,81,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 819
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 820
                self.expression(0)
                self.state = 821
                self.match(MiniGoParser.COMMA)
                self.state = 822
                self.list_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[57] = self.expression_sempred
        self._predicates[58] = self.expression1_sempred
        self._predicates[59] = self.expression2_sempred
        self._predicates[60] = self.expression3_sempred
        self._predicates[61] = self.expression4_sempred
        self._predicates[62] = self.expression5_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expression1_sempred(self, localctx:Expression1Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expression2_sempred(self, localctx:Expression2Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expression3_sempred(self, localctx:Expression3Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expression4_sempred(self, localctx:Expression4Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def expression5_sempred(self, localctx:Expression5Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         




