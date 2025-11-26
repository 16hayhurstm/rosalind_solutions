def main():
    with open("TREE/rosalind_tree.txt") as f:
       
        lines = [line.strip() for line in f if line.strip()]
    
    n = int(lines[0])        # nodes
    m = len(lines) - 1       # edges
    
   
    print(n - 1 - m)

if __name__ == "__main__":
    main()

