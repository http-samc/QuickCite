# QuickCite
 An API Wrapper for automatic MLA, CHI, & APA citations

## How To Use:

*Installation with PIP*
```
pip install QuickCite
```

*Basic Usage*

```python
# Import Module
from QuickCite import Citation 

# Create Citation Object with URL as paramater
c = Citation(URL="https://www.brookings.edu/research/trans-atlantic-scorecard-april-2021/")

# Get Citations
MLA = c.MLA()
APA = c.APA()
CHI = c.CHI()

print("MLA:\n"+MLA)
print("\nAPA:\n"+APA)
print("\nCHI:\n"+CHI)
```

Output:

```
MLA:
Wright, Thomas. "Trans-Atlantic Scorecard — April 2021" Brookings, 2021-04-27, https://www.brookings.edu/research/trans-atlantic-scorecard-april-2021/. Accessed 2/5/2021.

APA:
Wright, T. (2021, 04-27) Trans-Atlantic Scorecard — April 2021. Brookings. https://www.brookings.edu/research/trans-atlantic-scorecard-april-2021/

CHI:
Thomas Wright, "Trans-Atlantic Scorecard — April 2021," Brookings, last modified 2021-04-27, https://www.brookings.edu/research/trans-atlantic-scorecard-april-2021/.
```

*Advanced Usage (Cont'd from Basic)*

```python
# Adding the optional type paramater to define what citation
# format is outputted when the __str__() method is called.

c_advanced = Citation(URL="https://www.brookings.edu/research/trans-atlantic-scorecard-april-2021/", type="APA")

# The type parameter is a string, and can either be:
    # "MLA" (default)
    # "APA"
    # "CHI"

# Printing Citation Object
print(c_advanced)
```

Output:
```
Wright, T. (2021, 04-27) Trans-Atlantic Scorecard — April 2021. Brookings. https://www.brookings.edu/research/trans-atlantic-scorecard-april-2021/
```

## Known issues
- Errors with date formatting
- Errors getting multiple authors