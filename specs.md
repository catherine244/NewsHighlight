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
