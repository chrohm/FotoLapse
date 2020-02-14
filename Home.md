# PhotoLapse Product Overview

[//]: # (TODO Leaving this here until a logo is developed)
[![Temporary Logo](https://avatars2.githubusercontent.com/u/37767905?s=40&v=4)](https://github.com/pouneh)


# POC:
Take a series of pictures and have them be displayed as a photo lapse GIF.

# MVP:
Allow anyone to upload photos with date/time/geolocation through a Web App. The generated gif should be stabilized and flow smoothly.

# Future:
Many users should be able to create their own cloud-based collections to create time lapse videos of things they care about.


# Product Requirements

  - POC
    - Take photo and store photo
    - Assemble GIF/Video
  - MVP (Web app)
    - Users can upload photos 
    - Users can download GIF
    - Support multiple locations
    - Stabilize photos when assembling the photolapse
  - Future
    - User account model w/ authentication
    - Privacy restrictions on uploading, viewing, and downloading lapses
    - Phone apps to fascilitate process and automatically upload photos when connectivity is detected
   

# Technical Reqs

1.	GREEN Back end/ processing unit for assembling the video or gif
    * [x] GIF seems to be the place to start, add option for video later
    * [x] Use Python as backend programming language
2.	YELLOW Web App (cloud based? Docker or leveraging cloud provider stuff)
    * [ ] Back end 
      * [ ] Photo storage
        * [ ] Cloud Database – need date/time and location
      * [ ] Photo manipulation
        * [ ] Stabilization algorithm
        * [ ] Landscape vs portrait photos?
        * [ ] Option for beautifying images? (lighting…)
      * [ ] Animation assembly (per location)
        * [ ] Allow for filtering the experience (time range, time of day, etc)
        * [ ] Specify a maximum size/length for the animation (we can filter out pictures based on that)
        * [ ] How fast can I assemble? Can I leverage prior animations? Do I store assembled animations to 
      * [ ] RED  account creation
      * [ ] RED account authentication
      * [ ] RED Privacy restrictions on uploading/viewing/modifying photostores
    * [ ] Front end
      * [ ] PUT (options to upload image)
      * [ ] GET most recent images in the location so user can compare
      * [ ] GET animation based on filters
      * [ ] RED login/account creation
      * [ ] RED UI for location collection privacy
3.  RED Phone apps!
    * [ ] UI elements in Web App front end
    * [ ] Delay upload until connection available

 
