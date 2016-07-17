FROM python:3.5-onbuild
# Use the official python 3.5 image with docker's new onbuild technique.

RUN pip install paver \
  && python setup.py install

EXPOSE 8888

CMD [ "/usr/local/bin/restapp" ]
