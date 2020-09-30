primes = [2,3,5,7]

for num in range(3,100000,2):
    if all(num%x != 0 for x in primes):
        primes.append(num)
primestring = ''.join([str(n) for n in primes])
def solution(i):
    answer = primestring[i:i+5]
    return answer
print(solution(0))
