# Use the official Python base image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy requirements.txt and install the required packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app folder containing app.py, dashboard.py, and models.py
COPY app/ app/

# Copy notebooks folder containing Prototype.ipynb
COPY notebooks/ notebooks/

# Copy data folder containing time_series_data.db
COPY data/ data/

# Expose the necessary ports for Flask, Streamlit, and JupyterLab
EXPOSE 5000 8501 8888

# Start JupyterLab, Flask, and Streamlit (customize the commands as needed)
CMD jupyter lab --ip 0.0.0.0 --port 8888 --no-browser --allow-root --NotebookApp.token='' --NotebookApp.password='' & \
    python app/app.py & \
    streamlit run app/dashboard.py
