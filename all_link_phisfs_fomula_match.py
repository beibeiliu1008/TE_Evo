import sys
import math
filename = sys.argv[1]
matched_filename = f'{filename.replace(".txt",".matched.txt")}'
chrm1_8_filename = f'{filename.replace(".txt",".chrm.1.8.txt")}'
chrm9_10_filename = f'{filename.replace(".txt",".chrm.9.10.txt")}'
matched_chrm1_8_filename = f'{filename.replace(".txt",".chrm.1.8.matched.txt")}'

####split the file both the TE and the sampled snp file into two files
#####chrm1-8 (have 26 samples) and chrm9-10 files (have 25 samples)

def split_chrm(filename):
    with open(filename) as f:
        with open(chrm1_8_filename,'w') as nf:
            with open(chrm9_10_filename,'w') as nf1:
                for line in f:
                    line = line.strip('\n').split('\t')
                    if line[5] != '9' and line[5] != '10':
                        # freqency = int(line[6])
                        newline = '\t'.join(line)
                        nf.write(f'{newline}\n')
                    else:
                        # freqency = round(float(line[-2]) * 24,0)
                        newline = '\t'.join(line)
                        nf1.write(f'{newline}\n')
split_chrm(filename)

####get the counts for each frequency (1 to 26) from chrom1-8

def get_freqbin_count(chrm1_8_filename):
    frequency_count = {}
    with open(chrm1_8_filename) as f:
        for line in f:
            line = line.strip('\n').split('\t')
            frequency = int(line[6])
            frequency_count.setdefault(frequency,[]).append(line[0])
    return frequency_count


frequency_count = get_freqbin_count(chrm1_8_filename)

# ###these is the fomula used to reassign the possibility of each frequency
#
def funmulti(fj, i):
    prob_list = []
    for num in i:
        prob = (math.comb(fj, num) * math.comb(26 - fj, 25 - num)) / math.comb(26, 25)
        prob_list.append(prob)
    return prob_list

# ###get the matched chrom1-8 using the formula
#
def matched_chrm1_8(matched_chrm1_8_filename):
    with open(matched_chrm1_8_filename,'w')as nf:
        nf.write(f'original_freq\tmatched_freq\tmatched_count\n')
        num = list(range(0,26))
        for key,value in frequency_count.items():
            fj = int(key)
            #print(fj)
            count = len(value)
            #print(count)
            prob_list = funmulti(fj,num)[1:25]
            #print(prob_list)
            #print(len(prob_list))
            for i in range(1,25):
                name = f'{fj}_{i}'
                matched_count = round(prob_list[i-1] * count,0)
                #matched_frequency_count[name] = matched_count
                nf.write(f'{int(fj)}\t{int(i)}\t{float(matched_count)}\n')

matched_chrm1_8(matched_chrm1_8_filename)
#
def get_matched_dict(matched_chrm1_8_filename):
    matched_frequency = {}
    with open(matched_chrm1_8_filename) as f:
        next(f)
        for line in f:
            line = line.strip('\n').split('\t')
            matched_frequency.setdefault(int(line[1]),[]).append(float(line[-1]))
    return matched_frequency

matched_frequency = get_matched_dict(matched_chrm1_8_filename)
#
def get_chrm9_10_dict(chrm9_10_filename):
    chrm9_10_frequency = {}
    with open(chrm9_10_filename) as f:
        for line in f:
            line = line.strip('\n').split('\t')
            key = int(line[6])
            chrm9_10_frequency.setdefault(key,[]).append(line[0])
    return chrm9_10_frequency
#
chrm9_10_frequency = get_chrm9_10_dict(chrm9_10_filename)
#
def get_the_final_sfs(filename):
    with open(filename) as f:
        with open(matched_filename,'w') as nf:
            num_lines = len(f.readlines())
            for key,value in matched_frequency.items():
                #print(key,value)
                count_chrm1_8 = sum(value)
                if key in chrm9_10_frequency.keys():
                    count_chrm9_10 = len(chrm9_10_frequency[key])
                    sum_count = count_chrm1_8 + count_chrm9_10
                    sfs = round(sum_count/num_lines,4)
                    nf.write(f'{key}\t{sfs}\n')
                else:
                    count_chrm9_10 = 0
                    sum_count = count_chrm1_8 + count_chrm9_10
                    sfs = round(sum_count/num_lines,4)
                    nf.write(f'{key}\t{sfs}\n')


get_the_final_sfs(filename)






