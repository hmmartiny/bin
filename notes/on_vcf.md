# Notes on working with VCF files
VCF = Variant Call Format

## Sources:
* [Comparing VCF files by Dave Tang](https://davetang.org/muse/2019/09/02/comparing-vcf-files/)
* [SNP Filtering Tutorial on dDocent](http://www.ddocent.com/filtering/)
* [SNP calling workflow](http://userweb.eng.gla.ac.uk/cosmika.goswami/snp_calling/SNPCalling.html)

## Setup
Installing on MacOS Catalina with homebrew:
```bash
brew tap brewsci/bio
brew install samtools
brew install bcftools
brew install vcftools
```

## Filtering
### Filter for depth to be at least `n` (`depth >= n`)
Depth filtering ensures that all positions are covered by a minimum number of reads. 

Here the cut-off is at 10, meaning that we want a depth of at least 10 reads.
```bash
bcftools filter -i 'DP>=10' sample.vcf.gz -Oz -o sample.filtered.vcf.gz
```

It can also be done with vcftools
```bash
vcftools --gzvcf sample.vcf.gz --minDP 10 ..
```

### Filtering for mapping quality
Quality filtering should be done to filter out positions that are poor and most likely cannot be trusted.

```bash
vcftools --gzvcf sample.vcf.gz --minQ 25 ..
```

### Combining the above filters into one command
```bash
vcftools --gzvcf sample.vcf.gz --minQ 25 --minDP 10 --recode --recode-INFO-all --remove-filtered-all --out sample.filtered
```
Output file in this case is named sample.filtered.recode.vcf

To only look at the SNPs by filtering out indel mutations, run:
```bash
vcftools --gzvcf sample.vcf.gz --minQ 25 --minDP 10 --recode --recode-INFO-all --remove-indels --remove-filtered-all --out sample.snps
```

skal det være minGQ i stedet?

### Filter variants 
This uses both bcftools to view the file and vcftools to filter:
```bash
bcftools view sample.vcf.gz | vcfutils.pl varFilter - > sample.varfilter.vcf
```

## Merging files 
Assuming you are in a directory with vcf.gz files:
```bash
bcftools merge *.vcf.gz | bgzip > all_merged.vcf.gz
```
## Consensus sequences
Create consensus sequences from VCF file and a reference fasta file with 
```bash
bcftools consensus -f fasta.ref file.vcf.gz -o out.fa
```

If you need to retrieve the reference sequences from another FASTA file first, do the following:
1. Retrieve the IDs of the corresponding sequences first by grep:
```bash
grep "^>" input.fasta | sed 's/>//' | grep mcr > retrieved_ids.txt
```
2. Then extract sequences matching the retrieved IDs with `samtools faidx`:
```bash
samtools faidx input.fasta $(cat retrieved_ids.txt) > fasta.ref
```
3. Then run `bcftools consensus`:
```bash
bcftools consensus -f fasta.ref file.vcf.gz -o out.fa
```


## Other stuff
### Count total number of SNPs:
```bash
bcftools view -v snps sample.vcf.gz | grep -v '^#' | wc -l
```

do it per sample and with filter PASS: 
```bash
bcftools view multisample.vcf.gz -s sample_id -f PASS -v snps | grep -v  "^#" | wc -l
```

Command explained:
- `bcftools view -v snps`: select only snps to view 


### Statistics on the VCF file
```bash
bcftools stats sample.vcf.gz > sample.stats
```
