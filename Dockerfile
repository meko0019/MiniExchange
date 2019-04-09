FROM python:3.7.2-slim
WORKDIR /src

# Copy the requirements file in order to install
# Python dependencies
COPY requirements.txt .

RUN pip install --upgrade pip &&\ 
    pip install --no-cache-dir -r  requirements.txt

# Copy over the rest of the project
COPY . /src