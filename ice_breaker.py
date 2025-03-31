from dotenv import load_dotenv
import os

# Checks if the script is being run directly (as opposed to being imported as a module in another script). If it is being run directly, the code block under this condition will execute.
if __name__ == "__main__":
    load_dotenv()
    print("Hello Langchain!!")

    try:
        print(os.environ["COOL_API_KEY"])
        print(os.environ["OPENAI_API_KEY"])
    except KeyError as e:
        print(f"Error: Missing environment variable {e}")
