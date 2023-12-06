from hash_table import HashTable

table = HashTable(capacity=1)
for i in range(20):
    num_pairs = len(table)
    num_empty = table.capacity - num_pairs
    print(f"{num_pairs}/{table.capacity}:", ("X" * num_pairs) + ("." * num_empty))
    table[i] = i
