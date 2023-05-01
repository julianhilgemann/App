#### 27.04.2023

I know for sure that I need Github to manage the code and documentation. Thankfully, no issues in setting it up

```ChatGPT
how can i do it in just terminal. Just code

To create a new Git repository using the folder "App" on your "Desktop" using Terminal in macOS, follow these steps:

1.  Open the Terminal app on your macOS.
    
2.  Navigate to the "Desktop" directory by entering the following command:
    

bash

`cd ~/Desktop`

3.  Create a new folder named "App" on your desktop (if it doesn't already exist) with this command:

arduino

`mkdir App`

4.  Change directory to the newly created "App" folder:

bash

`cd App`

5.  Initialize a new Git repository in the "App" folder:

csharp

`git init`

Now you have a local Git repository in the "App" folder on your Desktop. To add files, make changes, and commit them to your local repository, you can use Terminal commands. For example:

1.  Create a new file, e.g., `README.md`:

bash

`touch README.md`

2.  Add the file to the staging area:

csharp

`git add README.md`

3.  Commit the changes:

sql

`git commit -m "Initial commit"`

To push the changes to a remote repository, first create a new repository on a platform like GitHub, GitLab, or Bitbucket. Once you've created the remote repository, copy the repository URL. Then, in the Terminal, add the remote repository and push the changes:

1.  Add the remote repository (replace `your-remote-repo-url` with the actual remote repository URL you just copied):

csharp

`git remote add origin your-remote-repo-url`

2.  Push the changes to the remote repository:

perl

`git push -u origin master`

If the default branch is not `master`, replace it with the appropriate branch name (e.g., `main`).

You have now successfully created a new Git repository using the folder "App" on your "Desktop" using Terminal in macOS.
```

Cool. Now I think the first thing I have to do is track the changes and push this liitle update. Trivial steps I guess but important nonetheless.

```ChatGPT
to track changes and upload them to GitHub, follow these steps in the Terminal:

1.  Navigate to your repository folder on your computer:

bash

`cd path/to/your/repo`

Replace `path/to/your/repo` with the actual path to your repository folder.

2.  Check the status of your repository to see the changes you've made:

lua

`git status`

3.  Stage the changes (add the files to the staging area):

For all changed files:

csharp

`git add .`

Or for specific files, replace `your-changed-file` with the actual file name:

csharp

`git add your-changed-file`

4.  Commit the changes with a descriptive message:

sql

`git commit -m "Your commit message"`

Replace `Your commit message` with a brief description of the changes you've made.

5.  Make sure your local repository is up to date with the remote repository:

`git pull origin your-branch-name`

Replace `your-branch-name` with the name of the branch you're working on (e.g., `main` or `master`).

6.  Push the changes to the remote GitHub repository:

perl

`git push origin your-branch-name`

Replace `your-branch-name` with the name of the branch you're working on (e.g., `main` or `master`).

Your changes are now uploaded to GitHub.
```

Or this. Done :) 

```ChatGPT
```bash
cd path/to/your/repo
git status
git add .
git commit -m "Your commit message"
git pull origin your-branch-name
git push origin your-branch-name
```
```

Now that the plan is done, swift execution is key.

The best way to keep track of progress is set up a project management tool and from past experiences I know that ASANA will be sufficient for the the task since there are no collaborators or other users that need to access the information. Premium Account with all bells and whistles will be 11 €, lets see if I need it. One month trial Period starts from now on. 

First things first, putting all necessary steps inside asana to get a visual understanding about the requirements. I will plan using the original timeframe and see if I can outpace myself.

From previous documentation  I will use this list and split it into workable chunks

```ChartGPT

Week 1:

-   Define project goals and objectives.
-   Set up project management and communication tools (e.g., Trello, Slack).

Week 2:

-   List all the features and tasks required for the project.
-   Prioritize the tasks based on importance and dependencies.
-   Estimate the effort required for each task.

Weeks 3-4:

-   Brainstorm and finalize design ideas (2 hours).
-   Create wireframes for the application (3 hours).

Week 5:

-   Create a prototype of the time series forecasting tool using Google Sheets (4 hours).
-   Iterate on the prototype based on your own feedback (1 hour).

Weeks 6-10:

-   Set up the Flask API framework (6 hours).
-   Connect the application to the required data sources (10 hours).
-   Design and implement the database schema using SQLAlchemy (10 hours).
-   Develop API endpoints for data retrieval and manipulation (14 hours).

Weeks 11-13:

-   Implement the interactive front-end using Streamlit (18 hours).
-   Connect the front-end to the Flask API (6 hours).
-   Test the application for bugs and performance (6 hours).
-   Host the project repository on Github (4 hours).
-   Deploy the application to a suitable hosting platform (e.g., Heroku, AWS) (8 hours).

```


