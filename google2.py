def solution(xs):
  sol = 1
  counter = 0
  tmp = float("-inf")
  for i in xs:
    if i > 0:
      sol *= i
      counter += 1
    if i < 0:
      if i > tmp:
          tmp = i
      sol *= i
      counter += 1
  if sol < 0 and counter != 1:
    sol = sol // tmp
  if counter == 0 or (sol < 0 and counter == 1):
    sol = 0
  return str(sol)