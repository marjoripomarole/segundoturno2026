#!/bin/zsh
# Baixa, extrai quadros e transcreve vídeos do Instagram a partir dos shortcodes.
# Uso: scripts/processar_videos.sh PASTA_DE_SAIDA SHORTCODE1 SHORTCODE2 ...
# Requer: yt-dlp, ffmpeg, openai-whisper (modelo "small"), python3.
# Os vídeos baixados ficam fora do repositório (não redistribuir); só transcrições e metadados são versionados.
set -u
OUT="$1"; shift
mkdir -p "$OUT"; cd "$OUT"
wavs=()
for id in "$@"; do
  yt-dlp -q --no-warnings -f "best[ext=mp4]/best" --write-info-json -o "%(id)s.%(ext)s" "https://www.instagram.com/reel/$id/" 2>&1 | tail -1
  [ -f "$id.mp4" ] || { echo "#### $id FALHOU (post sem vídeo ou indisponível)"; continue; }
  ffmpeg -v error -y -i "$id.mp4" -vn -ac 1 -ar 16000 "$id.wav"                                     # áudio mono 16 kHz para o Whisper
  ffmpeg -v error -y -i "$id.mp4" -vf "fps=1/6,scale=200:-1,tile=4x3" -frames:v 1 "${id}_frames.jpg" # folha de quadros (1 a cada 6 s)
  wavs+=("$id.wav")
done
[ ${#wavs[@]} -gt 0 ] && whisper "${wavs[@]}" --language pt --model small --output_format txt --output_dir . >/dev/null 2>&1
for id in "$@"; do
  [ -f "$id.info.json" ] || continue
  python3 -I -c '
import json,sys; d=json.load(open(sys.argv[1]+".info.json"))
print("\n####",sys.argv[1]); [print(k,":",d.get(k)) for k in ["uploader","channel","upload_date","like_count","comment_count"]]; print("description:",d.get("description"))' "$id"
  echo "--- transcrição"; cat "$id.txt" 2>/dev/null
done
