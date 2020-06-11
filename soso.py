#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# load the appropriate libraries
import os
import json
import time
import requests


# parse the json file for the urls
def parse_json(json_file):

    # initiate an empty list
    url_list = []

    # read file containing the information
    with open(json_file, "r") as file:

        # load the information as dictionary
        data_thumbnails = json.load(file, strict=False)

        # extract only the entries list from the dictionary
        entries = data_thumbnails["JSON"]

        # make a list of all urls in the dictionary
        for entry in entries:
            # url_list.append(entry["request"]["url"])
            url_list.append(entry["pageImagePath"])

        book_number = url_list[0].split("/")[0]

    return url_list, book_number


def get_page(full_url):

    # perform a GET request to download the png image and wait 1 second to not "overload" the server
    image_page = requests.get(full_url, time.sleep(1))

    return image_page


def save_image(image_page, book_number):

    # define the image filename by using only the 192_1570219750.png part of the URL
    image_filename = image_page.url.split(book_number + "/")[1]
    print("Downloading and saving page named {}".format(image_filename.strip(".png")))
    # save the downloaded image to file
    with open(book_number + "/" + image_filename, "wb") as image_file:
        image_file.write(image_page.content)


def main():

    # define the base url
    base_url = "https://www.iplusinteractif.com/storage/assets-prod/book_content/"

    # define the filename where the bulk information is found
    json_file = "list_requests_test.json"
    # json_file = "list_requests.json"


    # parse the file and create a list of urls to get the thumbnails
    url_list, book_number = parse_json(json_file)

    # make directory to save book if it does not exist
    if not os.path.exists(book_number):
        os.makedirs(book_number)

    for page_url in url_list:
        full_url = base_url + page_url
        image_page = get_page(full_url)
        save_image(image_page, book_number)


# run the main function if the library is invoked from the command prompt
# $ python soso.py will execute what is described in the main function
if __name__ == "__main__":
    main()