#### Saturday 29.04.2023

However, planning it out I immediately see that the timeframe for project completion is very generous and I might be able to do it faster. A quick jot down inside the timeline should be fine and then I will power through as much as I can without waiting too long or sticking to the long time intervalls.

Thankfully, Asana offers very nice interactivity when it come to planning. Once the tasks are broken down and inside the system, it's possible to manually morph and adjust in whatevery way needed which makes it fun to use. The visual features really help with the process.

Instead sticking to the initial plan I will shift the blocks around manually and then work from there. Thankfully timeframes are already estimated. Planning itself is a breeze and took up almost no time. The project does not feel overwhelming since its broken down into small pieces that are managable. 

Intuitively the most tedious taks right now seem to be the wiring up of the software tools. Planning, Design, Featured and documentation are by far the easiest.

Based on the technical complexity I decided to give all-things-code the highest priority. It all really is based on the code. Tasks and features are kinda not really that important since its about an E2E MVP anyways and since I got my basic wireframes it feels like I should go for the code immediately and not plan too much. Same goes for the google-sheets prototyping. It seems that its not needed since all I have to do is define a few time series that I want to be selectable, get the Keys and work the backend. The interface is simple anyways, there is no need for prototyping as the MVP is somewhat the prototype. 

Based on previous wireframe I think the easiest way would be to go straight for the code since al it needs is simple interface, simple model, simple backend and a few API Calls to central bank servers. Might as well immediately setup development environment.

![[wireframe MVP.png]]

After prompting for Development Environment suggestions, especially since I want the environment Machine and OS Independent, ChatGPT suggests to do this inside a docker container. Looks simple enought, might as well just go for it.

here are the suggested steps:

To create a development environment that is machine and OS independent, you can use Docker. Docker allows you to package an application with its dependencies into a lightweight, portable container that can run consistently on any platform with Docker installed.

1. Install Docker on your machine. Download the appropriate installer for your operating system from the Docker website: https://www.docker.com/products/docker-desktop

2. After installing Docker, create a `Dockerfile` in your project directory. This file will contain instructions to build the Docker image for your application. Add the following content to the `Dockerfile`:

```
# Use the official Python base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files into the container
COPY . .

# Expose the Flask application port
EXPOSE 5000

# Expose the Streamlit application port
EXPOSE 8501

# Start the Flask and Streamlit applications
CMD ["sh", "-c", "flask run --host=0.0.0.0 & streamlit run dashboard.py --server.address 0.0.0.0 --server.port 8501"]
```

3. Create a `requirements.txt` file in your project directory to list your application's dependencies:

```
Flask
streamlit
pandas
numpy
matplotlib
statsmodels
requests
```

4. Build the Docker image for your application:

```
docker build -t your-image-name .
```

Replace `your-image-name` with a name for your Docker image.

5. Run the Docker container for your application:

```
docker run -p 5000:5000 -p 8501:8501 your-image-name
```

Replace `your-image-name` with the name you used in the previous step.

Now your Flask application will be accessible at `http://localhost:5000`, and your Streamlit application will be accessible at `http://localhost:8501`.

With this setup, your development environment is machine and OS independent. Anyone with Docker installed can build and run your application consistently, regardless of their platform. They only need to clone your repository and follow the steps to build and run the Docker container.

---
Since I have no clear Idea of how this is supposed to work I might as well prompt for more detailed instructions considering the creation of the Dockerfile:

The creation of the Docker image in step 2 is done through a Dockerfile. A Dockerfile is a script containing a set of instructions that define the base image, dependencies, and configuration needed to create a custom image for your application.

Here's a step-by-step explanation of how to create the Dockerfile:

1. In your project directory, create a new file named `Dockerfile` (without any extension). You can use any text editor to create this file.

