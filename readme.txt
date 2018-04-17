Readme

1. get_filters function:

To build this function, I had to use the Slack Data Analyst Workspace. Using input from other students, I built out the filtering function which takes inputs from the user. I noticed that, while testing, I would often type “New York” instead of “New York City”. To be able to use “New York” as a valid answer, I wrote an if statement to transform “New York” to the correct “New York City”. Loops are included within this function to handle inputs that are not valid. To call this function in main(), I realized I had to first pass in arguments that would be immediately overwritten by the user inputs.

2. load_data function:

I also used the Slack Workspace to help build this function. My strategy the whole time was to build a single function and test it until I could prove it was working. This function helped me to understand how define variables based on the return of another function (df = load_data(city, month, day).

3. time_stats function:

I used some code from the Slack Workspace to begin this function, but changes some of it to make my own. Using month number did not make sense to me, so I change the number into month name using the “calendar” library. I also wanted to change the starting hour into a time, to I turned it to military time and added that time +1 hour to define a window within which the most popular time is. I also passed in the city name into print() to state which city the stats are for.

4. station_stats function:

By the time I go to this function, I was able to build the code without help from the forums. I used .idxmax to determine the most popular station points and passed them into print().

5. trip_duration_stats: 

I noticed that the returns for total_duration and mean_duration were in seconds. This did not make sense as an answer, so I decided to write a function to change seconds into days: hours: minutes: seconds. To do that, I defined the time_convert function and passed in the appropriate variable as an integer.

6. user_stats

In this function, I had to include an error handler for the fact that Washington contains less data than the other two cities.
