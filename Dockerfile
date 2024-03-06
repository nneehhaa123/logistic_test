From python:3.9-buster
COPY . /app
WORKDIR /app
EXPOSE 8501
RUN pip cache purge
RUN rm -rf /tmp/ptp*
RUN apt-get update && apt-get install -y make && make install
ENTRYPOINT ["streamlit", "run", "prediction/app.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.headless", "true", "--server.fileWatcherType", "none", "--browser.gatherUsageStats", "false"]
