from prettytable import PrettyTable
# doc: https://code.google.com/archive/p/prettytable/wikis/Tutorial.wiki

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Charmander", "Squirtle"])
table.add_column("Type", ["Electric", "Fire", "Water"])

print(table)
