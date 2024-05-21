import mechanicalsoup
import requests
from bs4 import BeautifulSoup

browser = mechanicalsoup.Browser()


def get_urls(url: str)->list:


    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Find all the story items
        story_items = soup.find_all("li", class_="story-item")
        
        # Initialize an empty list to store the URLs
        urls = []
        
        # Iterate over each story item and extract URL
        for item in story_items:
            # Extract URL
            url = item.find("a")["href"]
            
            # Append URL to the list
            urls.append(url)
            
        return urls
    else:
        print("Failed to retrieve the webpage.")
        return None

import requests
from bs4 import BeautifulSoup

def extract_text_from_div(url) ->str:
    text_content = []
    
    # Fetch the HTML content of the webpage
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
        
        # Parse the HTML content
        soup = BeautifulSoup(html_content, "html.parser")
        
        # Find the specific <div> element with class 'caas-body'
        div_element = soup.find("div", class_="caas-body")
        
        if div_element:
            # Find all <p> tags within the specified <div> element
            p_tags = div_element.find_all("p")
            
            # Extract the text from each <p> tag and append to the list
            for p in p_tags:
                text_content.append(str(p.get_text()))
    
    full_text = ' '.join(text_content)
    
    return full_text


def extract_date_from_url(url) -> str:
    # Fetch the HTML content of the webpage
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
        
        # Parse the HTML content
        soup = BeautifulSoup(html_content, "html.parser")
        
        # Find the <time> element
        time_element = soup.find("time")
        
        if time_element and time_element.has_attr('datetime'):
            # Extract the value of the datetime attribute
            datetime_value = time_element['datetime']
            # Split the datetime value to get only the date part
            date_value = datetime_value.split('T')[0]
            return date_value
        else:
            return "No datetime attribute found"
    else:
        return "Failed to retrieve the webpage"


