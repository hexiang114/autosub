#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Defines constants used by autosub.
"""

from __future__ import unicode_literals

GOOGLE_SPEECH_V2_API_KEY = "AIzaSyBOti4mM-6x9WDnZIjIeyEU21OpBXqWBgw"
GOOGLE_SPEECH_V2_API_URL = \
    "www.google.com/speech-api/v2/recognize?client=chromium&lang={lang}&key={key}"
DEFAULT_SUBTITLES_FORMAT = 'srt'
DEFAULT_CONCURRENCY = 10
DEFAULT_SRC_LANGUAGE = 'en-US'
DEFAULT_DST_LANGUAGE = 'en-US'
DEFAULT_ENERGY_THRESHOLD = 45
MAX_REGION_SIZE = 6.0
MIN_REGION_SIZE = 0.5
DEFAULT_CONTINUOUS_SILENCE = 0.3
MAX_EXT_REGION_SIZE = 10
# Maximum speech to text region length in milliseconds
# when using external speech region control

SPEECH_TO_TEXT_LANGUAGE_CODES = {
    'af-ZA': 'Afrikaans (South Africa)',
    'am-ET': 'Amharic (Ethiopia)',
    'ar-AE': 'Arabic (United Arab Emirates)',
    'ar-BH': 'Arabic (Bahrain)',
    'ar-DZ': 'Arabic (Algeria)',
    'ar-EG': 'Arabic (Egypt)',
    'ar-IL': 'Arabic (Israel)',
    'ar-IQ': 'Arabic (Iraq)',
    'ar-JO': 'Arabic (Jordan)',
    'ar-KW': 'Arabic (Kuwait)',
    'ar-LB': 'Arabic (Lebanon)',
    'ar-MA': 'Arabic (Morocco)',
    'ar-OM': 'Arabic (Oman)',
    'ar-PS': 'Arabic (State of Palestine)',
    'ar-QA': 'Arabic (Qatar)',
    'ar-SA': 'Arabic (Saudi Arabia)',
    'ar-TN': 'Arabic (Tunisia)',
    'az-AZ': 'Azerbaijani (Azerbaijan)',
    'bg-BG': 'Bulgarian (Bulgaria)',
    'bn-BD': 'Bengali (Bangladesh)',
    'bn-IN': 'Bengali (India)',
    'ca-ES': 'Catalan (Spain)',
    'cmn-Hans-CN': 'Chinese, Mandarin (Simplified, China)',
    'cmn-Hans-HK': 'Chinese, Mandarin (Simplified, Hong Kong)',
    'cmn-Hant-TW': 'Chinese, Mandarin (Traditional, Taiwan)',
    'cs-CZ': 'Czech (Czech Republic)',
    'da-DK': 'Danish (Denmark)',
    'de-DE': 'German (Germany)',
    'el-GR': 'Greek (Greece)',
    'en-AU': 'English (Australia)',
    'en-CA': 'English (Canada)',
    'en-GB': 'English (United Kingdom)',
    'en-GH': 'English (Ghana)',
    'en-IE': 'English (Ireland)',
    'en-IN': 'English (India)',
    'en-KE': 'English (Kenya)',
    'en-NG': 'English (Nigeria)',
    'en-NZ': 'English (New Zealand)',
    'en-PH': 'English (Philippines)',
    'en-SG': 'English (Singapore)',
    'en-TZ': 'English (Tanzania)',
    'en-US': 'English (United States)',
    'en-ZA': 'English (South Africa)',
    'es-AR': 'Spanish (Argentina)',
    'es-BO': 'Spanish (Bolivia)',
    'es-CL': 'Spanish (Chile)',
    'es-CO': 'Spanish (Colombia)',
    'es-CR': 'Spanish (Costa Rica)',
    'es-DO': 'Spanish (Dominican Republic)',
    'es-EC': 'Spanish (Ecuador)',
    'es-ES': 'Spanish (Spain)',
    'es-GT': 'Spanish (Guatemala)',
    'es-HN': 'Spanish (Honduras)',
    'es-MX': 'Spanish (Mexico)',
    'es-NI': 'Spanish (Nicaragua)',
    'es-PA': 'Spanish (Panama)',
    'es-PE': 'Spanish (Peru)',
    'es-PR': 'Spanish (Puerto Rico)',
    'es-PY': 'Spanish (Paraguay)',
    'es-SV': 'Spanish (El Salvador)',
    'es-US': 'Spanish (United States)',
    'es-UY': 'Spanish (Uruguay)',
    'es-VE': 'Spanish (Venezuela)',
    'eu-ES': 'Basque (Spain)',
    'fa-IR': 'Persian (Iran)',
    'fi-FI': 'Finnish (Finland)',
    'fil-PH ': 'Filipino (Philippines)',
    'fr-CA': 'French (Canada)',
    'fr-FR': 'French (France)',
    'gl-ES': 'Galician (Spain)',
    'gu-IN': 'Gujarati (India)',
    'he-IL': 'Hebrew (Israel)',
    'hi-IN': 'Hindi (India)',
    'hr-HR': 'Croatian (Croatia)',
    'hu-HU': 'Hungarian (Hungary)',
    'hy-AM': 'Armenian (Armenia)',
    'id-ID': 'Indonesian (Indonesia)',
    'is-IS': 'Icelandic (Iceland)',
    'it-IT': 'Italian (Italy)',
    'ja-JP': 'Japanese (Japan)',
    'jv-ID': 'Javanese (Indonesia)',
    'ka-GE': 'Georgian (Georgia)',
    'km-KH': 'Khmer (Cambodia)',
    'kn-IN': 'Kannada (India)',
    'ko-KR': 'Korean (South Korea)',
    'lo-LA': 'Lao (Laos)',
    'lt-LT': 'Lithuanian (Lithuania)',
    'lv-LV': 'Latvian (Latvia)',
    'ml-IN': 'Malayalam (India)',
    'mr-IN': 'Marathi (India)',
    'ms-MY': 'Malay (Malaysia)',
    'nb-NO': 'Norwegian Bokmal (Norway)',
    'ne-NP': 'Nepali (Nepal)',
    'nl-NL': 'Dutch (Netherlands)',
    'pl-PL': 'Polish (Poland)',
    'pt-BR': 'Portuguese (Brazil)',
    'pt-PT': 'Portuguese (Portugal)',
    'ro-RO': 'Romanian (Romania)',
    'ru-RU': 'Russian (Russia)',
    'si-LK': 'Sinhala (Sri Lanka)',
    'sk-SK': 'Slovak (Slovakia)',
    'sl-SI': 'Slovenian (Slovenia)',
    'sr-RS': 'Serbian (Serbia)',
    'su-ID': 'Sundanese (Indonesia)',
    'sv-SE': 'Swedish (Sweden)',
    'sw-KE': 'Swahili (Kenya)',
    'sw-TZ': 'Swahili (Tanzania)',
    'ta-IN': 'Tamil (India)',
    'ta-LK': 'Tamil (Sri Lanka)',
    'ta-MY': 'Tamil (Malaysia)',
    'ta-SG': 'Tamil (Singapore)',
    'te-IN': 'Telugu (India)',
    'th-TH': 'Thai (Thailand)',
    'tr-TR': 'Turkish (Turkey)',
    'uk-UA': 'Ukrainian (Ukraine)',
    'ur-IN': 'Urdu (India)',
    'ur-PK': 'Urdu (Pakistan)',
    'vi-VN': 'Vietnamese (Vietnam)',
    'yue-Hant-HK': 'Chinese, Cantonese (Traditional, Hong Kong)',
    'zu-ZA': 'Zulu (South Africa)'
}

TRANSLATION_LANGUAGE_CODES = {
    'af': 'Afrikaans',
    'am': 'Amharic',
    'ar': 'Arabic',
    'az': 'Azerbaijani',
    'be': 'Belarusian',
    'bg': 'Bulgarian',
    'bn': 'Bengali',
    'bs': 'Bosnian',
    'ca': 'Catalan',
    'ceb': 'Cebuano',
    'co': 'Corsican',
    'cs': 'Czech',
    'cy': 'Welsh',
    'da': 'Danish',
    'de': 'German',
    'el': 'Greek',
    'en': 'English',
    'eo': 'Esperanto',
    'es': 'Spanish',
    'et': 'Estonian',
    'eu': 'Basque',
    'fa': 'Persian',
    'fi': 'Finnish',
    'fr': 'French',
    'fy': 'Frisian',
    'ga': 'Irish',
    'gd': 'Scots Gaelic',
    'gl': 'Galician',
    'gu': 'Gujarati',
    'ha': 'Hausa',
    'haw': 'Hawaiian',
    'he': 'Hebrew',
    'hi': 'Hindi',
    'hmn': 'Hmong',
    'hr': 'Croatian',
    'ht': 'Haitian Creole',
    'hu': 'Hungarian',
    'hy': 'Armenian',
    'id': 'Indonesian',
    'ig': 'Igbo',
    'is': 'Icelandic',
    'it': 'Italian',
    'iw': 'Hebrew',
    'ja': 'Japanese',
    'jw': 'Javanese',
    'ka': 'Georgian',
    'kk': 'Kazakh',
    'km': 'Khmer',
    'kn': 'Kannada',
    'ko': 'Korean',
    'ku': 'Kurdish',
    'ky': 'Kyrgyz',
    'la': 'Latin',
    'lb': 'Luxembourgish',
    'lo': 'Lao',
    'lt': 'Lithuanian',
    'lv': 'Latvian',
    'mg': 'Malagasy',
    'mi': 'Maori',
    'mk': 'Macedonian',
    'ml': 'Malayalam',
    'mn': 'Mongolian',
    'mr': 'Marathi',
    'ms': 'Malay',
    'mt': 'Maltese',
    'my': 'Myanmar(Burmese)',
    'ne': 'Nepali',
    'nl': 'Dutch',
    'no': 'Norwegian',
    'ny': 'Nyanja(Chichewa)',
    'pa': 'Punjabi',
    'pl': 'Polish',
    'ps': 'Pashto',
    'pt': 'Portuguese(Portugal,Brazil)',
    'ro': 'Romanian',
    'ru': 'Russian',
    'sd': 'Sindhi',
    'si': 'Sinhala(Sinhalese)',
    'sk': 'Slovak',
    'sl': 'Slovenian',
    'sm': 'Samoan',
    'sn': 'Shona',
    'so': 'Somali',
    'sq': 'Albanian',
    'sr': 'Serbian',
    'st': 'Sesotho',
    'su': 'Sundanese',
    'sv': 'Swedish',
    'sw': 'Swahili',
    'ta': 'Tamil',
    'te': 'Telugu',
    'tg': 'Tajik',
    'th': 'Thai',
    'tl': 'Tagalog(Filipino)',
    'tr': 'Turkish',
    'uk': 'Ukrainian',
    'ur': 'Urdu',
    'uz': 'Uzbek',
    'vi': 'Vietnamese',
    'xh': 'Xhosa',
    'yi': 'Yiddish',
    'yo': 'Yoruba',
    'zh': 'Chinese (Simplified)',
    'zh-CN': 'Chinese (Simplified)',
    'zh-TW': 'Chinese (Traditional)',
    'zu': 'Zulu'
}

FORMATTERS = {
    'srt': 'SubRip',
    'ass': 'Advanced SubStation Alpha',
    'ssa': 'SubStation Alpha',
    'sub': 'MicroDVD Subtitle',
    'mpl2': 'Similar to MicroDVD(extension is \".mpl2.txt\")',
    'tmp': 'TMP Player Subtitle Format',
    'vtt': 'WebVTT',
    'json': 'json',
    'txt': 'Plain Text(Only text without times)'
}
