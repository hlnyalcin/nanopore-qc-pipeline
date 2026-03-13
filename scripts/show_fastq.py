from Bio import SeqIO

fastq_file = "barcode77.fastq"

# İlk 5 kaydı göster
for i, record in enumerate(SeqIO.parse(fastq_file, "fastq")):
    print(f"ID: {record.id}")
    print(f"Sequence: {record.seq}")
    print(f"Quality scores: {record.letter_annotations['phred_quality']}")
    print("-" * 40)
    if i == 4:
        break
