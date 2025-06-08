# Stock Sentiment Poller

This repository gathers sentiment data related to stock markets from a variety of sources such as
news feeds, social media, and opinion analysis APIs.

## Features

- Modular architecture for adding multiple sentiment sources
- Text sentiment analysis using NLP tools (e.g., TextBlob, Vader, OpenAI)
- Queue publishing for downstream processing or storage
- Secure configuration via Vault
- Supports RabbitMQ and AWS SQS
- JSON-structured logging for observability
- Docker and Kubernetes ready

## Project Structure

```
src/
├── app/
│   ├── config.py
│   ├── main.py
│   ├── poller_factory.py
│   ├── queue_sender.py
│   ├── utils/
│   └── pollers/                # e.g., news, reddit, twitter
```

## Usage

```bash
make install
make run
```

## Environment Variables

| Variable           | Description                      |
| ------------------ | -------------------------------- |
| `QUEUE_TYPE`       | `rabbitmq` or `sqs`              |
| `POLLING_INTERVAL` | Interval between sentiment pulls |
| `VAULT_ADDR`       | Vault server address             |
| `VAULT_TOKEN`      | Vault token or AppRole config    |

## Development

```bash
make lint
make test
make build
```

## License

Apache License 2.0
