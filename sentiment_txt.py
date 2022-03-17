# -*- coding: utf-8 -*-
#
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# DO NOT EDIT! This is a generated sample ("Request",  "language_sentiment_text")

# To install the latest published package dependency, execute the following:
#   pip install google-cloud-language

# sample-metadata
#   title: Analyzing Sentiment
#   description: Analyzing Sentiment in a String
#   usage: python3 samples/v1/language_sentiment_text.py [--text_content "I am so happy and joyful."]

# from: https://github.com/googleapis/python-language/blob/main/samples/v1/language_sentiment_text.py
import json
from flask import jsonify

from google.cloud import language_v1

def sample_analyze_sentiment(text_content):
    """
    Analyzing Sentiment in a String

    Args:
      text_content The text content to analyze
    """

    client = language_v1.LanguageServiceClient()

    # text_content = 'I am so happy and joyful.'

    # Available types: PLAIN_TEXT, HTML
    type_ = language_v1.Document.Type.PLAIN_TEXT

    # Optional. If not specified, the language is automatically detected.
    # For list of supported languages:
    # https://cloud.google.com/natural-language/docs/languages
    language = "en"
    document = {"content": text_content, "type_": type_, "language": language}

    # Available values: NONE, UTF8, UTF16, UTF32
    encoding_type = language_v1.EncodingType.UTF8

    response = client.analyze_sentiment(request = {'document': document, 'encoding_type': encoding_type})
    # Get overall sentiment of the input document
    print(u"Document sentiment score: {}".format(response.document_sentiment.score))
    print(
        u"Document sentiment magnitude: {}".format(
            response.document_sentiment.magnitude
        )
    )
    # Get sentiment for all sentences in the document
    return_data = []
    for sentence in response.sentences:
        print(u"Sentence text: {}".format(sentence.text.content))
        print(u"Sentence sentiment score: {}".format(sentence.sentiment.score))
        print(u"Sentence sentiment magnitude: {}".format(sentence.sentiment.magnitude))
        return_data.append((sentence.sentiment.score, sentiment.magnitude))


    # Get the language of the text, which will be the same as
    # the language specified in the request or, if not specified,
    # the automatically-detected language.
    print(u"Language of the text: {}".format(response.language))
    return return_data


def parse_udf(request_data):
    responses = []
    for row in request_data['calls']:
        print(row)    
        scores = sample_analyze_sentiment(row[3])
        responses.append(scores)

def sentiment(request):
    request_json = request.get_json()
    sentiment_scores = parse_udf(request_json)
    response = { "replies": sentiment_scores }
    return jsonify(response)



def main():

    # sample request example from https://cloud.google.com/bigquery/docs/reference/standard-sql/remote-functions
    sample_request="""{
 "requestId": "124ab1c",
 "caller": "//bigquery.googleapis.com/projects/myproject/jobs/myproject:US.bquxjob_5b4c112c_17961fafeaf",
 "sessionUser": "test-user@test-company.com",
 "userDefinedContext": {
  "key1": "value1",
  "key2": "v2"
 },
 "calls": [
  [null, 1, "", "I am so happy and joyful."],
  [null, 1, "", "I am so sad and remorseful."]
 ]
    }"""

    parse_udf(json.loads(sample_request))



if __name__ == "__main__":
    main()