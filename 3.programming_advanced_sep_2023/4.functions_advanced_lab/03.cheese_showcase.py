# White a function called sorting_cheeses that receives keywords arguments:
# •	The key represents the name of the cheese
# •	The value is a list of quantities (integers) of the pieces of the given cheese
# The function should return the cheeses and their pieces' quantities sorted by the number of pieces of a cheese kind in
# descending order. If two or more cheeses have the same number of pieces, sort them by their names in ascending order
# (alphabetically). For each kind of cheese, return their piece quantities in descending order.
# For more clarifications, see the examples below.
# Input1:
# print(
#     sorting_cheeses(
#         Parmesan=[102, 120, 135],
#         Camembert=[100, 100, 105, 500, 430],
#         Mozzarella=[50, 125],
#     )
# )
#
# Output1:
# Camembert
# 500
# 430
# 105
# 100
# 100
# Parmesan
# 135
# 120
# 102
# Mozzarella
# 125
# 50
#
# Input2:
# print(
#     sorting_cheeses(
#         Parmigiano=[165, 215],
#         Feta=[150, 515],
#         Brie=[150, 125]
#     )
# )
#
# Output2:
# Brie
# 150
# 125
# Feta
# 515
# 150
# Parmigiano
# 215
# 165

def sorting_cheeses(**kwargs):
    sorted_dict = sorted(kwargs.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    result = ""

    for name, quantities in sorted_dict:
        result += f"{name}\n"
        sorted_quantities = sorted(quantities, reverse=True)
        result += "\n".join([str(el) for el in sorted_quantities])
        result += "\n"

    return result

print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