2. Add the content provided in step 2 of the previous answer to the `Dockerfile`. This content specifies the base image, working directory, dependencies, exposed ports, and commands to run your Flask and Streamlit applications.

3. Save the `Dockerfile` in your project directory.

The Dockerfile is not run directly in the terminal or through the Docker engine. Instead, you use Docker commands in the terminal to build an image from the Dockerfile and then run a container using that image.

To build the Docker image, open a terminal, navigate to your project directory, and run the following command:

```
docker build -t your-image-name .
```

Replace `your-image-name` with a name for your Docker image. This command tells Docker to build an image using the Dockerfile in the current directory (indicated by the `.` at the end of the command).

After the image is built, you can run a container from it using the following command:

```
docker run -p 5000:5000 -p 8501:8501 your-image-name
```

Replace `your-image-name` with the name you used when building the image. This command maps the ports 5000 and 8501 from the container to the host machine, allowing you to access the Flask and Streamlit applications at `http://localhost:5000` and `http://localhost:8501`, respectively.

In summary, you create the Dockerfile in your project directory using a text editor, and then you use Docker commands in the terminal to build an image from the Dockerfile and run a container using that image.

At this point I might as well already work within VSCode to edit my files.

After creating the dockerfile and requirements as well as running Docker first I want to make sure that dashboard.py as well as app.py and all packages are downloaded and installed

![[Hello Streamlit.png]]

Alright, seems to work inside the docker in http://0.0.0.0:8501/
And flask ![[Hello Flask.png]] at port 5000. 

And to stay in the loop when it comes to the theory behind what just happened, some explainers:

Docker is a platform that allows developers to easily create, deploy, and run applications in containers. Containers are lightweight, portable, and isolated environments that can run applications and their dependencies consistently on any platform with Docker installed. Containers enable developers to package an application and its dependencies into a single unit, eliminating the "it works on my machine" problem when sharing or deploying code.

Ports are a communication endpoint in computer networking. They allow multiple processes to run on a single machine without conflicts, as each process can be assigned a unique port number. When you expose a port in a Docker container, you enable communication between the container and the host machine or other containers via that port.

We use ports 5000 and 8501 because they are the default ports for Flask and Streamlit, respectively. Flask applications typically run on port 5000, while Streamlit applications run on port 8501 by default.

Here's how the files `app.py`, `dashboard.py`, Docker, and the ports interact:

1. `app.py` contains the Flask application code. When the application is run, it starts a server that listens on port 5000 (the default Flask port) for incoming HTTP requests. This server processes the requests and returns the appropriate responses.

2. `dashboard.py` contains the Streamlit application code. When the application is run, it starts a server that listens on port 8501 (the default Streamlit port) for incoming HTTP requests. This server processes the requests and returns the appropriate responses.

3. The Dockerfile specifies how to build the Docker image for the application. It includes instructions to install the required dependencies, copy the application files, expose the ports, and run the Flask and Streamlit servers.

4. When you build the Docker image using the `docker build` command, Docker creates an image that includes the application files, dependencies, and configuration specified in the Dockerfile.

5. When you run the Docker container using the `docker run` command, Docker starts a new container from the image and runs the Flask and Streamlit servers inside the container. The `-p` option in the `docker run` command maps the container's ports to the host machine's ports, allowing you to access the Flask application at `http://localhost:5000` and the Streamlit application at `http://localhost:8501`.

In summary, `app.py` and `dashboard.py` contain the application code for Flask and Streamlit, respectively. Docker creates a container that runs both applications, with the ports exposed for communication between the container and the host machine or other containers.

And, finally, considering running the docker image on some other machine, the steps are as follows:

a) To end the running Docker container process, follow these steps:

1. Open a new terminal window.
2. List all running Docker containers using the command:

```bash
docker ps
```

This will show a list of running containers with their Container IDs, Image names, and other details.

3. Locate the Container ID of the running container you want to stop. Once you have the Container ID, stop the container using the command:

```bash
docker stop <container_id>
```

Replace `<container_id>` with the actual Container ID from the previous step.

b) To restart the process, simply run the `docker run` command you used earlier:

```bash
docker run -p 5000:5000 -p 8501:8501 your-image-name
```

