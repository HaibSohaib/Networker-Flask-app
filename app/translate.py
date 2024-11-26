import requests
from flask import current_app
from flask_babel import _

def translate(text, source_language, dest_language):
    if 'MS_TRANSLATOR_KEY' not in current_app.config or not current_app.config['MS_TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')

    # Get the key and region from the current configuration
    key = current_app.config.get('MS_TRANSLATOR_KEY')
    region = current_app.config.get('MS_TRANSLATOR_REGION')

    # Create authentication headers
    auth = {
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': region
    }

    # Make the API request
    r = requests.post(
        'https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&from={}&to={}'.format(
            source_language, dest_language),
        headers=auth,
        json=[{'Text': text}]
    )

    # Check if the request was successful
    if r.status_code != 200:
        return _('Error: the translation service failed.')

    # Return the translated text
    return r.json()[0]['translations'][0]['text']

    # Debugging outputs
    print(f"API Key: {key}")
    print(f"Region: {region}")

    if not key:
        return _('Error: the translation service is not configured.')