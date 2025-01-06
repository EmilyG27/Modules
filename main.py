import mood_responses
import text_utils

def main():
        mood = input("How are you feeling? ")
        print(mood_responses.mood_response(mood))

reverse_message = "Message"
capitalize_message = "message"

print(text_utils.reverse_string(reverse_message))
print(text_utils.capitalize_string(capitalize_message))

if __name__ == "__main__":
    main()