Replace `your-image-name` with the name you used when building the image.

c) To transfer the Docker container to another computer, follow these steps:

1. Push the Docker image to a container registry like Docker Hub. First, create an account on https://hub.docker.com/ if you don't have one. Then, log in to your Docker Hub account from the terminal using the command:

```bash
docker login
```

Enter your Docker Hub username and password when prompted.

2. Tag your Docker image with your Docker Hub username and a new image name:

```bash
docker tag your-image-name your-dockerhub-username/new-image-name
```

Replace `your-image-name` with the name you used when building the image, `your-dockerhub-username` with your Docker Hub username, and `new-image-name` with a new name for your Docker image.

3. Push the tagged image to Docker Hub:

```bash
docker push your-dockerhub-username/new-image-name
```

Replace `your-dockerhub-username` and `new-image-name` with the appropriate values from the previous step.

4. On the other computer, make sure Docker is installed. Then, pull the Docker image from Docker Hub using the command:

```bash
docker pull your-dockerhub-username/new-image-name
```

Replace `your-dockerhub-username` and `new-image-name` with the appropriate values.

5. Once the image has been pulled, run the Docker container on the new computer using the command:

```bash
docker run -p 5000:5000 -p 8501:8501 your-dockerhub-username/new-image-name
```

Replace `your-dockerhub-username` and `new-image-name` with the appropriate values.

Now the application should be running on the new computer, accessible at `http://localhost:5000` for the Flask app and `http://localhost:8501` for the Streamlit app.

---

To actually start working on the models itself It is important to figure out how to get the data from the Central Bank and then estimate the model + plotting and so on. 
First step in prototyping will be a jupyter notebook where to prototyping takes place.

For building the MVP, it's a good idea to start with prototyping in a Jupyter Notebook, as it provides a flexible and interactive environment for experimenting with the code, visualizations, and models. Once you have the core functionality working in the Jupyter Notebook, you can then integrate the code into the Streamlit and Flask applications.

Here's a suggested breakdown for building the MVP:

1. **Data acquisition and preprocessing**: Use the Jupyter Notebook to interact with the European Central Bank API or Bundesbank API to fetch the required time series data. Perform any necessary data cleaning, transformation, or aggregation.

2. **Exploratory data analysis (EDA)**: In the Jupyter Notebook, create visualizations like bar charts, seasonal plots, densities, and rates of change to understand the data better. Calculate summary statistics and correlations to gain insights into the data.

3. **Model selection and development**: Based on the EDA, choose appropriate time series regression models to forecast the data. Implement these models in the Jupyter Notebook and evaluate their performance using relevant metrics.

4. **Model integration with Streamlit**: Once you have a working model in the Jupyter Notebook, integrate it with the Streamlit application (`dashboard.py`). Build the user interface to allow users to select the desired time series data, the model, and the forecasting frequency (yearly, quarterly, or monthly).

5. **Model integration with Flask**: Create the necessary API endpoints in the Flask application (`app.py`) to handle the requests from the Streamlit frontend. The Flask backend should be responsible for fetching the data from the APIs, running the selected model, and returning the forecasting results to the frontend.

6. **Finalize the user interface**: Refine the Streamlit frontend to display the forecasting results, model metrics, and any additional visualizations that might be helpful for the user. Ensure the interface is user-friendly and responsive.

Starting with a Jupyter Notebook allows you to test and iterate quickly on different parts of the application. Once the core functionality is established, you can integrate it into the Streamlit and Flask applications, focusing on creating a seamless and user-friendly experience.

So, lets start with Prototype.ipynb. After adding it to the local working directory, I want to make sure to keep it all contained within the docker file and in sync with Github.

To run the dockerfile with everything use:

```bash

docker run -d --name app -p 5000:5000 -p 8501:8501 -p 8888:8888 app
```

---

