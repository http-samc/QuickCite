from QuickCite import Citation
import unittest

global c, MLA, APA, CHI
c = Citation("https://www.brookings.edu/blog/future-development/2020/01/17/whoever-leads-in-artificial-intelligence-in-2030-will-rule-the-world-until-2100/")

MLA = """Gill, Indermit. "Whoever leads in artificial intelligence in 2030 will rule the world until 2100" Brookings, 2020-01-17, https://www.brookings.edu/blog/future-development/2020/01/17/whoever-leads-in-artificial-intelligence-in-2030-will-rule-the-world-until-2100/. Accessed 2/5/2021."""

APA = """Gill, I. (2020, 01-17) Whoever leads in artificial intelligence in 2030 will rule the world until 2100. Brookings.
https://www.brookings.edu/blog/future-development/2020/01/17/whoever-leads-in-artificial-intelligence-in-2030-will-rule-the-world-until-2100/"""

CHI = """Indermit Gill, "Whoever leads in artificial intelligence in 2030 will rule the world until 2100," Brookings, last modified 2020-01-17, https://www.brookings.edu/blog/future-development/2020/01/17/whoever-leads-in-artificial-intelligence-in-2030-will-rule-the-world-until-2100/."""

class TestQuickCite(unittest.TestCase):

    def testMLA(self):
        self.assertEqual(c.MLA(), MLA)
    
    def testAPA(self):
        self.assertEqual(c.APA(), APA)
    
    def testCHI(self):
        self.assertEqual(c.CHI(), CHI)

if __name__ == "__main__":
    unittest.main()