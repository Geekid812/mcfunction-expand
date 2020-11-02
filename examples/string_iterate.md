The mcfunction-expand compiler does not consider strings as iterables. If you want to force it to, you can turn the string into a list.

### Input
```
say *('Bees!')*

say *(list('Bees!'))*
```

### Result
```mcfunction
say Bees!

say B
say e
say e
say s
say !
```