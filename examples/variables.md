Variables are saved globally for each file, so you can access them from different lines!

### Input
```
execute store result score Player*(players = [1, 2, 3])* Progress run bossbar get example:player_*(players)* value
execute if score Player*(players)* Progress matches 100.. run say The winner is player *(players)*!
```

### Result
```mcfunction
execute store result score Player1 Progress run bossbar get example:player_1 value
execute store result score Player2 Progress run bossbar get example:player_2 value
execute store result score Player3 Progress run bossbar get example:player_3 value
execute if score Player1 Progress matches 100.. run say The winner is player 1!
execute if score Player2 Progress matches 100.. run say The winner is player 2!
execute if score Player3 Progress matches 100.. run say The winner is player 3!
```