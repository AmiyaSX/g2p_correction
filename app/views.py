from flask import render_template, request, url_for, redirect
import datetime
import os

import tts_reader

def text_to_audio():
    print(f'{request.method=}')
    print(f'{request.form=}')
    if request.method == 'POST':
        text = request.form['text']
        if text:
            audio = tts_reader.read_text(text)
            word2phoneme_audio = tts_reader.read_words(text)
            print(f"{request.form.getlist('word')=}")
            return render_template(
                'text-to-audio.html', audio=audio,
                text=text, word2phoneme_audio=word2phoneme_audio
            )

    return render_template('text-to-audio.html')


def grapheme_log_view(grapheme_id):
    # from app.db_utils import fetch_grapheme_logs, fetch_grapheme
    # from app.models import Grapheme

    grapheme_logs = [
    ('ruislip', 'ɹˈaɪslɪp', 'ɹˈaɪslɪp', datetime.datetime(2024, 3, 11, 14, 53, 55, 20387)),
    ('ruislip', 'ɹˈaɪslɪpi:p', 'ɹˈaɪslɪp', datetime.datetime(2024, 3, 11, 14, 40, 47, 976755)),
    ('ruislip', 'sɒbaka', 'ɹˈaɪslɪpi:p', datetime.datetime(2024, 3, 11, 14, 40, 32, 181943)),
    ('ruislip', 'ɹˈaɪslɪp', 'sɒbaka', datetime.datetime(2024, 3, 11, 14, 39, 50, 972417)),
    ('ruislip', 'ɹˈuːɪslɪp', 'ɹˈaɪslɪp', datetime.datetime(2024, 3, 11, 14, 39, 3, 72773)),
    ('ruislip', 'ɹˈaɪslɪp', 'ɹˈuːɪslɪp', datetime.datetime(2024, 3, 11, 14, 38, 26, 49876)),
    ('ruislip', 'ɹˈuːɪslˈɪp', 'ɹˈaɪslɪp', datetime.datetime(2024, 3, 11, 14, 38, 14, 283224)),
    ('ruislip', 'ɹˈuːɪslɪp', 'ɹˈuːɪslˈɪp', datetime.datetime(2024, 3, 11, 14, 37, 18, 210686)),
    ('ruislip', "ɹ'aɪslɪp", 'ɹˈuːɪslɪp', datetime.datetime(2024, 3, 11, 14, 35, 57, 696221)),
    ('ruislip', None, "ɹ'aɪslɪp", datetime.datetime(2024, 3, 11, 14, 20, 27, 147224))]
    grapheme, phoneme = ['ruislip', 'ruislip']

    return render_template(
        'grapheme-log.html', 
        grapheme=grapheme,
        phoneme=phoneme,
        grapheme_logs=grapheme_logs)


