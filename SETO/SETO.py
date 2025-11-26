def parse_set(s):
    # convert to list from strigng
    s = s.strip().strip("{}")
    if not s:
        return set()
    return set(map(int, s.split(",")))

input_file = "SETO/rosalind_seto.txt"
output_file = "output.txt"

# --- Read input ---
with open(input_file) as f:
    n = int(f.readline().strip())
    A = parse_set(f.readline().strip())
    B = parse_set(f.readline().strip())


U = set(range(1, n + 1))


results = [
    A | B,      # union
    A & B,      # intersection
    A - B,      # A minus B
    B - A,      # B minus A
    U - A,      # complement of A
    U - B       # complement of B
]

# save to a file 
with open(output_file, "w") as out:
    for i, r in enumerate(results):
        formatted = "{" + ", ".join(map(str, sorted(r))) + "}"
        if i < len(results) - 1:
            out.write(formatted + "\n")
        else:
            out.write(formatted) 

print(f"Saved output to {output_file}")
