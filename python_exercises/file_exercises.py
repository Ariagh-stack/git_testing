# number = 3.14159
# print(f"{number:.2f}")


# def main():
#     # Open the file in write mode
#     with open("txt.output", "a") as file:  # Use 'a' to append or 'w' to overwrite
#         while True:
#             user_input = input("Please enter something (type 'exit' to quit): ")
#             if user_input.lower() == 'exit':
#                 print("Exiting the program.")
#                 break
#             file.write(user_input + '\n')
#
# if __name__ == "__main__":
#     main()

# ------------------------------------------------------------

# def clean_and_print_file_contents(filename):
#     try:
#         # Open the file in read mode
#         with open("data.txt", 'r') as file:
#             for line in file:
#                 # Remove extra spaces and print the line
#                 cleaned_line = ' '.join(line.split())
#                 print(cleaned_line)
#     except FileNotFoundError:
#         print(f"The file '{filename}' does not exist.")
#
# if __name__ == "__main__":
#     clean_and_print_file_contents("txt.data")

# ------------------------------------------------------------

# def copy_file_contents(source_filename, destination_filename):
#     try:
#         # Open the source file in read mode
#         with open(source_filename, 'r', encoding='utf-8') as source_file:
#             # Read the content of the source file
#             content = source_file.read()
#
#             # Open the destination file in write mode
#         with open(destination_filename, 'w', encoding='utf-8') as destination_file:
#             # Write the content to the destination file
#             destination_file.write(content)
#
#         print(f"Contents copied from '{source_filename}' to '{destination_filename}' successfully.")
#
#     except FileNotFoundError:
#         print(f"The file '{source_filename}' does not exist.")
#     except IOError as e:
#         print(f"An error occurred while copying the file: {e}")
#
#
# if __name__ == "__main__":
#     copy_file_contents("txt.source", "txt.destination")

# ------------------------------------------------------------

# def append_lines_to_file(filename):
#     try:
#         # Open the file in append mode
#         with open(filename, 'a', encoding='utf-8') as file:
#             print("Enter your notes (press Enter on an empty line to finish):")
#             while True:
#                 line = input()  # Read a line from the user
#                 if line == "":  # If the line is empty, break the loop
#                     break
#                 file.write(line + '\n')  # Write the line to the file
#
#         print(f"Notes have been added to '{filename}'.")
#
#     except IOError as e:
#         print(f"An error occurred while writing to the file: {e}")
#
# if __name__ == "__main__":
#     append_lines_to_file("txt.notes")

# ------------------------------------------------------------

# def calculate_sum_and_average(filename):
#     try:
#         with open(filename, 'r', encoding='utf-8') as file:
#             numbers = []
#             for line in file:
#                 try:
#                     # Convert the line to an integer and append to the list
#                     number = int(line.strip())
#                     numbers.append(number)
#                 except ValueError:
#                     print(f"Warning: '{line.strip()}' is not a valid integer and will be skipped.")
#
#             if numbers:
#                 total_sum = sum(numbers)
#                 average = total_sum / len(numbers)
#                 print(f"Sum: {total_sum}")
#                 print(f"Average: {average:.2f}")
#             else:
#                 print("No valid numbers to calculate.")
#
#     except FileNotFoundError:
#         print(f"The file '{filename}' does not exist.")
#     except IOError as e:
#         print(f"An error occurred while reading the file: {e}")
#
# if __name__ == "__main__":
#     calculate_sum_and_average("txt.numbers")

# -----------------------------------------------------------------------

# def search_and_replace(filename, new_filename, search_word, replace_word):
#     try:
#         with open(filename, 'r', encoding='utf-8') as file:
#             content = file.read()
#
#             # Replace the search_word with replace_word
#         updated_content = content.replace(search_word, replace_word)
#
#         # Write the updated content to a new file
#         with open(new_filename, 'w', encoding='utf-8') as new_file:
#             new_file.write(updated_content)
#
#         print(f"The word '{search_word}' has been replaced with '{replace_word}' and saved to '{new_filename}'.")
#
#     except FileNotFoundError:
#         print(f"The file '{filename}' does not exist.")
#     except IOError as e:
#         print(f"An error occurred: {e}")
#
#
# if __name__ == "__main__":
#     original_file = "txt.document"
#     updated_file = "txt.document_updated"
#
#     search_word = input("Enter the word to search for: ")
#     replace_word = input("Enter the word to replace it with: ")
#
#     search_and_replace(original_file, updated_file, search_word, replace_word)

# ---------------------------------------------------------------------

# import os
#
# def delete_file(filename):
#     """Deletes the specified file if it exists."""
#     try:
#         # Check if the file exists
#         if os.path.exists(filename):
#             os.remove(filename)  # Delete the file
#             print(f"The file '{filename}' has been deleted.")
#         else:
#             print(f"The file '{filename}' does not exist.")
#     except Exception as e:
#         print(f"An error occurred: {e}")
#
# if __name__ == "__main__":
#     file_to_delete = "txt.delete_to_file"
#     delete_file(file_to_delete)

# ---------------------------------------------------------------------