FROM golang:1.20 AS builder
WORKDIR /app
COPY go.mod go.sum ./
RUN go mod download && go mod verify
COPY . .
RUN go build -o build/fizzbuzz

FROM gcr.io/distroless/base
WORKDIR /root/app
COPY --from=builder /app/build/fizzbuzz ./
COPY --from=builder /app/templates ./templates
CMD [ "./fizzbuzz", "serve" ]