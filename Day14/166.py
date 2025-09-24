from fractions import Fraction

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        frac = Fraction(numerator, denominator)
        numerator, denominator = frac.numerator, frac.denominator
        
        res = []
        if numerator * denominator < 0:
            res.append("-")
        numerator, denominator = abs(numerator), abs(denominator)
        
        res.append(str(numerator // denominator))
        remainder = numerator % denominator
        if remainder == 0:
            return "".join(res)
        
        res.append(".")
        remainder_map = {}
        
        while remainder:
            if remainder in remainder_map:
                res.insert(remainder_map[remainder], "(")
                res.append(")")
                break
            remainder_map[remainder] = len(res)
            remainder *= 10
            res.append(str(remainder // denominator))
            remainder %= denominator
        
        return "".join(res)