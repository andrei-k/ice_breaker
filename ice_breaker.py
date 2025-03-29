import os

# Checks if the script is being run directly (as opposed to being imported as a module in another script). If it is being run directly, the code block under this condition will execute.
if __name__ == "__main__":
    print("Hello Langchain!")
    print(os.environ["OPENAI_API_KEY"])
