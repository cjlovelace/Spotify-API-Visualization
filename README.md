<img src="https://storage.googleapis.com/pr-newsroom-wp/1/2018/11/Spotify_Logo_CMYK_Green.png" alt="Spotify Logo in Green" width="270px" height="85px">

# Spotify API Visualizer by Cody Lovelace
	Primary Languages: Javascript, HTML, CSS, Python | Libraries: Eel, Spotipy


## Application Premise
*Spotify API Visualizer* allows a Spotify user to see their listening data in a new and interesting way. While we get just a glimpse of our listening statistics during Spotify's year-end celebration Spotify Unwrapped, much of this data is poorly utilized or completely hidden from the end user. This application gives the user insight into their own listening habits with some appealing data visualization and Python-to-Javascript programming magic.

This application was built using my personal Spotify April 2021 - April 2022 listening data.


## Technical (Music) Notes and Data Symphonies
Spotify API Visualizer uses the Eel library to connect Python's data visualization to a locally hosted web application. As blending Python with front-end web design can be a little daunting, Eel was chosen to serve as a bridge to bring Python functionality into a responsive website for data visualization.

<img src="https://developer.spotify.com/assets/AuthG_Intro.png" 
		 alt="Infographic showing My App as a connector between Spotify data and the end user">

Once creating a Spotify Developer project, a user receives an API key to gain access to Spotify data and functionalities as well as the ability to glean information directly from the authorized user. This information allowed my personal user data and artist specific names and images to be generated for display on the application.

## Composing Our Data

Spotify users can request a JSON file containing one year of their most recent listening history and then a subsequent request to receive their profile's data in its entirety.

The JSON file received upon first request will provide information in the following format:
```
  {
    "endTime" : "2021-04-11 15:53",
    "artistName" : "Robyn",
    "trackName" : "Dancing On My Own - Radio Edit",
    "msPlayed" : 278080
  }
```

Using this information, Python data visualizations were split into three categories:
- User Snapshot
- Top Artists
- User Profile

### User Snapshot
<img src="https://raw.githubusercontent.com/cjlovelace/Spotify-API-Visualization/main/static_web_folder/userProfileHeader.png">

Following authorization by the user in form of the Spotify API key, simple display information was pulled to greet the user and offer them a high-level overview of their profile information. 
* User queries Spotify to return the user's display name and profile hyperlink.
* Top artist and song are returned.
* Using JSON data, the most frequent time of day Spotify is used is displayed.
* A total number of hours is displayed for the user.

### Top Artists
<img src="https://raw.githubusercontent.com/cjlovelace/Spotify-API-Visualization/bd2dbab558c6c5b301b22f934743508e3ee795bd/static_web_folder/topArtistSample.png"
		 alt="A sample of the top artist UI interface. BLACKPINK's spotify profile image is shown in a circle with black text saying BLACKPINK and 670 plays listed in gold.">

Upon entering the Top Artists menu, the user's top ten artists for the given year are displayed alongside their data visualizations. Using the API, the artist's current profile image and the account's total number of plays for that artist are shown.

Visualizations include a pie chart depicting proportions of individual song listens, a line graph charting number of monthly listens for each artist, and a bar graph showing the number of song plays for each song by the artist.

**A sample of each generated visualization for my data can be <a href="https://github.com/cjlovelace/Spotify-API-Visualization/tree/main/static_web_folder"> found here.</a>**

### User Profile
<img src="https://github.com/cjlovelace/Spotify-API-Visualization/blob/main/static_web_folder/streamspertime.png"
		 alt="A pie chart displaying the number of Spotify streams per day. Afternoon 2956 streams, Morning 354 streams, Evening 2188 streams, and 5498 total streams.">

When selecting the User Profile menu, the user is shown a bar graph depicting their top songs for the given year. A pie chart breaks down the number of streams per given time of day, and a treemap of top artists shows the proportion of the user's listening habits in pleasing warm color tones.

## Takeaways and Future Development
This application was my first time producing a large scale project in Python and then connecting its visualizations to a front-end website. Development of this project was enjoyable; as an avid listener of music - and one stuck in a K-Pop loop lately - I was overjoyed to see my data and develop new categories of analysis outside of Spotify's in-the-box functionalities (see streams per day, top 20 song visualizations, artist listens per month, and others.)

While I have previously used APIs for smaller class projects, creating a full interface that used multiple dynamic images, links, and datasets was difficult, but I am a better developer for it.

Currently this application is limited to displaying my specific user data. If I were to continue development intended for a public release, I would allow any user to authenticate within this application and see what mysteries their Spotify account may hold.
