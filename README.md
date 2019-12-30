## PROJECT NAME 
 - NewsHighlight 
 ![alt text](12.png)

 # DESCRIPTION

This is a Python-Flask Application that makes use of NEWS API to fetch Latest & Trending News from Various sources. 

## User Story

- Users can see various news sources on the homepage of the application.

- Users can select a news source and see all news articles from the selected news source in the application..

- Users can see image, description and the time a news was created. 

- Users can click on an article and read the full article on the source website.


## Features
Here are the features in summary:
* A minimalistic landing page showing trending world news and a variety of news sources
* Clickable news sources which direct the user to a page with article highlights from the particular source.

## Behaviour Driven Development (BDD)
|Behaviour 	           |    Input 	                 |       Output          |
|----------------------------------------------|:-----------------------------------:|-----------------------------:|       
|Page loads, user arrives in the landing page, is greeted to a list of all available news sources.                        |  The user can click on any particulr list group item to be directed to a separate page containing news highlights curated by the same publisher.          | On clicking the "read more" button, the user is redirected to the main article to read the full story.    |   

## Requirements
* This program requires python3.+ (and pip) installed, a guide on how to install python on various platforms can be found [here](https://www.python.org/)
* Once python is installed, install the folowing external libraries provided in the requirements.txt file using pip
* Example: 
    * **`pip install flask`**