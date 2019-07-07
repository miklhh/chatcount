#!/usr/bin/env python3
import json
import zipfile
import os
import re
import sys
import shutil

TMP_DIR = '__tmp_chatcount__'
MESSAGE_DIR = TMP_DIR + '/messages/inbox'
MESSAGE_JSON_NAME = 'message_1.json'

def iso8859_to_utf8(string):
    return str(string.encode('iso-8859-1').decode('utf-8'))

def usage():
    ''' Prints program usage. '''
    print('Usage: ', end="")
    print(str(sys.argv[0]) + ' <facebook_json_zipfile>')
    regex = re.compile('.*\\.zip')
    matches = [string for string in os.listdir('.') if re.match(regex, string)]
    print('Potential zipfiles in this directory: ')
    if not matches:
        print('    None.')
    else:
        for match in matches:
            print('    ', end="")
            print(str(match))

def open_and_unzip(input_file_name, output_directory_name):
    ''' Open and extract the content of a facebook JSON zip file.'''
    zip_handle = zipfile.ZipFile(input_file_name, 'r')
    zip_handle.extractall(output_directory_name)
    zip_handle.close()

def parse_json(file_name):
    ''' Open and parse a facebook message JSON file. '''
    with open(file_name, 'r') as file_handle:
        return json.loads(file_handle.read())

def count_characters(json_data):
    ''' Returns amount of characters in messages from a message JSON file. '''
    res = 0
    conversation = json_data['messages']
    for message in conversation:
        if 'content' in message:
            res += len(message['content'])
    return res

def main():
    ''' Entry point. '''
    # Print usage or extract provided filename.
    if len(sys.argv) != 2:
        usage()
        exit()
    zip_filename = sys.argv[1]

    # Unzip all content to a tmp directory.
    try:
        print("Unziping content of '" + zip_filename + "' to '" + TMP_DIR + "' directory.")
        open_and_unzip(zip_filename, TMP_DIR)
    except zipfile.BadZipfile:
        print("Error while extracting zipfile.")
        exit()
    except FileNotFoundError:
        print("Error opening zipfile.")
        exit()

    # Parse each individual file.
    result = []
    for filename in os.listdir(MESSAGE_DIR):
        full_filename = MESSAGE_DIR + '/' + filename + '/' + MESSAGE_JSON_NAME
        if os.path.isfile(full_filename):
            json_data = parse_json(full_filename)
            chat_title = json_data['title']
            message_count = len(json_data['messages'])
            character_count = count_characters(json_data)
            result.append((chat_title, message_count, character_count))

    # Sort result after character count.
    result.sort(key=lambda x: x[1])

    # Print the result.
    print('Result:')
    rank = 1
    for (chat_title, message_count, character_count) in reversed(result):
        print('  (' + str(rank) + ')', end=" ")             # Rank
        print(iso8859_to_utf8(chat_title) + " -", end=" ")  # Chat title
        print("Messages: " + str(message_count), end=", ")  # Message count
        print("Characters: " + str(character_count))        # Character count
        rank += 1

    # Remove tmp directory.
    print("Removing '" + TMP_DIR + ".")
    shutil.rmtree(TMP_DIR)

main()
