# docker build -t pan24-authorship-cli .
FROM pytorch/pytorch:2.3.0-cuda12.1-cudnn8-runtime

ADD requirements.txt /

RUN set -x \
    && apt update \
    && apt install -y git python3 python3-packaging python3-pip \
    && pip install --no-cache --upgrade pip \
    && pip install -r /requirements.txt \
    && rm -Rr /requirements.txt \
    && rm -rf /var/lib/apt/lists/*

RUN python3 -c 'from transformers import BertTokenizer, BertConfig, BertForSequenceClassification; BertTokenizer.from_pretrained("bert-base-uncased"); BM = BertForSequenceClassification.from_pretrained("bert-base-uncased"); print(BM.from_pretrained("yadagiriannepaka/BERT_MODELGYANDEEP.pth"))'

ENV PYTHONPATH=/app
ENV HF_HUB_OFFLINE=1

COPY . /app

ENTRYPOINT [ "python3", "/app/cli.py", "$inputDataset/dataset.jsonl", "$outputDir" ]