ECB SDMX 2.1 RESTful web service [Documentation](https://sdw-wsrest.ecb.europa.eu/help/)
and also the [documentation for Bundesbank](https://www.bundesbank.de/de/statistiken/zeitreihen-datenbanken/hilfe-zu-sdmx-webservice)

Also, before going into the prototyping itself the SQL Environment should be created first, for proper data management. I will go with SQL Alchemist.

Lets see how this will go:

Here's a high-level plan for incorporating a database with SQLAlchemy into your project:

1. Choose a relational database management system (RDBMS) that meets your requirements. Some popular options are PostgreSQL, MySQL, and SQLite. SQLite is a lightweight option that's easy to set up and works well for smaller projects, while PostgreSQL and MySQL provide more robust features and can handle larger workloads.

2. Update your `requirements.txt` to include SQLAlchemy and the appropriate database driver. For example, if you choose PostgreSQL, you'll need to add `SQLAlchemy` and `psycopg2` to your `requirements.txt`.

3. Modify your Dockerfile to include the installation of the necessary database server if you decide to run the database server within the same container as your application. However, for better separation of concerns, it's recommended to run the database server in a separate container or on a separate server.

4. Update your Flask application to establish a connection with the database using SQLAlchemy. You'll need to define your data models (tables) and set up the necessary queries to interact with the data.

5. Update your Streamlit application to request data from your Flask backend, which will then fetch the data from the database.

Remember that when dealing with databases, it's important to consider data backup and recovery strategies, as well as security measures such as user authentication and access control.

With the addition of the database, the whole process changes a bit. Not substantially but a bit:

Here's a high-level overview of how Flask, the database, and the Central Bank API will interact in the application:

1. **User interaction**: A user interacts with the Streamlit application, selecting a time series and specifying parameters such as the time range and model.

2. **Streamlit to Flask request**: The Streamlit application sends a request to your Flask backend, including the user's selected parameters.

3. **Flask checks the database**: Upon receiving the request, the Flask backend checks the database to see if the requested data is already available. If the data is in the database, Flask retrieves it and proceeds to the next step. If the data is not available or needs to be updated, Flask sends a request to the Central Bank API.

4. **Request data from Central Bank API**: If necessary, Flask sends a request to the Central Bank API, including the appropriate parameters to fetch the required data.

5. **API response**: The Central Bank API returns the requested data to the Flask backend.

6. **Store data in the database**: If the Flask backend fetched new data from the API, it stores the data in the database for future use.

7. **Data processing and modeling**: With the data in hand, Flask processes the data as needed (e.g., applying the selected model) and calculates the necessary metrics.

8. **Flask to Streamlit response**: Once the processing is complete, Flask sends a response to the Streamlit application, including the processed data and any relevant metrics.

9. **Display results**: The Streamlit application updates the user interface, displaying the time series data, model results, and any additional charts or metrics.

This architecture allows for efficient data retrieval and processing, as well as a separation of concerns between the frontend (Streamlit) and the backend (Flask). By caching data in the database, one can reduce the number of requests to the Central Bank API and improve the performance of the application.

---
So yeah, I will go for prototyping first, until I have a pandas dataframe that I can fetch with a simple key and then I will setup the Database to save the Data into the database. 

#### 01.05.2023

For that I will integrate the API Call for the german Bundesbank that I already build once. The idea is simple: Given a dictionary of Names and Keys, the code accesses the API and gets the JSON that has the information. From there it extracts the time series data and time stamps and puts it into a pandas dataframe. If I give it a whole list of variables, it loops through the list and gives back the whole table and joins in to match the start and end date. For this purpose I will adjust it and make it return just one time series and store some metadata, such as dates, frequencies and the like inside a database. Later on, the concept is that first there will be a lookup inside the database and, if not available, only then a call to the central bank server.

Fortunately the code works as expected and the API call does what it is supposed to do which means now I have data.

Strategically I think setting up an environment for the Database management might be beneficial to get closer to the end goal. Especially since the data is not as useful when its in the ram anyways.

So here comes the first technically challenging part, that is creating the database and hooking it all up. For now I will stick to a two stage process where I will use Flask to call the Central bank and manage the data and flask should just access the ready DB and plot.

Since I have my data already I might as well quickly prototype a graph that I want to be displayed in streamlit, including the time series regression, trendline.

And since it is unnecessary at this stage to deal with Docker images, I might as well continue locally, without containerization.

First things first. I successfully fetched the Data and wrote it into the SQL Database and now can extract it from the database and plot it accordingly. I might as well go for a regression right off the bat.


![[Pasted image 20230501165904.png]]


With some more statistics:

![[Pasted image 20230501165946.png]]

