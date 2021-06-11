FROM golang:alpine

RUN mkdir /app

ENV GOOGLE_APPLICATION_CREDENTIALS=./sentimentanalysis-315620-51cd413739f1.json

COPY . /app
WORKDIR /app
## we run go build to compile the binary
## executable of our Go program
RUN go build .
## Our start command which kicks off
## our newly created binary executable
CMD ["/app/main"]