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
        entries = data_thumbnails["log"]["entries"]

        # make a list of all urls in the dictionary
        for entry in entries:
            url_list.append(entry["request"]["url"])

    return url_list


def get_page(page_url):

    # perform a GET request to download the png image and wait 1 second to not "overload" the server
    image_page = requests.get(page_url, time.sleep(1))

    return image_page


def save_image(image_page, book_number):

    # define the image filename by using only the 192_1570219750.png part of the URL
    image_filename = image_page.url.split(book_number + "/")[1]
    print("Downloading and saving page named {}".format(image_filename.strip(".png")))
    # save the downloaded image to file
    with open(book_number + "/" + image_filename, "wb") as image_file:
        image_file.write(image_page.content)


def main():

    # define the filename where the bulk information is found
    json_file = "list_requests.json"

    book_number = "736"

    # make directory to save book if it does not exist
    if not os.path.exists(book_number):
        os.makedirs(book_number)

    # parse the file and create a list of urls to get the thumbnails
    url_list = parse_json(json_file)

    # use the below URL as initial test
    # url_list = ["https://www.iplusinteractif.com/storage/assets-prod/book_content/736/thumbs/192_1570219750.png"]

    # loop through the list of URLs
    for url in url_list:
        # if the URL contains /thumbs, process it
        if book_number + "/thumbs/" in url:
            # replace the thumbs/ by nothing to create the URL corresponding to the full size image
            page_url = url.replace("thumbs/", "")
            # function to make the request to get the image
            image_page = get_page(page_url)
            # function to save the image
            save_image(image_page, book_number)


# run the main function if the library is invoked from the command prompt
# $ python soso.py will execute what is described in the main function
if __name__ == "__main__":
    main()
