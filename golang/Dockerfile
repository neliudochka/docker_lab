FROM golang:1.20 AS builder
WORKDIR /app
COPY go.mod go.sum ./
RUN go mod download && go mod verify
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -o build/fizzbuzz

FROM scratch
WORKDIR /root/
COPY --from=builder /app/build/fizzbuzz ./
COPY --from=builder /app/templates ./templates
CMD [ "/root/fizzbuzz", "serve" ]