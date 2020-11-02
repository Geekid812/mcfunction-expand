### Syntax
`range(start, stop, step)`
```py
range(0, 20, 2) # This returns [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```
Note: `stop` is always omitted! (The range actually ends at `stop - 1`)

### Input
```
execute as @a if score @s Points matches *(minimum = range(0, 100, 25))*..*(maximum = [item + 24 for item in minimum])* run say Your Rank: *(ranks = ['D','C','B','A'])*
```

### Result
```mcfunction
execute as @a if score @s Points matches 0..24 run say Your Rank: D
execute as @a if score @s Points matches 25..49 run say Your Rank: C
execute as @a if score @s Points matches 50..74 run say Your Rank: B
execute as @a if score @s Points matches 75..99 run say Your Rank: A
```