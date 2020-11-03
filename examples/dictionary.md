### Syntax
`my_dict = {'key':'value'}`
```py
polygons = {3: 'triangle', 4: 'square', 5: 'pentagon'}
polygons[4] # This returns 'square'
polygons.values() # This returns ['triangle', 'square', 'pentagon']
```

### Input
```
# Hero Type: *(strength_of_type = {'warrior': 3, 'mage': 1, 'thief': 2})* | Strength: *(strength_of_type.values())*
effect give @a[tag=*(strength_of_type.keys())*] minecraft:strength 60 *(strength_of_type.values())* true
```

### Result
```mcfunction
# Hero Type: warrior | Strength: 3
# Hero Type: mage | Strength: 1
# Hero Type: thief | Strength: 2
effect give @a[tag=warrior] minecraft:strength 60 3 true
effect give @a[tag=mage] minecraft:strength 60 1 true
effect give @a[tag=thief] minecraft:strength 60 2 true
```