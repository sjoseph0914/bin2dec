# this program converts binary to decimal numbers 
def bin2dec(num): 
  result = 0
  for index in range(len(num)):
    digit = num[index] 
    if digit == "1":
      result = result + pow(2,len (num)-index-1) 
  return result
  