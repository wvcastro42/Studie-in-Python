"""
Split the string into pairs of two characters. If the string contains an odd number of characters, then the missing second character of the final pair should be replaced with an underscore ('_').

Input: A string.
Output: An iterable of strings.

split_pairs('abcd') == ['ab', 'cd']
split_pairs('abc') == ['ab', 'c_']

Precondition: 0<=len(str)<=100"""

a = 'asdf gggggggg aaa'
print(a.split(' ', len(a)//2))
