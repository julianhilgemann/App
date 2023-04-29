# Use the official Python image as the base image
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt requirements.txt

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app.py, dashboard.py, and Jupyter notebook files into the container
COPY app.py app.py
COPY dashboard.py dashboard.py
COPY Prototype.ipynb Prototype.ipynb

# Expose the ports used by Flask, Streamlit, and JupyterLab
EXPOSE 5000
EXPOSE 8501
EXPOSE 8888

# Run the application and JupyterLab
CMD ["sh", "-c", "flask run --host=0.0.0.0 --port=5000 & streamlit run dashboard.py --server.port 8501 --server.headless=True --server.enableCORS=False & jupyter lab --ip 0.0.0.0 --port 8888 --no-browser --allow-root --NotebookApp.token='' --NotebookApp.password=''"]
