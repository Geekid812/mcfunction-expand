[![GitHub](https://img.shields.io/github/license/geekid812/mcfunction-expand?style=for-the-badge)](https://github.com/geekid812/mcfunction-expand)

[![Twitter Follow](https://img.shields.io/twitter/follow/geekid812?style=social)](https://twitter.com/geekid812)
[![Discord](https://img.shields.io/discord/760194844001304616?logo=discord&style=social)](https://discord.gg/mHnjK8K)

# MCFunction Expand
A Minecraft Function compiler which aims to reduce time writing duplicate code.

mcfunction-expand is a CLI tool that compiles `.mcfunction` files. It can evaluate Python code and clone multiple lines with different arguments.

## Installation
Python version **3.8** or higher is required.
```
# Clone the repisory into your working directory
git clone https://github.com/geekid812/mcfunction-expand

# Install dependencies
pip install -r mcfunction-expand/requirements.txt

# Rename the directory
ren mcfunction-expand expand

# Show the CLI help message
python expand --help
```

## Usage
Compiling a single file:
```
python expand path/to/file.mcfunction
```
Watching the current directory for file changes:
```
python expand --watch
```
To prevent mcfunction-expand from compiling a specific file, add this comment at the top of said file:
```py
# NO-EXPAND
```

## Example
mcfunction-expand will evaluate Python code written as such: `*(YOUR CODE HERE)*`.
If the evaluation returns an iterable (except for strings), the line will be cloned for as many items it contains.

```
execute as @a[team=*(teams = ['red','blue','green','yellow'])*] run say I am in team *(teams)*!
```
will compile to
```mcfunction
execute as @a[team=red] run say I am in team red!
execute as @a[team=blue] run say I am in team blue!
execute as @a[team=green] run say I am in team green!
execute as @a[team=yellow] run say I am in team yellow!
```

See the `examples` directory for more examples on how to use the compiler!