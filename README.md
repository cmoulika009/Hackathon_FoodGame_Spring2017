# Food Game : Junk or Healthy?

<h3>About Use-Case</h3>

The main aim of this use-case is to classify Food i.e Junk or Health using Machine Learning Tools. Also need to predict calories of food and score of Food based on user reviews.

<h3>Application Overview</h3>

As part of this use-case we developed a web application to display and predict the images. First we collected dataset from Food100 from which only 25 classes are chosen and divided them as Junk or Healthy. We used Inception Model to retrain the last layer (kind of transfer learning) with which we achieved 75% accuracy. Further used Edmam API to fetch calories of given image and used IBM Watson API for sentiment analysis to the scale of food based on reviews.

<h3>Tools and Softwares Used</h3>

JetBrains PyCharm

Inception Model

Tensor Flow

Python,HTML,CSS

<h3>About the Application</h3>

As discussed we collected food data set from https://www.vision.ee.ethz.ch/datasets_extra/food-101/. Among which we took 25 classes and classified them as Junk and Healthy. Using Inception Model to retrain the last layer (kind of transfer learning) with which we achieved 75% accuracy. The ouput grapgh of inception model is saved and used in our Web Application. Once the web application is executed the below page is displayed. In the main page where all the images related to Food is displayed where we can click on Predict to get further details of image.  

<img src="https://github.com/cmoulika009/Hackathon_FoodGame_Spring2017/blob/master/Documentation/Images/Home.png">

Once we click on Predict, Tensor Flow is invoked and corresponding images are displayed in image. We used Edmam API to fetch calories of given image and used IBM Watson API for sentiment analysis to the scale of food based on reviews.

<img src="https://github.com/cmoulika009/Hackathon_FoodGame_Spring2017/blob/master/Documentation/Images/PizzaPredict.png">

<img src="https://github.com/cmoulika009/Hackathon_FoodGame_Spring2017/blob/master/Documentation/Images/pizza-code.png">

As shown in below image first the pizza is predicted and the calories and food classification is also displayed below.

<img src="https://github.com/cmoulika009/Hackathon_FoodGame_Spring2017/blob/master/Documentation/Images/Pizza.png">

Below is another example for Orange

<img src="https://github.com/cmoulika009/Hackathon_FoodGame_Spring2017/blob/master/Documentation/Images/Orange-Code.png">

<img src="https://github.com/cmoulika009/Hackathon_FoodGame_Spring2017/blob/master/Documentation/Images/Orange.png">

<h3>Youtube Link:</h3> https://www.youtube.com/watch?v=ix7ALJjknow

<h3>Presentation Link:</h3> https://github.com/cmoulika009/Hackathon_FoodGame_Spring2017/blob/master/Documentation/FoodGame-HackathonSpring2017.pptx


