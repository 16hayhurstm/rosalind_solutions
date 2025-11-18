def main():
    with open("TREE/rosalind_tree.txt") as f:
        # read all non-empty lines
        lines = [line.strip() for line in f if line.strip()]
    
    n = int(lines[0])        # number of nodes
    m = len(lines) - 1       # edges = number of remaining lines
    
    # A tree on n nodes has n-1 edges → missing edges = (n-1 - m)
    print(n - 1 - m)

if __name__ == "__main__":
    main()

