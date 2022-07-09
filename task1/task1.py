import requests
import xml.etree.ElementTree as ET


def task1_solution():
    r = requests.get('https://coding-academy.pl/all_customers')
    if r.status_code == 200:
        root = ET.fromstring(r.text)
        with open("task1_solution.txt", "wt") as file:
            for child in root:
                if child.tag == "customer":
                    file.write(child.text + "\n")

if __name__ == '__main__':
    task1_solution()