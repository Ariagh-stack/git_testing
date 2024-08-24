# def main():
#     with open("txt.output", "a") as file:
#         while True:
#             user_input = input("Enter text (type 'exit' to quit): ")
#             if user_input.lower() == 'exit':
#                 break
#             file.write(user_input + "\n")
#
#
# if __name__ == "__main__":
#     main()

# ------------------------------------------------------------------

# def remove_extra_spaces(line):
#     """Remove extra spaces between words in a line."""
#     return ' '.join(line.split())
#
# def main():
#     try:
#         with open("txt.data", "r") as file:
#             for line in file:
#                 cleaned_line = remove_extra_spaces(line)
#                 print(cleaned_line)
#     except FileNotFoundError:
#         print("The file 'txt.data' does not exist.")
#
#
# if __name__ == "__main__":
#     main()

# -------------------------------------------------------------------

# import re
# from collections import Counter


# def count_words_in_file(filename):
#     """Count the occurrences of each word in a given file."""
#     with open(filename, "r") as file:
#         # Read contents of the file
#         text = file.read()
#         # Use regex to find all words (case insensitive)
#         words = re.findall(r'\b\w+\b', text.lower())
#
#         # Count the occurrences of each word
#         word_count = Counter(words)
#
#         return word_count
#
#
# def main():
#     filename = "txt.sample"
#     try:
#         word_count = count_words_in_file(filename)
#         # Print each word and its count
#         for word, count in word_count.items():
#             print(f"{word}: {count}")
#     except FileNotFoundError:
#         print(f"The file '{filename}' does not exist.")
#
#
# if __name__ == "__main__":
#     main()

# ------------------------------------------------------------------

# def copy_file(source, destination):
#     """Copy the contents of the source file to the destination file."""
#     try:
#         with open(source, "r") as src_file:
#             with open(destination, "w") as dest_file:
#                 # Read and write the contents line by line
#                 for line in src_file:
#                     dest_file.write(line)
#         print(f"Contents of '{source}' have been copied to '{destination}'.")
#     except FileNotFoundError:
#         print(f"One of the files '{source}' or '{destination}' does not exist.")
#     except IOError as e:
#         print(f"An error occurred: {e}")
#
# def main():
#     source_filename = "txt.source"
#     destination_filename = "txt.destination"
#     copy_file(source_filename, destination_filename)
#
# if __name__ == "__main__":
#     main()

# ---------------------------------------------------------------------

# def append_to_file(filename):
#     """Append lines of text to a file until an empty line is entered."""
#     try:
#         with open(filename, "a") as file:  # Open the file in append mode
#             while True:
#                 line = input("Enter a line of text (or press Enter to finish): ")
#                 if line == "":
#                     break  # Exit the loop if the input is an empty line
#                 file.write(line + "\n")  # Write the line to the file with a newline
#         print(f"Text has been appended to '{filename}'.")
#     except IOError as e:
#         print(f"An error occurred: {e}")
#
# def main():
#     filename = "txt.notes"
#     append_to_file(filename)
#
# if __name__ == "__main__":
#     main()

# ------------------------------------------------------------------------

# def calculate_sum_and_average(filename):
#     """Read integers from a file and calculate their sum and average."""
#     try:
#         with open(filename, "r") as file:
#             numbers = []
#             for line in file:
#                 # Convert the line to an integer and append to the list
#                 numbers.append(int(line.strip()))
#
#         if numbers:
#             total_sum = sum(numbers)
#             average = total_sum / len(numbers)
#             print(f"Sum: {total_sum}")
#             print(f"Average: {average}")
#         else:
#             print("The file is empty or contains no valid numbers.")
#
#     except FileNotFoundError:
#         print(f"The file '{filename}' does not exist.")
#     except ValueError:
#         print("The file contains non-integer values.")
#     except IOError as e:
#         print(f"An error occurred: {e}")
#
#
# def main():
#     filename = "txt.numbers"
#     calculate_sum_and_average(filename)
#
#
# if __name__ == "__main__":
#     main()

# -----------------------------------------------------------------------

# def replace_in_file(input_filename, output_filename, search_word, replace_word):
#     """Read a file, replace occurrences of a word, and write to a new file."""
#     try:
#         with open(input_filename, "r") as file:
#             content = file.read()  # Read the entire content of the file
#
#         updated_content = content.replace(search_word, replace_word)  # Replace the search word with the replace word
#
#         with open(output_filename, "w") as new_file:
#             new_file.write(updated_content)  # Write the updated content to the new file
#
#         print(f"Updated content saved to '{output_filename}'.")
#
#     except FileNotFoundError:
#         print(f"The file '{input_filename}' does not exist.")
#     except IOError as e:
#         print(f"An error occurred: {e}")
#
#
# def main():
#     input_filename = "txt.document"
#     output_filename = "txt.document_updated"
#
#     search_word = input("Enter the word to search for: ")
#     replace_word = input("Enter the word to replace it with: ")
#
#     replace_in_file(input_filename, output_filename, search_word, replace_word)
#
#
# if __name__ == "__main__":
#     main()

# ---------------------------------------------------------------------------

# import os
#
# def delete_file(filename):
#     """Delete a file if it exists."""
#     try:
#         if os.path.exists(filename):
#             os.remove(filename)  # Delete the file
#             print(f"The file '{filename}' has been deleted.")
#         else:
#             print(f"The file '{filename}' does not exist.")
#     except Exception as e:
#         print(f"An error occurred while trying to delete the file: {e}")
#
#
# def main():
#     filename = "txt.delete_to_file"
#     delete_file(filename)
#
#
# if __name__ == "__main__":
#     main()

# ---------------------------------------------------------------------------
