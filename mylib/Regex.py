'''
https://docs.python.org/3/library/re.html
##################
Special characters
##################
\       escape special characters
.       matches any character
^       matches beginning of string
$       matches end of string
[5b-d]  matches any chars '5', 'b', 'c' or 'd'
[^a-c6] matches any char except 'a', 'b', 'c' or '6'
R|S     matches either regex R or regex S
()      creates a capture group and indicates precedence

#################
Quantifiers
##################
*       0 or more (append ? for non-greedy)
+       1 or more (append ? for non-greedy)
?       0 or 1 (append ? for non-greedy)
{m}     exactly mm occurrences
{m, n}  from m to n. m defaults to 0, n to infinity
{m, n}? from m to n, as few as possible

###################
Special sequences
###################
\A      start of string
\b      matches empty string at word boundary (between \w and \W)
\B      matches empty string not at word boundary
\d      digit
\D      non-digit
\s      whitespace: [ \t\n\r\f\v]
\S      non-whitespace
\w      alphanumeric: [0-9a-zA-Z_]
\W      non-alphanumeric
\Z      end of string
\g<id>  matches a previously defined group
'''
import re
print(re.search('^\+\d{1,3}-\d{9,11}$', '+123-12345678'))
print(re.search('^(\+\d{1,3})-(\d{9,11})$', '+123-123456789').group(2))
print(re.sub('^\+\d{1,3}-\d{9,11}$', 'x', '+123-12345678'))
print(re.sub('^\+\d{1,3}-\d{9,11}$', 'x', '+123-123456789'))


