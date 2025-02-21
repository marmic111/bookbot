#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 11:38:17 2025

@author: marmic
"""

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    wordcount = get_num_words(text)
    charcount = get_num_char(text)
    list_of_dict = dict_to_list(charcount)
    sorted_list = sort_dict(list_of_dict)
    report = write_report(book_path, wordcount, list_of_dict)
    #print(charcount)
    #print(list_of_dict)
    #print(report)
    
    
    
def get_book_text(path):
    with open(path) as f:
        return f.read()
        
def get_num_words(text):
    words = text.split()
    return len(words)
  
def get_num_char(text):
    lower_text = text.lower()
    dict_char = {}
    for char in lower_text:
      if char not in dict_char:
        dict_char[char] = 1
      else:
        dict_char[char] += 1
    return dict_char


def dict_to_list(charcount):
    list_of_dict = []
    for key in charcount:
      list_of_dict.append(
        {"character" : key,
        "count" : charcount[key]}
      )
    return list_of_dict

def sort_on(list_of_dict):
    return list_of_dict["count"]
  
def sort_dict(list_of_dict):
  list_of_dict.sort(reverse = True, key = sort_on)
  return list_of_dict

def write_report(book_path, wordcount, list_of_dict):
    print(f"----- Begin report of {book_path} -----\n")
    print(f"{wordcount} words found in the document\n")
    
    for char in list_of_dict:
      if char["character"].isalpha():
        print(f"The '{char['character']}' character was found {char['count']} times")
      
    print ("\n----------- End report -----------")


if __name__ == "__main__":
    main()

    

