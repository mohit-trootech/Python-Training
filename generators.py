"""Python Example to Understand Generators"""
import random


def generate_random_words(lines: int) -> str:
    """
    function to Generate Random Content for file using random module
    @param lines: int
    @return: str
    """
    words = ["Banana ", "Watermelon ", "Melon ", "Mango ", "Cherry ", "Chocolates ", "Coffee ", "Tea "]
    content = ""
    for line in range(lines):
        for word in range(random.randint(1, 10)):
            content += random.choice(words)
        content += "\n"
    return content


def create_file_content(content: str) -> None:
    """
    function to write file content
    @param content: str
    @return: None
    """
    with open("file", "w") as f:
        f.write(content)


def read_file_content() -> str:
    """
    function to yield file content
    @return: str
    """
    with open("file", "r") as f:
        for lines in f:
            yield lines


c = generate_random_words(100)
create_file_content(c)
file_content = read_file_content()
while True:
    try:
        choice = input("Press Any Key to ReadLine or q to Exit: ")
        if choice.lower() != 'q':
            print(next(file_content))
        else:
            print("Stop Reading File")
            break
    except StopIteration:
        print("File END")
        break
