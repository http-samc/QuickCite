# citer
 An API Wrapper for automatic MLA citations

## How To Use:

### As a Code Utility
*Requires that the ``Requests`` and ``Json`` packages are installed*
1. Import the ``cite`` class from ``citer``. \
*Example:* ``from citer import cite``
2. Create a ``cite`` object with the URL as a parameter. \
*Example:* ``citation = cite("https://www.npr.org/2019/04/10/709490855/github-has-become-a-haven-for-chinas-censored-internet-users")``
3. Call the ``mla`` method on ``citation`` \
*Example:* ``print(citation.mla())``

*Output Value:* \
Feng, Emily. "GitHub Has Become A Haven For China’s Censored Internet Users" NPR, 2019-04-10, https://www.npr.org/2019/04/10/709490855/github-has-become-a-haven-for-chinas-censored-internet-users. Accessed 15/2/2021.

### As a GUI tool

1. Download the latest release of citer from this repository.
2. Start the ``citer.exe`` program.
3. Enter the webpage URL in the entry box.
4. Click ``Start``.
5. A popup with your MLA citation will open. This is a gui wrapper for the ``cite`` class.
6. Click out of your popup and enter another URL, or end the program.

## TODO
1. Improve collection (some sites like Reuters do not work).