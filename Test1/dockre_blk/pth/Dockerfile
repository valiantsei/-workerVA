FROM python:3
WORKDIR /usr/src/app
RUN pip3 install ansible junos-eznc jxmlease ncclient
RUN ansible-galaxy install Juniper.junos
COPY . .
CMD ["run.py"]
ENTRYPOINT ["python3"]
