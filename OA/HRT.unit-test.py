import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import unittest
from calculator import Lit, Var

# Test all functionality of the calculator, which is:
#  - Lit(i), Var(name) to create literal expressions
#  - foo.Add(bar), foo.Sub(bar), foo.Mul(bar) to perform operations on two expressions
#  - foo.toString() and foo.simplify() to display and evaluate calculator expressions

class TestingCalculator(unittest.TestCase):
    def eq(self, e, before, after):
        # Ensure the string represtation matches expected value
        self.assertEqual(e.toString(), before)
        # Ensure the string represtation after simplication matches expected value
        self.assertEqual(e.simplify().toString(), after)
        # simplify() should NOT change the original value
        self.assertEqual(e.toString(), before)
        
    def testLiterals(self):
        self.eq(Lit(2), "2", "2")
        self.eq(Lit(-1), "-1", "-1")
        
    def testAdding(self):
        self.eq(Lit(2).Add(Lit(3)), "(2 + 3)", "5")
        self.eq(Lit(1).Add(Lit(2)).Add(Lit(3)), "((1 + 2) + 3)", "6")
        
    def testSubtracting(self):
        self.eq(Lit(1).Sub(Lit(2)).Sub(Lit(3)), "((1 - 2) - 3)", "-4")
        
    def testMultiplying(self):
        self.eq(Lit(1).Mul(Lit(2)).Mul(Lit(3)), "((1 * 2) * 3)", "6")
        
    def testGraph(self):
        x = Lit(4).Add(Lit(5))
        self.eq(x.Mul(x), "((4 + 5) * (4 + 5))", "81")
        
    def testVariables(self):
        self.eq(Var("x"), "x", "x")
        self.eq(Var("x").Add(Var("y")), "(x + y)", "(x + y)")
        self.eq(Var("x").Add(Lit(1)), "(x + 1)", "(x + 1)")
        self.eq(Var("x").Add(Lit(1).Add(Lit(2))), "(x + (1 + 2))", "(x + 3)")
        self.eq(Var("x").Add(Lit(1)).Add(Lit(2)), "((x + 1) + 2)", "((x + 1) + 2)")
        
    def testUseResults(self):
        x = Lit(4).Add(Lit(5)).simplify()
        self.eq(x.Mul(x), "(9 * 9)", "81")
        y = x.Mul(x).simplify()
        self.eq(y.Add(x), "(81 + 9)", "90")


# caluclator.py
# interesting
class Lit:
    def __init__(self, value):
        self.value = value

    def Add(self, other):
        return Add(self, other)

    def Sub(self, other):
        return Sub(self, other)

    def Mul(self, other):
        return Mul(self, other)

    def toString(self):
        return str(self.value)

    def simplify(self):
        return self

class Var:
    def __init__(self, name):
        self.name = name

    def Add(self, other):
        return Add(self, other)

    def Sub(self, other):
        return Sub(self, other)

    def Mul(self, other):
        return Mul(self, other)

    def toString(self):
        return self.name

    def simplify(self):
        return self

class Add:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def Add(self, other):
        return Add(self, other)

    def Sub(self, other):
        return Sub(self, other)

    def Mul(self, other):
        return Mul(self, other)

    def toString(self):
        return f"({self.left.toString()} + {self.right.toString()})"

    def simplify(self):
        left = self.left.simplify()
        right = self.right.simplify()
        if isinstance(left, Lit) and isinstance(right, Lit):
            return Lit(left.value + right.value)
        return Add(left, right)

class Sub:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def Add(self, other):
        return Add(self, other)

    def Sub(self, other):
        return Sub(self, other)

    def Mul(self, other):
        return Mul(self, other)

    def toString(self):
        return f"({self.left.toString()} - {self.right.toString()})"

    def simplify(self):
        left = self.left.simplify()
        right = self.right.simplify()
        if isinstance(left, Lit) and isinstance(right, Lit):
            return Lit(left.value - right.value)
        return Sub(left, right)

class Mul:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def Add(self, other):
        return Add(self, other)

    def Sub(self, other):
        return Sub(self, other)

    def Mul(self, other):
        return Mul(self, other)

    def toString(self):
        return f"({self.left.toString()} * {self.right.toString()})"

    def simplify(self):
        left = self.left.simplify()
        right = self.right.simplify()
        if isinstance(left, Lit) and isinstance(right, Lit):
            return Lit(left.value * right.value)
        return Mul(left, right)