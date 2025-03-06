def main():
    data_list = [
        "Hi",
        "How are you",
        "I'm normal"
    ]
    write_text_file("polly_the_pirate.txt", data_list)
    print(read_text_file("polly_the_pirate.txt"))

def read_text_file(filename):
    with open(filename, "rt") as file:
        data = file.readlines()
        for i, line in enumerate(data):
            data[i] = line.strip()
        return data

def write_text_file(filename, data_list):
    with open(filename, "wt") as file:
        for line in data_list:
            file.write(line + "\n")

if __name__ == "__main__":
    main()