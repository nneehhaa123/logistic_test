From python:3.9-buster
COPY . /app
WORKDIR /app
EXPOSE 8600
RUN pip cache purge
RUN rm -rf /tmp/ptp*
RUN apt-get update && apt-get install -y make && make install
ENTRYPOINT ["streamlit", "run", "prediction/app.py", "--server.port=8600", "--server.address=localhost", "--server.headless", "true", "--server.fileWatcherType", "none", "--browser.gatherUsageStats", "false"]
