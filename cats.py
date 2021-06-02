#!/usr/bin/python3
import requests
from lxml import html
from urllib.error import HTTPError


def main():
    page_number = 0
    try:
        while 1:
            page_number += 1
            url = f'https://www.spca.com/en/adoption/cats-for-adoption/page/{page_number}/'
            page_content = requests.get(url)
            tree = html.fromstring(page_content.content)

            cat_names = tree.xpath('//*[@id="page-main"]/div[4]/div/div[3]/div[*]/a/div[2]/h5/text()')
            cat_info = tree.xpath('//*[@id="page-main"]/div[4]/div/div[3]/div[*]/a/div[2]/div[1]/text()')
            print("===============================")
            print(f"Evaluating page: {page_number}")
            print("===============================")
            for name, info in zip(cat_names, cat_info):
                print(name)
                print(info.strip())
                if "Baby" in info:
                    print("A baby cat is available!")
                    print(f"Hurry! Head over to {url}")
                    print("GO GO GO!")
            if len(cat_names) < 12:
                print("No more pages to evaluate, terminating...")
                break
    except HTTPError:
        print("No more pages to evaluate, terminating...")
    print("Terminated.")


if __name__ == "__main__":
    main()
