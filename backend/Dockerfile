FROM public.ecr.aws/lambda/python:3.11


COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt --no-cache-dir

COPY . .

RUN mkdir -p /tmp/.cache

# Tell OpenCV to work without display
ENV QT_QPA_PLATFORM=offscreen
ENV OPENCV_IO_ENABLE_OPENEXR=0

CMD ["app.handler"]