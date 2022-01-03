# dash.plotly covid visualization

## What is Dash? 
According to the official documentation:

“Downloaded 600,000 times per month, Dash is the original low-code framework for rapidly building data apps in Python, R, Julia, and F# (experimental).
Written on top of Plotly.js and React.js, Dash is ideal for building and deploying data apps with customized user interfaces. It's particularly suited for anyone who works with data.
Through a couple of simple patterns, Dash abstracts away all of the technologies and protocols that are required to build a full-stack web app with interactive data visualization.
Dash is simple enough that you can bind a user interface to your code in less than 10 minutes.
Dash apps are rendered in the web browser. You can deploy your apps to VMs or Kubernetes clusters and then share them through URLs. Since Dash apps are viewed in the web browser, Dash is inherently cross-platform and mobile ready.”
 
## What can be done with dash? 
Well, Dash is the pencil, you are the artist, but to make an idea of what has been accomplished, check out the Dash app gallery

## Building our first dash Graph
### Installation

In this tutorial we will show how to use Dash to build a Choropleth Map, 

so, first goes first, create a virtual environment and activate it
```
   $ virtualenv dashvenv
   $ source ./dashvenv/bin/activate
```
Then, install dash
```
 $ pip install dash
 $ pip install jupyter-dash
 $ pip install pandas
```
you can try by running one of the dash premade examples, just create an app.py file and copy one of the following examples, we will use this one

gist

### Test the installation
and then, just run it and see it working 
```
Run this app with `python app.py` and
visit http://127.0.0.1:8050/ in your web browser.
```

### Change the example
Dash includes "hot-reloading", this feature is activated by default when you run your app withapp.run_server(debug=True). This means that Dash will automatically refresh your browser when you make a change in your code.


# Create our own Dash app

We will use a Covid-19 public dataset, to create a world map with the pandemic evolution through dates,  

First, we will pull the data as CSV and create a pandas dataframe, only with the relevant information 



Then, we will create a dash component that will contain:
DIV,
H1 header,
DROPDOWN slct_year that will contain the dates of our dataset,
DIV output_container a div that will display a user friendly message 
Graph the world heat map

 to do this we have to re-format the dates in an object, to create the Dash dropdown component 

Then, we can create the app layout with our Dash components


Now, we have to create a Callback function, that will have the dropdown value as input, and the output_container and the map, to update the information with the given input



Then, we can define what to do with the input given value, that is the selected year


We will create the friendly message and the choropleth graphic, 
here you can find more information about this plotly.express.choropleth
The data frame will be filtered by date, go ahead and add a continent filter, or add a selector for different values, like vaccination percentage, or test realized

If everything goes well, we shall be able to run our app and see it working


here you can find the repository of this project
