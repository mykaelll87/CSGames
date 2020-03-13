directions = [(1,-1), (1, 0), (1,1), (0,1)]
def solve(numbers):
  maxNum = -1
  for i in range(len(numbers)):
    for j in range(len(numbers[i])):
      for di, dj in directions:
        if i +3*di >= len(numbers) or j + 3*dj >= len(numbers[i]) or j + 3*dj < 0:
          continue

        s = numbers[i][j] * numbers[i+di][j+dj] * numbers[i+2*di][j+2*dj] * numbers[i+3*di][j+3*dj]
        maxNum = max(maxNum, s)

  
  return maxNum        
  

if __name__ == "__main__":
    lines = open('./input.txt').readlines()
    
    numbers = list(map(lambda l: list(map(int,l.split())), lines))

    print(solve(numbers))