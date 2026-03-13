from Bio import SeqIO

fastq_file = "barcode77.fastq"

for i, record in enumerate(SeqIO.parse(fastq_file, "fastq")):
    print(f"{record.id} min quality: {min(record.letter_annotations['phred_quality'])}")
    if i == 9:  # ilk 10 kaydı kontrol et
        break
