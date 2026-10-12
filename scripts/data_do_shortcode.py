"""Extrai a data de publicação de um post do Instagram a partir do shortcode do link.

O shortcode é o ID numérico do post em base64 (alfabeto do Instagram). Os bits altos do ID
codificam o horário de criação em milissegundos desde a "época" do Instagram (1314220021721 ms).
Conferido contra a data de publicação informada pelo yt-dlp em vários vídeos da amostra.

Uso: python3 scripts/data_do_shortcode.py DeKsl-aNeFW DdkDk87vk8q
"""
import sys, datetime

ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_"
EPOCA_INSTAGRAM_MS = 1314220021721


def data(shortcode):
    n = 0
    for c in shortcode[:11]:
        n = n * 64 + ALFABETO.index(c)
    ms = (n >> 23) + EPOCA_INSTAGRAM_MS
    return datetime.datetime.fromtimestamp(ms / 1000, datetime.timezone.utc).date()


if __name__ == "__main__":
    for sc in sys.argv[1:]:
        print(sc, data(sc))
