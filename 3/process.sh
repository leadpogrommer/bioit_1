#!/bin/bash

set -e
set -o xtrace

if [[ $# -ne 3 ]] ; then
    echo "Usage: $0 <reference> <fasta> <output_dir>"
    exit 1
fi

REF_PATH="$1"
FASTA_PATH="$2"
OUT_PATH="$3"
NPROC=$(nproc)


mkdir -p "$OUT_PATH"


fastqc -o "$OUT_PATH" -t "$NPROC" "$FASTA_PATH"

bwa mem -t "$NPROC" "$REF_PATH" "$FASTA_PATH" > "$OUT_PATH/result.sam"

samtools view --threads "$NPROC" -b "$OUT_PATH/result.sam" > "$OUT_PATH/result.bam"

QUALITY=$(samtools flagstat --threads "$NPROC" "$OUT_PATH/result.bam" | python3 -c 'from sys import stdin; d=stdin.read(); import re; print(re.findall(r"\d+\s+\+\s+\d+\s+mapped\s+\((\d+\.\d+)%", d)[0])')
echo "Quality = $QUALITY"

if python3 -c 'a,b = map(float, input().split())'$'\n''if a < b: exit(1)' <<< "$QUALITY 90.0" ;then
    echo "Quality is ok"
else
    echo "Quality is not ok"
    exit 0
fi

samtools sort --threads "$NPROC" -T "$OUT_PATH/sam_tmp" "$OUT_PATH/result.bam" > "$OUT_PATH/result.sorted.bam"

freebayes -f "$REF_PATH" "$OUT_PATH/result.sorted.bam" > "$OUT_PATH/result.vcf"