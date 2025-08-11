from stats import get_book_text
from stats import counting_ants
from stats import print_statement
import sys
def main():
    if len(sys.argv) == 2:
        
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print("Found",(get_book_text(sys.argv[1])),"total words")
        print("--------- Character Count -------")
        print(print_statement(counting_ants(sys.argv[1]))) 
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
main()