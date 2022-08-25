height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

water = 0

left = 0
right = len(height) - 1

while left < right:
    water = max(water, min(height[left], height[right]) * (right - left))
    if height[left] <= height[right]:
        left += 1
    else:
        right -= 1

print(water)
