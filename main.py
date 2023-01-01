if __name__ != "__main__":
  exit(1)

from br import br 
from clear import clear

clear()

print("Input your numbers separated by spaces. > ")

nums = [int(i) for i in input().split()]

br() # ==================================================

print("Sorting array...")

nums = sorted(nums)

hi = nums.index(max(nums))
lo = nums.index(min(nums))

print(f"Done! New array => {' '.join([str(i) for i in nums])}")

br() # ==================================================

print("What number you want to find? > ")
toFind = int(input())
found: int = None

br() # ==================================================

pointer: int = None

while True:
  pointer = round((hi + lo) / 2)
  print(f"Pointer: I={pointer} V={nums[pointer]}")

  if nums[pointer] < toFind:
    lo = pointer
    print(f"New low: {nums[lo]} at index {lo}")

  elif nums[pointer] > toFind:
    hi = pointer
    print(f"New high: {nums[hi]} at index {hi}")

  elif nums[pointer] == toFind:
    found = nums[pointer]
    print(f"Found {found} at index {nums.index(found)} (sorted).")
    break
