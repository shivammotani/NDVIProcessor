# NDVIProcessor

# Intro

This is a Python program that calculates the NDVI value for a polygon defined, based on the Landsat data for "Near Infrared Band" and "Red Band".

Follow the process below to run the code on your local machine

### Step 1: Clone the Repository

`git clone https://github.com/shivammotani/SalesTax.git`

### Step 2: Install Requirements and Dependencies
I'm using pipenv as a virtual environment manager. You can use any other virtual environment as you like.
  Go to your directory where you've cloned this repository, open up your terminal and run the below commands:
  * `pip install pipenv`
  * `pipenv shell`
  * `pipenv sync`
    
### Step 3: Execute the below command to generate the output folder with NDVI image
  * `python app.py`
    
This will create a folder called Output in the current directory which contains the generated NDVI image along with the statistics.
Note: I would suggest removing the output folder once you clone the repository in your local.

### Step 4: Test with different inputs
  If you want to calculate the NDVI for any other region, put the polygon file inside `src/input` folder,
  and update the file name in app.py
  You can also update the source values for satellite data in app.py as well.
