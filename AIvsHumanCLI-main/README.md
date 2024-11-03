[//]: # (write heading)

# AIvsHuman Command Line Interface

[//]: # (write description)

~~~
git clone https://github.com/Dimpal-Kalita/AIvsHumanCLI.git
cd AIvsHumanCLI
~~~

~~~
pip3 install -r requirements.txt
~~~

~~~
 python3 cli.py <input_file_path> <output_directory>
~~~ 

The model has been uploaded in Huggingface.

[Hugging faceLink](https://huggingface.co/yadagiriannepaka/BERT_MODELGYANDEEP.pth/commit/ebf7e40680f41fb5229d2b28606aa97ab3df94ad)

model = BertModel.from_pretrained("yadagiriannepaka/BERT_MODELGYANDEEP.pth") - line 14 in cli.py

## Build with Docker

~~~
docker build -t pan24-authorship-cli .
~~~

Push to TIRA via:

~~~
tira-run \
  --input-dataset generative-ai-authorship-verification-panclef-2024/pan24-generative-authorship-tiny-smoke-20240417-training \
  --image pan24-authorship-cli \
  --push true
~~~

