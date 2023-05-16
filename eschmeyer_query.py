# -*- coding: utf-8 -*-
"""
Created on Tue May 16 16:51:38 2023

@author: John Whalen
"""


# input file with potential scientific names
import requests, mechanicalsoup, re, os, sys, time
from bs4 import BeautifulSoup


def scrape_species_info(field_id):
    # URL for searching the species
    search_url = 'https://researcharchive.calacademy.org/research/ichthyology/catalog/fishcatmain.asp'

    # Send a POST request with the scientific name as data
    response = requests.post(search_url, data={'GenusSpecies': field_id})

    # Parse the response using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the relevant information on the page
    input_species_id = soup.find('Species, Genus')
    current_status = soup.find('font', text='Current Status:').next_sibling.strip()
    eschmeyer_id = soup.fin('font', text=)
    distribution = soup.find('font', text='Distribution:').next_sibling.strip()


    # Return the retrieved information
    return input_species_id, current_status, distribution

# Read input file and process each scientific name
#input_file = print()
input_file = 'all_spp_1978.txt'
output_file = 'all_spp_1978_eschmeyer.txt'

with open(input_file, 'r') as file:
    with open(output_file, 'w') as output:
        for line in file:
            field_id = line.strip()

            # Skip empty lines or comments
            if not field_id or field_id.startswith('#'):
                continue

            # Scrape the species information
            current_status, distribution = scrape_species_info(field_id)

            # Write the information to the output file
            output.write(f'Scientific Name: {field_id}\n')
            output.write(f'Current Status: {current_status}\n')
            output.write(f'' {}
            output.write(f'Distribution: {distribution}\n')
            output.write('\n')


# layers to query the search bar of the catalog for valid scientific names




"""
From famfetcher.py

Family = input('Enter the name of the family:')# apogonidae
PathName = input('Enter the full pathway for the working directory: ')# /Users/ivanlopez/Desktop/Daily_Work/Practical_computing/test/
StartTime = time.time()
Today = date.today()
Day = Today.strftime('%b-%d-%Y')
os.chdir(PathName)
RawFileName = Family + 'raw.txt'
RawFile = open(RawFileName, 'w')
Browser = mechanicalsoup.StatefulBrowser()
Browser.open("https://researcharchive.calacademy.org/research/ichthyology/catalog/fishcatmain.asp")
Browser.select_form()
Browser.get_current_form()#.print_summary()
Browser["contains"] = Family
Response = Browser.submit_selected()
Soup = BeautifulSoup(Response.text, 'html.parser')
RawFile.write(Soup.get_text())
Lines = open(RawFileName).readlines()
open(RawFileName, 'w').writelines(Lines[87:-1])
"""

# output file with field_id, current_status, eschmeyer_id, distribution




