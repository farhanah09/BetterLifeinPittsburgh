'''

Authors: Farhan Ahmad, Keyi Chai, Luyi Sun, Harish Balaji, Yikun Yang

'''
import requests
from bs4 import BeautifulSoup
import re
import csv
import pandas as pd
from pandasgui import show

def collegepadsscraping():
    Main_Url = "https://www.rentcollegepads.com/off-campus-housing/carnegie-mellon/search"

    page = requests.get(Main_Url)

    soup = BeautifulSoup(page.content, 'html.parser')

    urls = []

    ### EXTRACTING THE URLS OF THE PROPERTIES FROM THE MAIN PAGE WITH PROPERTY LISTINGS 
    apartment_type = soup.find("main")
    for h in soup.findAll('h3', attrs={'class':'ellipsis'}):
        a = h.find('a')
        try: 
            if 'href' in a.attrs:
                url = a.get('href')
                urls.append(url)
        except:
            pass

    ##CREATING CSV FILE TO STORE DATA ###
    f = open("RentCollegePad_live.csv","w", newline='') #change to your specific path if doesn't work
    writer = csv.writer(f)
    writer.writerow(("Name", "Address","Rent", "Bedroom","Bathroom", "Property Features"))
    f.close()


    #### START OF FUNCTION ####
    ### IT TAKES IN A URL AND EXTRACTS DATA FROM IT
        
    def func(a):
            url = a
            page = requests.get(url)

            soup = BeautifulSoup(page.content, 'html.parser')

            apartment_type = soup.find("main")

            head = []
            addr = []
            rows = []
            result = []

            ##EXTRACT APARTMENT NAME
            p_tags = soup.select('h1')
            for p_tag in p_tags:
                head.append(p_tag.get_text(strip=True))

            ##EXTRACT APARTMENT ADDRESS
            p_tags = soup.select('span[class="sub-heading"]')
            for p_tag in p_tags:
                addr.append(p_tag.get_text(strip=True))

            price = None

            ##EXTRACT Name-Bed-Bath-Rent-Sqft-Available?          
            table = soup.find('table')
            for row in table.find_all('td'):
                rows.append(re.sub("\<td\>|\</td\>","", str(row)))
                try:
                        price = re.search(r'\$(\d+)(\.|-)', str(row)).group(0)[1:-1]   ##EXTRACTING ONLY PRICE
                except:
                    continue
            

            ##EXTRACT UTILITIES 1
            p_tags = soup.select('div.feature-block div[class="extra-feature"] div[id="collapse-1"] li')
            for p_tag in p_tags:
                result.append(p_tag.get_text(strip=True))


            ##EXTRACT UTILITIES 2
            p_tags = soup.select('div.feature-block div[class="extra-feature"] div[id="collapse-2"] li')
            for p_tag in p_tags:
                result.append(p_tag.get_text(strip=True))


            ##EXTRACT UTILITIES 3
            p_tags = soup.select('div.feature-block div[class="extra-feature"] div[id="collapse-3"] li')
            for p_tag in p_tags:
                result.append(p_tag.get_text(strip=True))


            del rows[0:4] # To remove data that is not required
            rows = rows[2:]

            # Joining the list elements to a single variable
            bname = "".join(head)   # Property Name
            baddr = " ".join(addr)  # Propert Address
            bed = str(rows[1][2:])  # Number of Bedrooms
            bath = str(rows[3][2:]) # Number of Bathrooms
            butil = ",".join(result) # Property Features
            
            
            # APPENDING VALUES FOR EACH PROPERTY TO NEW ROW IN THE CSV FILE
            f = open("RentCollegePad_live.csv","w", newline='') #change to your specific path if doesn't work
            writer = csv.writer(f)
            writer.writerow((bname,baddr,price,bed,bath,butil))
            f.close()

    ### END OF FUNCTION ###

    ## PASSING THE URL OF EACH PROPERTY TO THE FUNCTION
    for i in urls:
        func(i)
