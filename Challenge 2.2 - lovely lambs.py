def solution(total_lambs):

  doubledlist = list()

  x = 0
  runningtotal = 0
  while x <= total_lambs:
    currentvalue = 2**x
    doubledlist.append(currentvalue)
    runningtotal = runningtotal + currentvalue
    if runningtotal > total_lambs:
      break
    x = x + 1

  fiblist = [1,1]
  Frunningtotal = 2
  y = 2
  while y <= total_lambs:
    currentvalue2 = fiblist[y-1] + fiblist[y-2]
    fiblist.append(currentvalue2)
    Frunningtotal = Frunningtotal + int(fiblist[y])
    if Frunningtotal > total_lambs:
      break
    y = y + 1


  Difference = len(fiblist) - len(doubledlist)
  return Difference

print(solution(143))
