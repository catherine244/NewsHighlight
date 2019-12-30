# <p align="center">The News API Specification

Last modified: **30/12/2019**

Version: **3.6 **

I have tried my best to make the specification easy to read and implement, so if you come across
any inconsistencies or experience any difficulty, do let me know by sending an
email [here](ccayreen24@gmail.com),
or by reporting an issue in the [specification
repo](https://github.com/catherine244/NewsHighlight/issues).


## Table of Contents ##
- [Introduction](#1-introduction)
- [System Overview](#2-system-overview)
- [Usage](#2.2-usage)
- [Future Directions and Open Questions](#2.3-future-directions-and-open-questions)

## **1. Introduction**
* **1.1. Scope**
    + This document describes a News Website App that is primarily concerned with making its users get information and updates about latest happenings around the globe(world).
    The app is entirely updated/powered by the News API.  
    + Because of time constraint, this project only covers fetching, filtering and displaying data.
    + Its future scope is to implement ability to authenticate,choose favourites, subscribe to specific source updates and also share updates via social sites.

    * **1.2. Goals**

   1. Give information to the public-political,sports, entertainment, technology.
   2. Instant and latest news fro all over the globe.
   3. Easier accessibility.
   4. Pictures of articles resective of news source

* **1.2.1 Goals for implementation**

      +  The process by which the API push updates to the app must be simple.
    
      + The app must be secure to use in environments that lack support for Security. This is by use of SECRET_KEY which will prevent CrossSiteOriginForgery


## **2. System overview**


   The News Web ultimately provides a comfortable and friendly method of obtaining trusted
   news around the world.
   This app targets everyone around the world since it is easy to use. 

   *  **2.1 How the system works** 

  The following are the steps on how The News Web app works, (This is an error-free case.)

       Fetching data:
            Periodically, the News app gets updates from The News Web API using the defined Base_URL and an API_KEY, with the use of a context manager, the data from the API gets read, then converted into json format and stored in an object.

      Processing data:
            The Json data then gets processed while applying a filter by the key value assigned to a variable
            i.e
            urlToImage = item.get('urlToImage)
            if urlToImage:
                create object, then instantiate it respective class.
      Displaying data:
            Processed data then get passed into the template(html), where it gets iterated through and displayed.

  *  **2.2. Usage**


       **Minimum Requirements(if working on a local environment)**
    1. Fair/Good internet connection.
   

      **You can also choose to use the live link**
      Steps
    1. With a browser of your choice, Visit )
    2. Onload, the page displays news sources(Channels").
    3. Click on any channel you woud like to read news from.
    4. You will be presented with various articles from the news source.
    5. Click any that you find interesting.