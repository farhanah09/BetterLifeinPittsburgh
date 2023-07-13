'''

Authors: Farhan Ahmad, Keyi Chai, Luyi Sun, Harish Balaji, Yikun Yang

'''
import pandas as pd
from pandasgui import show
import requests
from bs4 import BeautifulSoup
import re
import csv

def walnutscraping():

    URL = [] ## This is to store the list of urls extracted from Walnut Capital
    # ws = pd.read_csv("D:\CMU_S23\DFP\GroupProject\Interface\walnutcapital_live.csv")
    # show(ws)
    ## Function takes in a main webpage's URL and extracts the individual URLs of each property listed on the website 
    def get_url(a):
            Main_Url =  a 
            page = requests.get(Main_Url)
            soup = BeautifulSoup(page.content, 'html.parser')
            urls = []

            ### EXTRACTING THE URLS OF THE PROPERTIES FROM THE MAIN PAGE WITH PROPERTY LISTINGS 
            for h in soup.findAll('a', attrs={'class':'area-link'}):
                try: 
                    if 'href' in h.attrs:
                        url = h.get('href')
                        urls.append(url)
                except:
                    pass

            ## Appending the extracted URL path to the base URL
            for i in urls:
                a = "https://www.walnutcapital.com" + str(i)
                URL.append(a)
            return URL

    ## There are 2 main URLs displaying property listings, so we call the function get_url() to extract the property URLs
    get_url("https://www.walnutcapital.com/apartment-for-rent-in-pittsburgh?search=1&pgNum=1")
    get_url("https://www.walnutcapital.com/apartment-for-rent-in-pittsburgh?search=1&pgNum=2")
    get_url("https://www.walnutcapital.com/apartment-for-rent-in-pittsburgh?search=1&pgNum=3")

    del URL[21] ## Dat for it doesn't exist in the webpage

    ###CREATING CSV FILE TO STORE DATA ###
    f = open("walnutcapital_live.csv","w", newline='') #change to your specific path if doesn't work
    writer = csv.writer(f)
    writer.writerow(("Name", "Address","Rent", "Bedroom", "Bathroom", "Property Features"))
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
        result = []

        ##EXTRACT APARTMENT NAME
        p_tags = soup.select('div[class="col-lg-9 col-md-9 col-sm-9"] h1')
        for p_tag in p_tags:
            #print(p_tag.get_text(strip=True))
            head.append(p_tag.get_text(strip=True))

        ##EXTRACT APARTMENT ADDRESS
        p_tags = soup.select('div[class="inner-wrap content-section"] h2[class="color-dark-blue"]')
        for p_tag in p_tags:
            #print(p_tag.get_text(strip=True))
            addr.append(p_tag.get_text(strip=True))

        ##EXTRACT PRICE          
            price = None
            b = []
            p_tags = soup.select('div[class="big"] span[class="po-value color-pink"]')
            for p_tag in p_tags:
                a = p_tag.get_text(strip=True) 
                b.append(a.split())

            price = str(b[1])[3:-2] ## Propert Price/Rent

        ##EXTRACT BEDROOMS AND BATHROOMS
            beds = None
            bath = None
            property_details = []

            p_tags = soup.select('div[class="pl-details"] div[class="pl-cell"] div[class="small weight-bold"]')
            for p_tag in p_tags:
                temp = p_tag.get_text(strip=True)     
                property_details.append(temp.split())

            beds = property_details[2]
            bath = property_details[3]

        ##EXTRACT BUILDING UTILITIES
            p_tags = soup.select('div[class="more-amenities-wrap"] div[class="row flex-stretch"] div[class="col-sm-4"] li')
            for p_tag in p_tags:
                #print(p_tag.get_text(strip=True))
                result.append(p_tag.get_text(strip=True))

        ## Joining the list elements to a single variable
        bname = "".join(head)   # Property Name
        baddr = " ".join(addr)  # Property Address
        bed = str(beds)[2:-2]   # Number of Bedrooms
        bath = str(bath)[2:-2]  # Number of Bathrroms
        butil = ",".join(result) # Property Utilities

        ## APPENDING VALUES FOR EACH PROPERTY TO NEW ROW IN THE CSV FILE
        f = open("walnutcapital_live.csv","a", newline='') #change to your specific path if doesn't work
        writer = csv.writer(f)
        writer.writerow((bname,baddr,price,bed,bath,butil))
        f.close()
        # ### END OF FUNCTION ###
    ## PASSING THE URL OF EACH PROPERTY TO THE FUNCTION
    for i in URL:
        func(i)

        
