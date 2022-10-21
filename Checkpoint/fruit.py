
def main():
    try:
        # Create and print a list named fruit.
        fruit_list = ["pear", "banana", "apple", "mango"]
        print(f"original: {fruit_list}")

        fruit_list.reverse()
        print(f"reversed: {fruit_list}")

        fruit_list.append("orange")
        print(f"oranged: {fruit_list}")

        j = fruit_list.index("apple")
        print(f"apple: {j}")
        fruit_list.insert(j, "cherry")
        print(f"cherry: {fruit_list}")

        fruit_list.remove("banana")
        print(f"removed banana: {fruit_list}")

        last = fruit_list.pop()
        print(f"popped: {fruit_list}......{last}")

        fruit_list.sort()
        print(f"sorted: {fruit_list}")

        fruit_list.clear()
        print(f"cleared: {fruit_list}")
    
    except IndexError as ind_err:
        print(type(ind_err).__name__, ind_err, sep=": ")

if __name__ == "__main__":
        main()