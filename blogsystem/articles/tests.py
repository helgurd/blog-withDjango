def substring_copy(b, n):
  flen = 2
  if flen > len(b):
    flen = len(b)
  substr = b[:flen]
  
  result = ""
  for i in range(n):
    result = result + substr
  return result
print(substring_copy('abcdef', 2))
print(substring_copy('p', 3));